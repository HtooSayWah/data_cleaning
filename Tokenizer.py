import os
import re
import codecs
import sys
def TestTokenize():
    sentences = []
    with open("D:\\My_thesis\\file_collection\\dataset\\sample24.txt", encoding = 'utf8') as filehandle:
        sentences = filehandle.readlines()
    
    for sentence in sentences:
        wordSegment(sentence)

def wordSegment(text):
    data = segment(text)
    
    validWord = []
    temp1 = ""
    processWord ={}
    pos = None
    
    for w in range (len(data)-1):
        if pos is None:
            #print('I am pos None')
            pos=0
            if pos == len(data)-4:
##                processWord = MatchTextString(data[w])
                processWord = MatchText(data[w])
                pos = w
                #Match String for unigram
                if processWord['flag'] == True:
                    temp2 = processWord['val']
                    processWord = MatchText(data[w]+data[w+1])
                    #print(temp2)

                    #Match String for bigram
                    if processWord['flag'] == True:
                        pos = w+1
                        temp2 = processWord['val']
                        processWord = MatchText(data[w]+data[w+1]+data[w+2])
                        #print(temp2)
                        
                        #Match String for trigram
                        if processWord['flag'] == True:
                            pos = w+2
                            temp1 = processWord['val']                       

                        else: temp1 = temp2
                            
                        
                    else: temp1 = temp2
                else: temp1 = data[w]

            elif pos == len(data)-3:
                processWord = MatchText(data[w])
                pos = w
                #Match String for unigram
                if processWord['flag'] == True:
                    temp2 = processWord['val']
                    processWord = MatchText(data[w]+data[w+1])                   

                    #Match String for bigram
                    if processWord['flag'] == True:
                        pos = w+1
                        temp1 = processWord['val']
                        
                    else: temp1 = temp2
                else: temp1 = data[w]
                
            elif pos == len(data)-2:
                processWord = MatchText(data[w])
                pos = w
                #Match String for unigram
                if processWord['flag'] == True:                
                    temp1 = processWord['val']                    
                    
                else: temp1 = data[w]

            else:

                processWord = MatchText(data[w])
                pos = w
                #Match String for unigram
                if processWord['flag'] == True:
                    temp2 = processWord['val']
                    processWord = MatchText(data[w]+data[w+1])
                    #print(temp2)

                    #Match String for bigram
                    if processWord['flag'] == True:
                        pos = w+1
                        temp2 = processWord['val']
                        processWord = MatchText(data[w]+data[w+1]+data[w+2])
                        #print(data[w]+data[w+1]+data[w+2])

                        #Match String for trigram
                        if processWord['flag'] == True:
                            pos = w+2
                            temp2 = processWord['val']
                            processWord = MatchText(data[w]+data[w+1]+data[w+2]+data[w+3])
                            #print(temp2)

                            #Match String for 4gram
                            if processWord['flag'] == True:
                                pos = w+3
                                temp1 = processWord['val']                           

                            else:temp1 = temp2                    

                        else: temp1 = temp2
                        
                    else: temp1 = temp2
                else: temp1 = data[w]
            validWord.extend([temp1])
        else:
            #print('I am pos Something')
            if w < pos:
##                pos = pos - 1
                pass
            elif w== pos:
##                pos = pos - 1
                pass
                
            else:
                pos = w
                if pos == len(data)-4:
                    processWord = MatchText(data[pos])
                    orgVal = pos
                    #Match String for unigram
                    if processWord['flag'] == True:
                        temp2 = processWord['val']
                        processWord = MatchText(data[pos]+data[pos+1])
                        #print(temp2)
                        

                        #Match String for bigram
                        if processWord['flag'] == True:
                            pos = pos+1
                            temp2 = processWord['val']
                            processWord = MatchText(data[orgVal]+data[orgVal+1]+data[orgVal+2])
                            #print(temp2)

                            #Match String for trigram
                            if processWord['flag'] == True:
                                pos = pos+1
                                temp1 = processWord['val']                       

                            else: temp1 = temp2
                            
                        else: temp1 = temp2
                    else: temp1 = data[pos]

                elif pos == len(data)-3:
                    processWord = MatchText(data[pos])
                    #Match String for unigram
                    if processWord['flag'] == True:
                        temp2 = processWord['val']
                        processWord = MatchText(data[pos]+data[pos+1])
                        

                        #Match String for bigram
                        if processWord['flag'] == True:
                            pos = pos+1
                            temp1 = processWord['val']
                            
                        else: temp1 = temp2
                    else: temp1 = data[pos]
                    
                elif pos == len(data)-2:
                    processWord = MatchText(data[pos])
                    #Match String for unigram
                    if processWord['flag'] == True:                
                        temp1 = processWord['val']                    
                        
                    else: temp1 = data[pos]

                else:

                    processWord = MatchText(data[pos])
                    orgVal = pos
                    #Match String for unigram
                    if processWord['flag'] == True:
                        temp2 = processWord['val']
                        processWord = MatchText(data[orgVal]+data[orgVal+1])
                        

                        #Match String for bigram
                        if processWord['flag'] == True:
                            
                            pos = pos+1
                            temp2 = processWord['val']
                            processWord = MatchText(data[orgVal]+data[orgVal+1]+data[orgVal+2])
                            #print(temp2)

                            #Match String for trigram
                            if processWord['flag'] == True:
                                pos = pos+1
                                temp2 = processWord['val']
                                processWord = MatchText(data[orgVal]+data[orgVal+1]+data[orgVal+2]+data[orgVal+3])
                                #print(temp2)

                                #Match String for 4gram
                                if processWord['flag'] == True:
                                    pos = pos+1
                                    temp1 = processWord['val']                           

                                else:temp1 = temp2                    

                            else: temp1 = temp2
                            
                        else: temp1 = temp2
                    else: temp1 = data[pos]
                validWord.extend([temp1])
                    
                 
    testRemovalList = removestopwords(validWord)  
    print(testRemovalList)
            
def MatchText(text):
    
    wordVal = {'flag':False, 'val':''}
    #print(text)
    templist=[]
    with open("D:\\My_thesis\\file_collection\\dataset\\dictlist.txt", encoding = 'utf8') as filehandle:
        wlist = filehandle.readlines()

    with open("D:\\My_thesis\\file_collection\\dataset\\stop_words.txt", encoding = 'utf8') as filehandle1:
        wlist1 = filehandle1.readlines()
        wlist.append(wlist1)

##        templist = list(map(lambda x:x.strip(),wlist))

        for w in range(len(wlist1)-1):
            temp = wlist1[w]
            templist.append(temp.rstrip())
            
        if text in templist:
            wordVal['flag'] = True
            wordVal['val'] = text   
            
    return wordVal

                
def segment(text):
    
    text = re.sub(r'(?:(?<!္)([က-ဪဿ၊-၏]|[၀-၉]+|[^က-၏]+)(?![ှျ]?[့္်]))',r's\1',text).strip('s').split('s')
    temp = []
    for t in text:
        temp.append(t)
    
    
    return temp

def removestopwords(validWord):
    vWord = validWord
    returnList = []
    wlist = []
    with open("D:\\My_thesis\\file_collection\\dataset\\stop_words.txt", encoding = 'utf8') as filehandle1:
        wlist1 = filehandle1.readlines()
        wlist.append(wlist1)

        for w in range(len(wlist1)-1):
            temp = wlist1[w]
            wlist.append(temp.rstrip())
    
    for v in vWord:
        if any(v in s for s in wlist):
            continue
        else:
            returnList.append(v)
    return returnList    


