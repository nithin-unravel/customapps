import yaml
unhealthy_list=[]
with open('/opt/unravel/data/apps/UnravelStatusDashboard/unravel_status_dashboard/data/short_status.yaml', 'r') as file:
    data = yaml.safe_load(file)
for key,value in data.items():
    if value == 'FALSE':
        unhealthy_list.append(key)
print(unhealthy_list)
       
