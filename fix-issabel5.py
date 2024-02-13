#!/usr/bin/python3

### import modules
import os

print()
a = input("Please enter asteriskuser password for mysql\n")
b = input("Please enter root password for mysql\n")

cmd = "grant all privileges on asteriskcdrdb.* to 'asteriskuser'@'localhost' identified by '"+a+"'"
c = 'mysql -uroot -p'+b+' -e "'+cmd+'"'
os.system(c)

cmd = "use asteriskcdrdb; alter table cel alter eventextra set default 'NA'"
c = 'mysql -uroot -p'+b+' -e "'+cmd+'"'
os.system(c)

os.system("cp queues.conf /etc/asterisk/")
os.system("cp musiconhold.conf /etc/asterisk/")

print("Fixing Issabel5 Completed!!!\n")
