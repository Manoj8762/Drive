def spiral_order(matrix):
    result=[]
    top, bottom = 0, len(matrix)-1
    left, right =0, len(matrix[0])-1
    dir=0
    while top<=bottom and left<=right:
        # top left to  top right
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
        # from right top to right bottom
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1
        
        
    
        
        # dir=2 from right bottom to left bottom
        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1
        
        
        # dir =3 from left bottom to left top-
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1
    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Spiral order:", spiral_order(matrix))