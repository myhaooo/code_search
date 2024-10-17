# beg=243647
# str="http://47.92.197.167:5283/submission/"+str(beg)
# print(str)

def search(beg,end):
    for i in range(beg,end+1):
        string="http://47.92.197.167:5283/submission/"+str(i)
        ask(string)

def ask(str):
    print(str)

search(243647,300000)