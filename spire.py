def mat_spiral(matrix):
    top,bottom=0,len(matrix)-1
    left,right=0,len(matrix[0])-1
    res=[]
    
    while top<=bottom and left<=right:
        
        #left to right
        for num in range(left,right+1):
            res.append(matrix[top][num])
        top+=1
        #top to bottom
        for num in range(top,bottom+1):
            res.append(matrix[num][right])
        right-=1
        # right to left
        if left<=right:
            for num in range(right,left-1,-1):
                res.append(matrix[bottom][num])
            bottom-=1
            
        if top<=bottom:
            for num in range(bottom,top-1,-1):
                res.append(matrix[num][left])
            left+=1
    
    return res
mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]
print(mat_spiral(mat))
            