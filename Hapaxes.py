# book name here --> 1661-0.txt
import os
import string

def delPunc(text):
    punc = string.punctuation
    for i in text:
        if i in punc:
            text = text.replace(i, "")
    return text

def main():
    os.chdir('/Users/Ken/Desktop')
    filename = input("Enter filename: ")

    file = open(os.getcwd()+'/'+filename,'r')
    text = file.read()
    text = delPunc(text)
    text = text.lower()
    li1 = text.split()
    print(search(li1))

def search(li1):
    dic = {}
    for i in li1:
        if i not in dic:
            dic[i] = 1
        elif i in dic:
            del (dic[i])
    return dic

main()