def mat_traverssal(matrix):
    row=len(matrix)
    column=len(matrix[0])
    for i in range(0,row):
        for j in range(0,column):
            if i<=j:
                print(matrix[i][j], end="")
                
            
            else:
                
                print("*", end="")
        print()




mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(mat_traverssal(mat))