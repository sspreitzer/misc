import imaplib
import re

class g(object):
    def __init__(self, user, password):
        self._M = imaplib.IMAP4_SSL("imap.googlemail.com")
        self._M.login(user, password)
        self._M.select("[Gmail]/Alle Nachrichten")
        
    def getFilterByYear(self, year="2012"):
        return "(SINCE 01-Jan-" + str(year) + " BEFORE 31-Dec-" + str(year) + ")"
    
    def getList(self, filter="ALL"):
        return self._M.search(None, filter)[1][0].split()
    
    def getCount(self, filter="ALL"):
        return len(self.getList(filter))
    
    def fetchRFC822(self, num):
        return self._M.fetch(num, "(RFC822)")[1][0][1]
    
    def getSubject(self, message):
        try:
            subj = re.search("^[Ss]ubject:\ (.*)$", message, re.M).group(1)
        except:
            return ""
        return subj[:len(subj)-1]

    def __getitem__(self, num):
        return self.fetchRFC822(num)
    
    def __len__(self):
        return self.getCount()
    