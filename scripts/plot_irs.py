import pickle
import matplotlib.pyplot as plt
from parameters import params
from spectrum import Spectrum
from driver import Filter_Job


# import data
with open('btube_ir_data.p', 'rb') as F:
    ir = pickle.load(F)

