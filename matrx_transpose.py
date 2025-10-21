def trans(mat):
    row=len(mat)
    column=len(mat[0])
    transpose=[[0]*row for _ in range(column)]
    for i in range(row):
        for j in range(column):
            transpose[j][i]=mat[i][j]
        print(end=" ")
    return transpose


matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(trans(matrix))