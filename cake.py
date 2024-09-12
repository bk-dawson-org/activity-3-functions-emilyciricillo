import math

def getCylinderVolume(radius, height) :
    '''
    This function calculates the volume of a cylinder
    param radius: This is the radius of the cylinder
    param height: This is the height of the cylinder
    return : The function returns the volume of the cylinder
    '''
    volume = math.pi * radius**2 * height
    return volume 

# Calculate the volume of a cylinder wiyj thr valur 10 and 12
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

# Calculate the number of slices
NumberofSlices1 = getNumberofSlices(10, 10, 100)

print(NumberofSlices1)
