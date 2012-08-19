import gmap
import getpass
import threading
import os

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
            if not os.access(str(self.year) + "/" + str(msgnum), os.F_OK):
                print self.year, round(float(msgnum) / float(msgnums[len(msgnums)-1]) * 100, 2)
                e = open(str(self.year) + "/" + str(msgnum), "w+")
                msg = g[msgnum]
                e.write(msg)
                e.close()

        

if username == "":
    username = raw_input("Username: ")
    
if password == "":
    password = getpass.getpass("Password: ")

for year in years:
    w = worker(year)
    w.start()
    
    
