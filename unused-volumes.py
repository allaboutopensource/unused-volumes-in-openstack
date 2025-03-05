#!/usr/bin/python3
import openstack
from datetime import datetime, timedelta

conn = openstack.connect(cloud='openstack')
conn2 = conn.connect_as(username = os.environ.get('OS_USERNAME'), password = os.environ.get('OS_PASSWORD'))
cloud2 = conn.connect_as_project('7b9b3c86a8asdsd1cdc8234317ae190')

# Get all projects
projects = cloud2.identity.projects()

current_dt = datetime.now()
old_volume = current_dt - timedelta(days=12*30)

# Iterate over projects and count instances

for project in projects:
              print(f"Project Name: {project.name}\n")
#              print("=============================================================================================")
              for vol in cloud2.block_storage.volumes(all_projects=True, project_id=project.id):
  #                   print(f"volume name:{vol.name} and vol create at:{vol.created_at}")
                     created_at_date = datetime.strptime(vol.created_at, "%Y-%m-%dT%H:%M:%S.%f")
 #                    print(created_at_date)
                     if created_at_date < old_volume and vol.status=="available":
                            print(f"Volume name {vol.name} current Status: {vol.status} created on date {created_at_date} is older than 1 year.")
