# "C:\Users\vmp2303\Dropbox\Val_Work\Python\Training\mapping\website_blocker.pyw"
#
# Program to block certain websites at certain times of the day
# File needs to have a .pyw extension to run as a service
# Create as a task in windows scheduler - start at startup. Run as administrator
# Look for pythonw.exe task in resource monitor to see if it is running
# If it crashes, it won't write an error, so need to double-check that it is running
# once you kick it off.
#
# For path, can either use r"..." (raw pathname)  to ensure that none
# of the characters in the path are interpreted as special characters
# or can use double \\  e.g. c:\\windows\\system32\\....
#
import time
from datetime import datetime as dt

#hosts_temp=r"C:\Users\vmp2303\Dropbox\Val_Work\Python\Training\mapping\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.bing.com","bing.com"]

while True:
    if 7 <= dt.now().hour <= 16:
        #print ("Working hours.....7am - 4pm")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                    if website in content:
                        #print ("In content")
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
                        #print ("Writing to file")
    else:
        #print ("Fun hours....before 7am and after 4pm")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            update=False
            for website in website_list:
                    if website in content:
                        update=True
                        #print("Update required")
            if update:
                file.seek(0)

                content=content.splitlines()
                #print(content)
                for line in content:
                    if not any (website in line for website in website_list):
                        #print(line)
                        file.write(line + "\n")

                file.truncate()
            #else:
                #print("No update required")

    time.sleep(5)
