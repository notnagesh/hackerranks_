def str_to_lst(str):
    templst=[]
    k=""
    for i in str:
        if i==" ":
            templst.append(int(k))
            k=""
            continue
        else:
            k=k+i
    if(k):
        templst.append(int(k))  
    return templst         
input()
for i in ((str_to_lst(input()))[::-1]):
    print(i,end=" ")
