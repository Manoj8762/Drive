def lower_traingle(matrix):
   
    row=len(matrix)
    column=len(matrix)
    transposed=[[0]*row for _ in range(column)]
    for i in range(0,row):
        for j in range(0,column):
            transposed[j][i]=matrix[i][j]
            print(end="")
        print()
        
            
    print(transposed)
mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(lower_traingle(mat))