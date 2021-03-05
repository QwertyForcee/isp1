import sys
import time

def spam(fullname,spamername,count):
    try:
    	f = open(fullname, "a")
    except IOError:
    	f = open(fullname, "w")
    	f.write("created: "+str(time.time)+"\n")
    finally:
    	for m in range(int(count)):
        	f.write(spamername + "-" + str(m)+"\n")
        	time.sleep(1)#why???
    	f.close()
    	print(fullname)

spam(sys.argv[2],sys.argv[1],sys.argv[3])
