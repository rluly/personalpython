import time

#Make sure to have your desired txt file is saved in the same directory as this
#python file. Your results will be printed to the command line and written to
#a new file called wordcount.txt

def addToDictionary(l1,d1):
    prev = None
    for ii in l1:
        if ii==prev:
            d1[ii] += 1
        else:
            d1[ii] = 1
        prev = ii

def printDictionary(d1):
    f = open("wordcount.txt","a")
    for ii in sorted(d1,key=d1.get,reverse=True):
        s1 = "\n" + ii + " " + str(d1[ii])
        print(s1)
        f.write(s1)
    f.close()

start = time.time()

#Replace the *** with your desired file
f = open("***")
book = f.read().split()
f.close()

book.sort()
wordcount = {}

f = open("wordcount.txt","w")
f.write("Word count for textfile: ")
f.close()

addToDictionary(book,wordcount)
printDictionary(wordcount)
end = time.time()
print("Your total time is: ", str(end-start))
