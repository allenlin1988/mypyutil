#!/usr/bin/env python

import numpy as np

# Convert a N dimensional numpy array of labels from 0 to C-1 into a MxN matrix
# A element M[i,j]=1 if i is not j's label. M[i,j]=0 otherwise. 

# y: [1xN] numpy array
# num_class: number of classes
def l2v_np(y,num_class):
  M = np.zeros((len(y), num_class))
  M[y,range(num_class)] = 1
  return M

if __name__ == "__main__": 
  print "Running self demo..."
  y = np.array(range(4))
  print "y = \n", y
  M = l2v_np(y,num_class=4)
  print "M = \n", M


