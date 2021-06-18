def result(n, list):
    res=1
    count =1
    for i in range(0,len(list)-1):
        if count >= res:
            res = count
            

        if list[i] <= list[i+1]:
            count +=1
            res = max(count, res)

 
        else:
           
            count =1
        
    return res



n=int(input())
list = list(map(int, input().split()))

x = result(n, list)
print(x)