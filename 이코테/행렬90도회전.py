
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]


def rotate_90degree(a):
    n=len(a)
    new=[[0]*n for i in range(n)]
    for i in range(len(a)):
        for j in range(len(a[0])):
            # (x,y)  -->  (y, n-x-1)
            new[j][n-i-1]=a[i][j]
    
    return new

print(rotate_90degree(a))