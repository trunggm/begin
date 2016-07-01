# -*- coding: utf-8 -*-

def checkLink(link):
    if link[:4]=="http":
        return 0
    elif link[0]=='/':
        return 1
    else: 
        return 2
    
def checkFile(filename):
    try:
      open(filename, "r")
      return 1
    except IOError:
      return 0


def getchaper(str):
    arr = str.split(' ')
    quyen = 0
    chap = 0
    if str.find('quyển')!=-1:
        quyen = int(arr[1])
        chap = int(arr[3])
    else:
        chap = arr[1]
    return (quyen, chap)
        