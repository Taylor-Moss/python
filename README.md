# Python Cloud Automation Scripts

## Overview

This repository contains Python scripts focused on automating AWS operational tasks related to storage management and backup monitoring.

The scripts demonstrate the use of the AWS SDK (`boto3`) to interact with cloud services programmatically, enabling efficient and repeatable infrastructure operations.

---

## Use Cases Covered

* Backup job inspection and recovery point analysis
* S3 bucket cleanup and resource management
* Automation of routine cloud maintenance tasks

---

## Script Breakdown

### Backup & Recovery

* **describe-backup-job-rpo.py**
  Retrieves and analyzes AWS Backup job information to determine Recovery Point Objective (RPO) characteristics.
  Useful for validating backup compliance and understanding recovery timelines.

---

### Storage Management

* **wipe-bucket.py**
  Deletes all objects within an S3 bucket.
  Intended for cleanup scenarios such as decommissioning environments or resetting test resources.

---

## Technologies Used

* Python
* boto3 (AWS SDK)
* AWS Services:

  * S3
  * AWS Backup

---

## Usage

### Prerequisites

* AWS CLI configured (`aws configure`)
* Appropriate IAM permissions for S3 and AWS Backup

### Run Scripts

```bash
python describe-backup-job-rpo.py
python wipe-bucket.py
```

---

## Safety Considerations

* **wipe-bucket.py** performs destructive actions
* Always validate the target bucket before execution
* Recommended to test in non-production environments

---

## Purpose

This repository demonstrates:

* Programmatic interaction with AWS services
* Automation of operational cloud tasks
* Use of Python for infrastructure and maintenance workflows

---

## Future Improvements

* Add argument parsing (e.g., `argparse`)
* Implement logging and error handling
* Add dry-run mode for destructive operations
* Convert scripts into reusable modules or CLI tools

---

## Notes

These scripts are designed for specific operational use cases and may require modification before use in different environments.

---

## Author Notes

Part of a cloud engineering portfolio focused on automation, operational tooling, and AWS-based workflows.
