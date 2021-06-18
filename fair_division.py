def result(arr):
    if arr.count(1) %2 != 0:
        return "NO"
    
    arr.sort(reverse= True)  
    x=0
    y=0
    
    for i in arr:
        if x>y:
            y+=i
        else:
            x+=i
        
    if x == y:
        return "YES"
    
    return "NO"       

n = int(input())

for i in range (n):
    m = int(input())
    arr = list(map(int, input().split()))
    x = result(arr)
    print(x)


