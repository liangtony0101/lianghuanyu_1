import math
import pyinputplus as pyip

# 1個參數,有傳出值
def circule_area(r):
    a = r ** 2 * math.pi
    return a



radius = pyip.inputFloat("請輸入半徑:")
print(radius)
area = circule_area(radius)
print(f"半徑{radius},圓面積是{area}")