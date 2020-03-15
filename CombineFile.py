#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import re
import os
import converter
from converter import uni512zg1,zg12uni51,test

def SaveData(filename,data):
    user_post = data
    fname = filename
    path = "D:\\My_thesis\\file_collection\\dataset\\"
    #D:\\My_thesis\\dataset\\Working_Process\\links\\
    print("fname to look up"+fname)
    data = {}
    try:
        s = len(user_post)
        fh = open(path+fname+".txt","a+",encoding = 'utf8')
        for i in range(s):            
            post = ''
            raw_data = user_post[i]['message']
            if raw_data != "":
                post = clear_text(raw_data)                
                fh.write(post)
            raw_comments = user_post[i]['comments']['data']
            for j in range(len(raw_comments)-1):                
                if raw_comments[j]['message'] != '' :
                    text = clear_text(raw_comments[j]['message'])
                    fh.write(text)  
        return "Save Text File sucessfully!!"           

    except KeyError as error :
        return error

def SaveDataFromJSONFile():
    
    path = "D:\\My_thesis\\file_collection\\dataset\\"
    fname = input("input file name: ")
    print("fname to look up"+fname)
    data = {}
    with open(path+fname+".json", encoding = 'utf8') as f :
        user_post = json.load(f)
    try:
        s = len(user_post)
        fh = open(path+"sample23.txt","a+",encoding = 'utf8')
        for i in range(s):            
            post = ''
            raw_data = user_post[i]['message']
            if raw_data is not None:
                post = clear_text(raw_data)
                fh.write(post+"\n")
            raw_comments = user_post[i]['comments']['data']
            
##            raw_comments = filter(lambda x: x.strip(), raw_comments)
            for j in range(len(raw_comments)-1):
                
                if raw_comments[j]['message'] is not None:
                    text = clear_text(raw_comments[j]['message'])
                    fh.write(text+"\n")
        deleteEmptyLine("sample4")
        return "Save Text File sucessfully!!"           
    
    except KeyError as error :
        return error
        
def deleteEmptyLine(fname):
    path = "D:\\My_thesis\\file_collection\\dataset\\"
    with open(path+fname+".txt", 'r+', encoding = 'utf8') as filehandle:
        lines = filehandle.readlines()
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines) 

def removeUnnecessaryWord():
    path = "D:\\My_thesis\\file_collection\\dataset\\"
    fname = input("input file name: ")    
    with open(path+fname+".txt", 'r+', encoding = 'utf8') as filehandle:
        lines = filehandle.readlines()
        lines = filter(lambda x: x.strip(), lines)
        
        for rgx_match in lines:
            for w in rgx_match:
                if re.match(r'[#«“=”.•�❤;]+', w,re.I):
                    rgx_match = re.sub(r'[#«“=”.•�❤;။]'," ",rgx_match)
                if re.match(r'[년 서울 삼풍]+', w,re.I):
                    rgx_match = re.sub(r'[년 서울 삼풍]'," ",rgx_match)
                    
                Žăàÿ
            filehandle.writelines(rgx_match)
        filehandle.close()

def removeUnnecessaryWord(txtStr):
    rgx_match = txtStr
    for w in rgx_match:
        if re.match(r'[#«“=”.•�❤;]+', w,re.I):
            rgx_match = re.sub(r'[#«“=”‘‘.’’•�❤;။]'," ",rgx_match)
        if re.match(r'[년 서울 삼풍]+', w,re.I):
            rgx_match = re.sub(r'[년 서울 삼풍]'," ",rgx_match)
    return rgx_match

def clear_text(text_string):
    text = ''
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    for w in text_string:
        if not re.match(r'[A-Za-z0-9\.]+', w,re.I):
            if not re.match(r'[$-/:?{-~!"^_`\[\]]',w,re.I):
                w = re.sub(r"(?m)^[^\S\s\W\w\n]+","",w)
                text = text+w;
    text = text.translate(non_bmp_map)
    text = removeUnnecessaryWord(text)
    text = zg12uni51(text)
    return text
def remove_emptyline():
    lines = []
    path = "D:\\My_thesis\\file_collection\\dataset\\sample23.txt"   
    with open(path, 'r+', encoding = 'utf8') as filehandle:
        lines = filehandle.readlines()
    with open("../dataset/sample24.txt", 'w+', encoding = 'utf8') as filehandle2:
        
        
        for rgx_match in lines:
##            print(len(rgx_match))
            
            if len(rgx_match)>1:
                if re.match(r'^\s*$',rgx_match):
                    continue
                else:
                    for w in rgx_match:
                        if re.match(r'\u200b', w,re.I):
                            rgx_match = re.sub(r'\u200b'," ",rgx_match)
##                    rgx_match = rgx_match.strip(u'\u200b')
##                    temp = re.sub(r'\u200b','',rgx_match)
                    #white space
                    temp = re.sub(r'\s+', ' ', rgx_match)
                    filehandle2.writelines(temp+"\n")
##                
##                if re.match(r'^\s*$',rgx_match):
##                    continue
##                else:
##                    rgx_match = rgx_match.strip(u'\u200b')
##                    temp = re.sub(r'\u200b','',rgx_match)
##                    #white space
##                    temp = re.sub(r'\s+', '', rgx_match)
##                    filehandle2.writelines(temp+"\n")
            
##            if re.match(r'^\s*S',rgx_match):
##                continue
##            else:
##                filehandle2.writelines(rgx_match)                
                
            
        filehandle2.close()
        filehandle.close()

    

