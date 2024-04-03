
data = [1,2,3]
class item():
    def __init__(self,a,b,c):
        a=a
        b=b
        c=c
        print(a,b,c)

test = item(*data)