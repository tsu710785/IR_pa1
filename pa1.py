import nltk, re, porter_algorithm
from nltk.corpus import stopwords

#load porter algorithm
p = porter_algorithm.PorterStemmer()

#read file into buffer
f = open('./28.txt', 'rw')
buffer = f.read()
f.close()

stop = stopwords.words('english')

#lowercase and split it by space
words = buffer.lower().split()

f2 = open('result.txt', 'w+')
for idx,val in enumerate(words):
    out = ''
    words[idx] = re.sub('[.,\s]',"", words[idx])
    #print words[idx], len(words[idx])
    if words[idx] not in stop:
       out = p.stem(words[idx], 0,len(words[idx])-1)
       #print out
       f2.write(out+'\n')
f2.close()

