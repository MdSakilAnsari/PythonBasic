#from balance import avlbal
bal=1000
def cbal():
    global bal
    print("Current balance is =",bal)
def dep(d):
    global bal
    bal=bal+d
    return bal
def wth(wa):
    global bal
    if(bal>=wa+1000):
        bal=bal-wa
        return bal
    else:
        return "Insufficient balance...!!!"

