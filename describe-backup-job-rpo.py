import boto3
import os

# build the client
client = boto3.client('backup')

# first step: DescribeBackupJob
backup_job_id = 'JOB-ID'

describe_backup_job = client.describe_backup_job(
    BackupJobId=backup_job_id
)

backup_job_details = describe_backup_job['BackupJobId']

# second step: GetBackupPlan
plan_id = describe_backup_job['CreatedBy']['BackupPlanId']
rule_id = describe_backup_job['CreatedBy']['BackupRuleId']

get_backup_plan = client.get_backup_plan(
    BackupPlanId=plan_id
)

resource_type = describe_backup_job['ResourceType']
resource_arn = describe_backup_job['ResourceArn']
job_status = describe_backup_job['State']
frequency = get_backup_plan['BackupPlan']['Rules']
target = rule_id

# find the index of the rule
index = None
for i, item in enumerate(frequency):
    if item['RuleId'] == target:
        index = i
        break

scheduleExpression = get_backup_plan['BackupPlan']['Rules'][i]['ScheduleExpression']

try:
    destination_vault = get_backup_plan['BackupPlan']['Rules'][i]['CopyActions']
except KeyError:
    destination_vault = 'no_copy_actions_on_rule'

# third step: create a hash table output
table = {
    'resource_type': resource_type,
    'resource_arn': resource_arn,
    'job_id': backup_job_details,
    'job_status': job_status,
    'frequency': frequency,
    'copy_actions': destination_vault
}

print(table)