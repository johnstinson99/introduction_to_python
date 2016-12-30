import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

face_array = scipy.misc.face(gray=True)

print(face_array)
print(face_array.shape)

# plt.imshow(face_array)
# plt.show()

# use a colour map to display in gray
def display(an_array):
    plt.imshow(an_array, cmap=plt.cm.gray)
    plt.show()

crop_face = face_array[100:-100,100:-100]
# display(crop_face)

a = np.ones([768, 1024]) * 255
# print(a)
# display(a)
b = np.ones([768, 1024])*100
print(b)
# display(b)

max_y, max_x = face_array.shape
y, x = np.ogrid[0:max_y, 0:max_x] # x and y indices of pixels
print('y = ', y)
print('x = ', x)
print(y.shape, x.shape)

x_array = np.arange(0, 1024)
# y_array = np.arange(0, 768).transpose()  # doesn't work - have to cast to matrix first.
y_array = np.arange(0, 768)[:, np.newaxis]  # this works.  : selects all rows.
print(x_array)
print(y_array)
# ((768, 1), (1, 1024))
centerx, centery = (660, 300)  # center of the image
mask = ((y_array - centery)**2 + (x_array - centerx)**2) > 230**2  # circle
# print(mask)

# mask formula must contain both x and y arrays (this makes it 2 dimensional)
# and it must return a boolean value
x_array = np.arange(0,100)
y_array = np.arange(0,100)[:, np.newaxis]
mask = y_array == x_array ** 2
# display(mask)

x_array = np.arange(-10, 10)
y_array = np.arange(100,0, -1)[:, np.newaxis]
mask = y_array == x_array ** 2

x_array = np.arange(-100, 100)
y_array = np.arange(100,0, -1)[:, np.newaxis]
mask = y_array >= (x_array/10) ** 2

x_array = np.arange(0, 200)
y_array = np.arange(100, 0, -1)[:, np.newaxis]
mask = y_array >= ((x_array-100)/10) ** 2

# display(mask)

# # simple circle
# x_array = np.arange(-10,10)
# y_array = np.arange(-10,10)[:, np.newaxis]
# mask = ((y_array**2 + x_array**2 > 5**2))

x_array = np.arange(0, 1024)
y_array = np.arange(0, 768)[:, np.newaxis]  # this works.  : selects all rows.
mask = y_array > x_array

x_array = np.arange(0, 1024)
y_array = np.arange(0, 768)[:, np.newaxis]  # this works.  : selects all rows.
centerx, centery = (660, 300)  # center of the image
mask = (((y_array - centery)*2)**2 + (x_array - centerx)**2) > 230**2  # circle

face_array[mask] = 0
display(face_array)
