
def result(n, arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i][0] < n:
            n +=arr[i][1]
        else:
            return "NO"
        
    return "YES"
    
        
    



sn= list(map(int, input().split()))
arr=[]

for i in range(sn[1]):
    inp = list(map(int, input().split()))
    arr.append(inp)

x = result(sn[0], arr)
print(x)