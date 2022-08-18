# import manimlib
import cmath
import sys

def getchar() : return sys.stdin.read()

class E:
    to : int
    w : int
    next : int
    def __init__(self, to, w, next) -> None:
        self.to = to
        self.w = w
        self.next = next

maxn = int(1e5 + 8)
edge : list = [] * maxn 
cnt = 0
head : list = [] * maxn

def addEdge(u, v, w) :
    edge[cnt] = E(v, w, head[u])
    head[u] = cnt
    cnt += 1

def read() :
    f = 1
    c = 0
    c = getchar()
    x = 0
    while (c < '0' | c > '9') :
        if c == '-' : f = -1
        c = getchar()
    while (c >= '0' & c <= '9') :
        x = x * 10 + c - '0'
        c = getchar()
    return x


def scanf(format, *args):
    i = 0
    while 1:
        if format[i] == 0 :
            return
        if (format[i] == "%" & format[i + 1] == 'd') :
            return 
    sys.stdin.read()
    

x = 0
x = read()
print(x)
