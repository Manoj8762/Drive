def filter_negative(arr):
    filterd=[]
    for num in arr:
        if num<0:
            continue
        else:
            filterd.append(num)
    length=len(filterd)
    if length%2==0:
        mid_index=length//2
        return filterd[mid_index-1]
    else:
        mid_index=length//2
        return filterd[mid_index]
            
print(filter_negative(list(map(int,input("enter the array of numbers separated by space").split()))))