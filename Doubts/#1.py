import string
    handle = open('abc.txt')
    counts = dict()
    for line in handle:
        line = line.translate(string.punctuation)
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
                
        list1 = list()
        for key,val in counts.items():
            list1.append((val,key))
            
        list1.sort(reverse=True)
        
        for key,val in list1[:10]:
            print (key,val)

## The above code will print frequrntly used words, line by line. How can i tweak that so it prints all the words of the file 
## in descending order of frequency

## I have tried it here

def tupules():
    #import string
    handle = open('abc.txt')
    file = handle.read()
    wordcount = file.split()    
    counts = dict()
    for word in wordcount:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    
        list1 = list()
        for key,val in counts.items():
            list1.append((val,key))
            
        list1.sort(reverse=True)
        
        for key,val in list1[:10]:
            print(key,val)
