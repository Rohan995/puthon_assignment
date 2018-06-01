
wordcount=0
with open('input.txt','r') as f:
    for line in f:
        for word in line.split():
           wordcount[word]+=1

f = open("output.txt","a")
for i in sorted(word):
	f.write(i + ' : ' + str(wordcount[i]) + '\n')