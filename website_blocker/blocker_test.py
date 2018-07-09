#Program to block certain websites at certain times of the day
#
# For path, can either use r"..." (raw pathname)  to ensure that none
# of the characters in the path are interpreted as special characters
# or can use double \\  e.g. c:\\windows\\system32\\....
#
import time
from datetime import datetime as dt

hosts_temp="hosts"
#hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.bing.com","bing.com"]

while True:
    if 7 <= dt.now().hour <= 16:
        print ("Working hours.....7am - 4pm")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                    if website in content:
                        print ("In content")
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
                        print ("Writing to file")
    else:
        print ("Fun hours....before 7am and after 4pm")
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                print(line)
                if not any (website in line for website in website_list):
                        file.write(line)
            file.truncate()

    time.sleep(5)
