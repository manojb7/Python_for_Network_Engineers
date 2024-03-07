#script to validate the IP address file

import os.path
import sys

#Checking IP address file and content validity
def ip_file_validity(ip_file):
    #prompting user for the file
    ip_file = input("\n# Enter IP file path and name (e.g. /path/to/file.txt): ")
    #Check if the file exists
    if os.path.isfile(ip_file) == True:
        print("IP file is valid")
    else:
        print(f"The file {ip_file} does not exist")
        sys.exit()

    #Open user selected file for reading (IP addresses file)
    # selected_ip_file = open(ip_file, 'r')

    #Starting from the beginning of the file
    # selected_ip_file.seek(0)

    #Reading each line (IP address) in the file
    # ip_file_lines = selected_ip_file.readlines()

    #Closing the file
    # selected_ip_file.close()
    
    #open the file and read the content
    with open(ip_file, 'r') as selected_ip_file:
        ip_file_lines = selected_ip_file.readlines()

    #Checking if the file is empty
    if len(ip_file_lines) == 0:
        print(f"The file {ip_file} is empty")
        sys.exit()
    return ip_file_lines

#Calling the function
ips = ip_file_validity('ip_file')
#Printing the returned value
for ip in ips:
    ip = ip.rstrip("\n")
    print(ip)