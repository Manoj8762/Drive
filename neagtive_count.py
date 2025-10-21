def negative_count(arr):
    total_sum=0
    for num in arr:
        if num<0:
            total_sum+=num
        
    if total_sum<0:
        return total_sum
    else:
        return 0
       
        
            
    
arr=list(map(int,input(" enter the 4 numbers separated by space ").split()))
print(negative_count(arr))