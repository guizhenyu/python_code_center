import numpy as np
import matplotlib.pyplot as plt

def Normalization(x):
    min = min(x)
    max = max(x)
    return [float(i - min)/(max - min) for i in x]

def Normalization1(x):
    min = min(x)
    max = max(x)
    mean = np.mean(x)
    return [ float(i - mean)/(max - min) for i in x]

def Normalization2(x):
    mean = np.mean(x)
    sum = sum([(i-mean)*(i-mean) for i in x]) / len(x)
    return [ (i-sum)/ sum  for i in x]