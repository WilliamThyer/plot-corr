from plot_corr import plot_corr
import numpy as np

# Generating fake data
x = np.arange(0,100,4)
y = np.arange(0,100,4)**2

# Calling function
plot_corr(x,y)

# Generating fake null data 
x = np.arange(0,100,2)
y = np.random.permutation(np.arange(0,10,.2))

# Calling function with custom title and variable names
plot_corr(x,y,plot_title='No relationship between feathers and WM', x_variable_name='# of feathers', y_variable_name='Zebra finch WM capacity')