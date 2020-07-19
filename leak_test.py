# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:28:15 2020

@author: jmatt
"""


import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y = x


for i in range(3000):
    
    if i%50 == 0:
        print("Iteration: {}".format(i))
    #Set the figure size in inches
    fig_size=(3,3)
    
    
    fig = plt.figure(figsize=fig_size)
    
    plt.plot(x, y)
    
    fig.savefig('test.png',dpi=100)
    
    plt.close(fig)


