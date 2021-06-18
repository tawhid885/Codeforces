# def result(n,a,b,c,dict={}):
    
#     if n in dict.keys():
#         return dict[n]

#     if n==0:
#         return 0
    
#     if n< 0:
#         return -1

#     dict[n]=1+max(result(n-a,a,b,c,dict),result(n-b,a,b,c,dict),result(n-c,a,b,c,dict))
#     return dict[n]
    
    
    
    

# n=list(map(int, input().split()))
# arr=[]
# arr.append(n[1])
# arr.append(n[2])
# arr.append(n[3])
# arr.sort()
# x = result(n[0], arr)
# x = result(4000,5,5,1)
# print(x)

# if type(x)== "list":
#     print(len(x))

# else:
#     print(x)


# n,a,b,c=map(int,input().split())
# # z=[0]+[-1e9]*5000
# z=[0]*5000
# for i in range(1,n+1):
#     z[i]=max(z[i-a],z[i-b],z[i-c])+1
# print(z[n])


def result(n, arr):
    return n//arr[0]+n%arr[0]//arr[1]+n%arr[1]//arr[2]



arr =list(map(int, input().split()))
n = arr.pop(0)
arr.sort()
x = result(n, arr)
print(x)