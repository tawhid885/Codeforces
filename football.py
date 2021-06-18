def result(n):
    list=[n[0]]
  

    for i in range(1,len(n)):
        if list[-1]==n[i]:
            list.append(n[i])
            if len(list)==7:
                return "YES"
        else:
            list.clear()
            list.append(n[i])
    return "NO"
   

n = input()

x= result(n)
print(x)