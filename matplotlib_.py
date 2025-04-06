from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt
import numpy as np
#Variable define
x = np.array([10,12,14,16,18,20])
y = np.array([11,13,15,16,17,19])

#-------------------------------------------------------------------------------------------------------
# DRAW SIMPLE LINE...
# plt.plot(x,y)
#-------------------------------------------------------------------------------------------------------

# Plotting Without Line
# plt.plot(x,y, 'o')
#-------------------------------------------------------------------------------------------------------

#Line + position descover
# plt.plot(x,y, marker='o')
# plt.plot(x,y, ls=':')
#------------------------------------------------------------------------------------------------------------------------

# Color line
# plt.plot(x,y, color='red')
#-------------------------------------------------------------------------------------------------------
#Maker size
# plt.plot(x,y, marker='o',ms=20)

#Maker color border
# plt.plot(x,y, marker='+', ms=50, color='red')

#Fill color of marker
# plt.plot(x,y, marker='o', ms=50, color='red', mfc='blue')

#Line width
# plt.plot(x,y, marker='o', ms=50, color='red', mfc='black', linewidth='20.5')
#-------------------------------------------------------------------------------------------------------

#Multiple lines
# plt.plot(x)
# plt.plot(y)

#-------------------------------------------------------------------------------------------------------

#Create lable for a Plot
# plt.plot(x,y)
# plt.xlabel('Study Hour')
# plt.ylabel('Exam score')

# Create a title for a plot
# plt.plot(x,y)
# plt.title('Study hour and Exam score')

#Set Font properity for title and lable
# font_1 = {
#     'family': 'serif',
#     'color': 'blue',
#     'size': 15
# }
# font_2 = {
#     'family': 'serif',
#     'color': 'red',
#     'size': 15
# }
# plt.plot(x)
# plt.plot(y)
# plt.title('Study Hour and Exam Score' ,fontdict=font_1)
# plt.xlabel('Study Hour', fontdict=font_2)
# plt.ylabel('Exam Score', fontdict=font_2)

#Position of title
    #loc='left',
    #loc='center',
    #loc='right'
# plt.plot(x,y)
# plt.title('Study Hour and Exam Score', loc='left')
#-------------------------------------------------------------------------------------------------------

# Add grid line to a plot

#Grid in x-axis
# plt.grid(axis='x')

#Grid in y-axis
# plt.grid(axis='y')

#Set properity for grid the grid line
# plt.plot(x,y)
# plt.grid(color='green', linestyle='--', linewidth=0.5)
#-------------------------------------------------------------------------------------------------------

#Display multiple plot/graph in single window(Horizontal)

#plt_1
# plt.subplot(1,2,1)
# plt.plot(x)
# plt.plot(y)
# plt.title('Study Hour')
# The figure has 1 row, 2 column and this plot is the 1st plot.

#plt_2
# plt.subplot(1,1,1)
# plt.plot(x)
# plt.plot(y)
# plt.title('Exam Score')
# plt.suptitle('Exam Score according to Study Houe')
# The figure has 1 row, 2 column and this plot is the 2st plot.

#Display multiple plot/graph in single window(Vertical)
# plt.subplot(2,1,1)
# plt.plot(x,y)
# plt.title('Study Hour')
# The figure has 1 row, 2 column and this plot is the 2st plot(Vertical).

# plt.subplot(2,1,2)
# plt.plot(x,y)
# plt.title('Exam Score')
# plt.suptitle('Exam Score according to Study Houe')
#-------------------------------------------------------------------------------------------------------

#Creating scatter plots...
# plt.scatter(x,y)
# The scatter function plot one dot for each observation. it need array of tje same length. one for value of the x-axis and another for value of the y-axis
#-------------------------------------------------------

#Color of scatter
# plt.scatter(x,y,color='red')
#-------------------------------------------------------------------------------------------------------

#Color map
#Make x,y in same length(E.g x = 6, y = 6 )
# size = np.array([100, 200, 300, 400, 500, 600])  #-----> Bigger sizes
# size = x * 30  #-----> Multiplies each x-value for size
# colors = np.array([10, 20, 30, 40, 50, 60])  # must match length of x/y
# plt.scatter(x, y, c=colors, cmap='viridis', alpha=0.5, s=size)
# plt.colorbar()
#-------------------------------------------------------

# Generate random data
# X = np.random.randint(100, size=(100))
# Y = np.random.randint(100, size=(100))
# color = np.random.randint(100, size=(100))  # for color mapping
# size = 10 * np.random.randint(100, size=(100))  # for marker sizes
# Plot
# plt.scatter(X, Y, c=color, s=size, alpha=1, cmap='nipy_spectral')
# plt.colorbar()
#-------------------------------------------------------------------------------------------------------

#Create bars
# plt.bar(x,y)#---->(VERTICAL)
# plt.barh(x,y)#---->(HORIZONTIAL)
# plt.bar(x,y, width=0.1)
# plt.barh(x, y, height=0.3) 
#-------------------------------------------------------------------------------------------------------

#Histogram
# axix = np.random.randint(10,170,size=250)
# plt.hist(axix)
#-------------------------------------------------------------------------------------------------------

#Create pie chart 
# plt.pie(x)
#-------------------------------------------------------------------------------------------------------

plt.show()