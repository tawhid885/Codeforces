
def result(n, m):
    if n<m:
        return n

    res =0
    
    while n > 0 and n>=m:
        if n>=m:
            res +=m
            n= (n-m)+1
    
    return res+n


n=list(map(int, input().split()))

x= result(n[0], n[1])
print(x)