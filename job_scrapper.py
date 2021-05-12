from indeed import indeed_fun
from simply_hired import sh_fun

job_name = input("Enter Job Name\n")
job_location = input("Enter Job Location\n")

print("Jobs from Indeed\n")
indeed_fun(job_name, job_location)

print("Jobs from Simply Hired\n")
sh_fun(job_name, job_location)
