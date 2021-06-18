# def result(n, dict={}):

#     if n in dict.keys():
#         # print("dict is ",dict[n])
#         return dict[n]

#     if n == 0:
#         return 0
    
#     if n<0:
#         return 100000000000
    
#     dict[n]=min(result(n-100,dict),result(n-20,dict),result(n-10,dict),result(n-5,dict),result(n-1,dict))+1
#     return dict[n]

# n =int(input())
# # 1 5 10 20 100
# x = result(n)
# print(x)

n = int(input())
x = n//100 + n%100//20 + n%20//10 + n%10//5 + n%5//1
print(x)