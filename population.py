import numpy as np
import math as ma
import random

def population():    
    initial_pop = 0
    return initial_pop

def calculate_distance(pt_1, pt_2):
    return ma.sqrt(ma.pow((pt_1[0]-pt_2[0]), 2)+ma.pow((pt_1[1]-pt_2[1]), 2))