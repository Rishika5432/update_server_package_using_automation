#!/bin/bash
#setup files 
INVENTORY_FILE="linux-host-config.json"
PLAYBOOK_FILE="Redhat-package-status-automation.yml"

# Run the CSV to JSON conversion script
 python3 convert-csv-to-json.py "$1"
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

