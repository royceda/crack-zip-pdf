import string
from threading import Thread, RLock
import sys
import zipfile
#import pyPdf



#pdf = pyPdf.PdfFileReader(open(toto.pdf))


lock        = RLock()
zfile       = zipfile.ZipFile('Pi.zip')
name        = zfile.namelist()
thread      = []
tab         = []
charset_tab = [string.printable, string.ascii_lowercase, string.ascii_uppercase, string.ascii_letters,string.digits, string.hexdigits, string.punctuation]



length_max = 4
password   = ''
finished   = False

print str(name)

def brute(string, length, charset,tid):
    global finished
    global password

    if finished == True:
        with lock:
            try:
                zfile.read(name[0], pwd=password)
                exit()
            except:
                finished == False

    if len(string) == length:
        return string
    for char in charset:
        temp = string + char
        try:
            with lock:
                zfile.read(name[0], pwd=password)
                finished = True
                #pdf.decrypt(temp)
                print "Thread "+str(tid)+" found: "+temp
                password = temp
            exit()
        except:
            qry = temp +" nThread "+str(tid)+" "+str(finished)+"\n"
            #print qry
            with lock:
                tab.append(temp)
            brute(temp, length, charset, tid)



class Brute(Thread):
    def __init__(self, id, charset, length):
        Thread.__init__(self)
        self.id = id
        self.charset = charset
        self.length = length
        self.init = ''
        self.process = None

    def run(self):
        brute(self.init, self.length, self.charset, self.id)



#for length in range(1, 8):
for i in range(0, len(charset_tab)):
    c = Brute(i, charset_tab[i], length_max)
    thread.append(c)

for t in thread:
    print "thread "+str(t)
    t.start()
    print "thread "+str(t)


while(finished == False):
    a = 1;


for t in thread:
    print "thread "+str(t)
    t.join()


zfile.extractall(pwd=password)
print "password: "+password
