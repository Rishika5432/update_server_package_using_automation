# Project: Automated YUM Package Update and CSV to JSON Inventory Conversion

This project provides automation for:
1. Updating YUM packages on multiple hosts using Ansible.
2. Converting an Ansible host inventory file from CSV format to JSON format using Python.

## Table of Contents
- [Requirements](#requirements)
- [Files](#files)
- [Usage](#usage)
  - [Step 1: Update YUM Packages Using Ansible](#step-1-update-yum-packages-using-ansible)
  - [Step 2: Convert CSV Inventory to JSON Using Python](#step-2-convert-csv-inventory-to-json-using-python)
- [License](#license)

---

## Requirements

- **Ansible**: Install Ansible on your control machine to manage and execute playbooks.
- **Python**: Ensure Python 3 is installed on your system.
- **Git**: To clone the repository.

## Files

- **update_yum_packages.yml**: Ansible playbook to update YUM packages on all hosts listed in the inventory file.
- **csv_to_json_convert.py**: Python script to convert a CSV host inventory file into JSON format.
- **your_inventory.csv**: Sample CSV file used as an Ansible host inventory (replace with your actual inventory file).

## Usage

### Step 1: Update YUM Packages Using Ansible

This step updates all YUM packages on the hosts listed in the CSV inventory file.

1. **Edit the Inventory File**:
   - Make sure `your_inventory.csv` contains the hosts you want to target.
   - Replace `your_inventory.csv` with the path to your actual inventory file in the command below.

2. **Run the Playbook**:
   - Use the following command to execute the playbook:
     ```bash
     ansible-playbook -i your_inventory.csv update_yum_packages.yml
     ```

   - This will install the latest version of all YUM packages on each host specified in the inventory file.

### Step 2: Convert CSV Inventory to JSON Using Python

This step converts the CSV inventory file into a JSON format.

1. **Run the Python Script**:
   - Make sure your CSV inventory file path is correctly set in `csv_to_json_convert.py`.
   - Execute the script:
     ```bash
     python csv_to_json_convert.py
     ```

2. **Output**:
   - The script will generate a `inventory.json` file, which contains the host data in JSON format.

### Example

Here’s an example of what your `your_inventory.csv` file might look like:

```csv
hostname,ip_address,group
server1,192.168.1.1,web
server2,192.168.1.2,db
