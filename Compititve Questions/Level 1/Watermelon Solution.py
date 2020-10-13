def watermelonweight(weight):
    return "Yes" if (weight%2==0) else "NO"


print(watermelonweight(6))       #should return "YES"
print(watermelonweight(62))       #should return "YES"
print(watermelonweight(1))     #should return "NO"
print(watermelonweight(7))       #should return "NO"
print(watermelonweight(23))       #should return "NO"
print(watermelonweight(43))      #should return "NO"
print(watermelonweight(24))       #should return "YES"
print(watermelonweight(11))       #should return "NO"
print(watermelonweight(10))       #should return "YES"