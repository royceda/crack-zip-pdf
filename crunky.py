import string
import threading
import sys
import zipfile
import pyPdf  


#pdf = pyPdf.PdfFileReader(open(toto.pdf))
zfile       = zipfile.ZipFile('PDF.zip')
name        = zfile.namelist()
thread      = []
tab         = []
charset_tab = [string.printable, string.ascii_lowercase, string.ascii_uppercase, string.ascii_letters,string.digits, string.hexdigits, string.punctuation]
length_max  = 10


def brute(string, length, charset, tab):
    if len(string) == length:
        return string
    for char in charset:
        temp = string + char
        try:
            zfile.extractall(pwd=temp)
            #pdf.decrypt(temp) 
            for t in thread:
                t.join()
                print "password found !! "+string
                return string
        except:
            print temp + "checked!"
            tab.append(temp)
            brute(temp, length, charset, tab)



print charset_tab[0]
#for length in range(1, 8):
for charset in charset_tab:
    c = threading.Thread(None, brute, None,('', length_max, charset, tab))
    thread.append(c)
        
for t in thread:
    print "tread "+str(t)
    t.start()

for t in thread:
    print "tread "+str(t)
    t.join()

print tab
