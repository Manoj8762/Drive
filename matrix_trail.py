def mat_traverssal(matrix):
    sum=0
    row=len(matrix)
    column=len(matrix[0])
    for i in range(0,row):
        for j in range(0,column):
            print(matrix[i][j],end="")
        print()
           
mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(mat_traverssal(mat))
     