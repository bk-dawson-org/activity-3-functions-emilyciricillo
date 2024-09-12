import math

def getCylinderVolume(radius, height) :
    volume = math.pi * radius**2 * height
    return volume 

x = getCylinderVolume(10,12)
y = getCylinderVolume(2,6)

print(x)
print(y)
print(round(x,4))
print(round(y,4))
print(int(x))

def getNumberofSlices(radius, height, volumeofslice) :
    volume = getCylinderVolume(radius, height)
    NumberofSlices = volume/volumeofslice
    return int(NumberofSlices)

NumberofSlices1 = getNumberofSlices(10, 10, 100)

print(NumberofSlices1)
