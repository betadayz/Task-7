import math 
  
def variance(a, n): 
   
    sum = 0
    for i in range(0 ,n): 
        sum += a[i] 
    mean = sum /n 
   
    sqDiff = 0
    for i in range(0 ,n): 
        sqDiff += ((a[i] - mean)  
                * (a[i] - mean)) 
    return sqDiff / n 
  
  
def standardDeviation(arr, n): 
  
    return math.sqrt(variance(arr, n)) 
  
arr = [600, 470, 170, 430, 300] 
n = len(arr) 
print("Variance: ", int(variance(arr, n))) 
print("Standard Deviation: ", 
      round(standardDeviation(arr, n), 3)) 