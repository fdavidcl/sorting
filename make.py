##
# Sorting algorithms visualized.
#
# This code uses python2, pylab and ffmpeg. You may need to install them.
#
# The idea was taken from "The Glowing Python":
#    http://glowingpython.blogspot.com.es/2013/02/selection-sort-animated.html
##

# make.py

import sorting
import bubbleSort

datos = sorting.genData()
bubbleSort.optBubble(datos)
