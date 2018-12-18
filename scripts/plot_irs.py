import pickle
import matplotlib.pyplot as plt
from parameters import params
from spectrum import Spectrum
from driver import Filter_Job


# import data
with open('btube_ir_data.p', 'rb') as F:
    ir = pickle.load(F)


def plot_sat_act():
    """Plots the saturated activities of the integral responses."""

    for key, val in ir.items():
        if 'l1' in key and 'Cd' not in key:
            spec = val[1][:, 0]
            print(spec)
            plt.semilogy(spec)


plot_sat_act()
