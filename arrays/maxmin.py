def getMinMax(arr):
    arr.sort()
    minmax = {"min":arr[0],"max":arr[-1]}
    return minmax

arr=[100,23,66,72]
minmax=getMinMax(arr)
print("Minimum element is", minmax["min"])
print("Minimum element is", minmax["max"])


