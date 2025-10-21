def second(arr):
    fir=sec=arr[0]
    
    for num in range(1,len(arr)):
        
        if arr[num] > fir:
            sec=fir
            fir=arr[num]
        elif arr[num]< fir and sec<arr[num]:
            sec=arr[num]
            
    return fir,sec
print(second([7,8,89,4,2]))

