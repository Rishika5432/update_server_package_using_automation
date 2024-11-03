#!/bin/bash

# Run the Ansible playbook
cd "/testing_automation/"
INVENTORY_FILE="linux_host.json"
PLAYBOOK_FILE="update_redhat_package_status_automation.yml"

# Run the CSV to JSON conversion script
 python3 csv_to_json_convert.py "$1"
 echo "file converted to  CSV to JSON"

echo "Running Ansible playbook..."
ansible-playbook "$PLAYBOOK_FILE" -i "$INVENTORY_FILE"

# Check if the Ansible command was successful
if [[ $? -eq 0 ]]; then
	echo "Ansible playbook executed successfully."
else 
	echo "Ansible playbook execution failed."
	exit 1
fi 
echo "Script completed."

