def str_to_lst(str):
    k=""
    templst=[]
    for i in str:
        if i==" ":
            templst.append(int(k))
            k=""
            continue
        else:
            k=k+i
    if k:
        templst.append(int(k))
    return templst
meta_data=str_to_lst(input())
lst=str_to_lst(input())
if(meta_data[0]<meta_data[1]):
    meta_data[1]=meta_data[0]%meta_data[1]
def left_shift(lst,d):
    lst=lst[d:]+lst[:d]
    return lst
lst=left_shift(lst,meta_data[1])
for i in lst:
    print(i,end=" ")
