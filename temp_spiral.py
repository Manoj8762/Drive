def spiral(matrix):
    top,bottom=0,len(matrix)-1
    left,right=0,len(matrix[0])-1
    result=[]
    while top<=bottom and left<=right:
        # top left to top right
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
        
        # top right to top left
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1
        
        # right bottom to left bottom
        if left<=right:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1
        
        # left bottom to left top
        
        if top<bottom:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1
    return result
# example matrix
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print(spiral(matrix))