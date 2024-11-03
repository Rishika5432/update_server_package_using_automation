import csv 
import sys
import json  
def csv_to_json(csv_file) : 
 inventory = {"all": {"children": {"linux_servers": {"hosts": {}} , "windows_servers" : {"hosts" : {} }}}} 
 with open (csv_file , 'r') as csv_file :
    csv_file=csv.DictReader(csv_file)
    for row in csv_file : 
        hostname = row["hostname"]
        ansible_user = row["ansible_user"]
        ansible_password = row["ansible_password"]
        os_type = row["os_type"].lower()
        if os_type == "linux": 
         inventory["all"]["children"]["linux_servers"]["hosts"][hostname] = {"ansible_host":hostname}
         inventory["all"]["children"]["linux_servers"]["hosts"][hostname] = {"ansible_host":hostname,"ansible_user": ansible_user,"ansible_password": ansible_password}
        elif os_type == "windows":
            inventory["all"]["children"]["windows_servers"]["hosts"][hostname] = {"ansible_host":hostname}
            inventory["all"]["children"]["windows_servers"]["hosts"][hostname] = {"ansible_host":hostname,"ansible_user": ansible_user,"ansible_password": ansible_password}
 return inventory   
#print(csv_to_json("Book.csv"))
if __name__ == "__main__":
  csv_file = sys.argv[1]  # Pass the CSV file as an argument
  inventory=csv_to_json(csv_file)
  with open("linux_host.json",'w') as file  : 
    json.dump(inventory,file,indent=5)
  print("Ansible inventrory file is ready ")

 
 
