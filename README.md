
# 🛠️ Automation Project: Effortless CSV to JSON Conversion & YUM Package Management

Welcome to the **Automation Project**, where we streamline the process of managing your Red Hat servers with cutting-edge automation tools. This project simplifies the conversion of your CSV Ansible inventory files to JSON format and seamlessly updates YUM packages across your servers. 

## 🚀 Overview
In today’s fast-paced IT landscape, efficiency is key. This project combines Python scripting, Ansible playbooks, and Bash scripting to create an automated workflow that:
- Converts CSV inventory files into a structured JSON format.
- Updates all YUM packages to their latest versions on your Red Hat servers.
- Records the status of package updates for your records.

## 📦 Components

### 1. **CSV to JSON Converter**: `csv_to_json.py`
Transform your inventory CSV file into a JSON format that Ansible loves! This Python script makes it easy to prepare your inventory for deployment.

```python
# Read and convert CSV to JSON
import csv
import json

# Function to convert
def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open(json_file_path, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

# Usage
csv_to_json('inventory.csv', 'inventory.json')
```

### 2. **YUM Package Updater**: `update_yum.yml`
Using Ansible, this playbook ensures your packages are up-to-date, enhancing security and stability.

```yaml
---
- name: Update YUM packages on Red Hat servers
  hosts: all
  become: yes
  tasks:
    - name: Update all installed packages
      yum:
        name: '*'
        state: latest
      register: yum_update_result

    - name: Write package status to a file
      copy:
        content: "{{ yum_update_result }}"
        dest: "yum_update_status.txt"
```

### 3. **Run All Script**: `run_all.sh`
A simple Bash script that ties everything together. Run it to execute the entire process in one command!

```bash
#!/bin/bash

# Convert CSV to JSON
python csv_to_json.py

# Run Ansible Playbook
ansible-playbook -i inventory.json update_yum.yml
```

## 🛠️ Installation & Usage

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-project-directory>
   ```

2. **Make the Bash Script Executable**:
   ```bash
   chmod +x run_all.sh
   ```

3. **Run the Script**:
   Execute the complete automation workflow with a single command:
   ```bash
   ./run_all.sh
   ```

## 🌟 Benefits
- **Efficiency**: Automate tedious tasks and free up your time.
- **Consistency**: Ensure all your servers are uniformly updated.
- **Documentation**: Keep track of package statuses easily.

## 🤝 Contributing
We welcome contributions! If you have ideas for enhancements or fixes, feel free to submit a pull request.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgements
Thanks to [Ansible](https://www.ansible.com/) for their powerful automation framework and [Python](https://www.python.org/) for its versatility and ease of use.

---

**Ready to automate your server management? Let's get started! 🚀**
