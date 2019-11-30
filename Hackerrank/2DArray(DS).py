def hourglassSum(arr):
    maxi = -63
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            middle = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])
            tot = top+middle+bottom
            if tot > maxi:
                maxi = tot
    return(maxi)