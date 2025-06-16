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
def calculate_sum(lst,r,c):
    if((r+2)<6 and (c+2)<6):
        summed_value=lst[r][c]+lst[r][c+1]+lst[r][c+2]+lst[r+1][c+1]+lst[r+2][c]+lst[r+2][c+1]+lst[r+2][c+2]
    else:
        return -9999
    return summed_value
lst=[]
for i in range(0,6):
    lst.append(str_to_lst(input()))
summed_list=[]
for r in range(0,6):
    for c in range(0,6):
        summed_list.append(calculate_sum(lst,r,c))
max_value=-99999
for i in summed_list:
    max_value=max(i,max_value)
print(max_value)
