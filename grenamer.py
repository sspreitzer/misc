import gmap
import getpass
import threading
import os
import string

username    = ""
password    = ""
years       = [2008, 2009, 2010, 2011] # change to your needs

class worker(threading.Thread):
    def __init__(self, year):
        threading.Thread.__init__(self)
        self.year = year
        
    def run(self):
        g = gmap.g(username, password)
        f = g.getFilterByYear(self.year)
        msgnums = g.getList(f)
        
        try:
            os.mkdir(str(self.year))
        except:
            pass
        
        for msgnum in msgnums:
            if os.access(str(self.year) + "/" + str(msgnum), os.F_OK|os.R_OK):
                oldname = str(self.year) + "/" + str(msgnum)
                msg = open(oldname, "r")
                subj = g.getSubject(msg.read())
                msg.close()
                newname = oldname + "." + string.replace(subj[:20], "/", " ") + ".eml"
                print newname
                os.rename(oldname, newname)

if username == "":
    username = raw_input("Username: ")
    
if password == "":
    password = getpass.getpass("Password: ")

for year in years:
    w = worker(year)
    w.start()
    
    
