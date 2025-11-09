def min_max_dif(a1):
    
    for i in range(len(a1) - 1):
        for j in range(i + 1, len(a1)):
            if a1[i] > a1[j]:
                a1[i], a1[j] = a1[j], a1[i]
    
    
    max_diff = a1[-1] - a1[0]
    
    min_diff=float('inf')
    for i in range(len(a1)-1):
        diff=a1[i+1]-a1[i]
        if diff<min_diff:
            min_diff=diff
   
   
    

    return min_diff, max_diff
    
    return min_diff, max_diff


# Example test
print(min_max_dif([7, 8, 9, 5, 6, 21, 3, 8, 2, 3, 1]))
