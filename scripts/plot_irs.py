import numpy as np
import pickle
import matplotlib.pyplot as plt
from parameters import params
from spectrum import Spectrum
from driver import Filter_Job


# import data
with open('btube_ir_data.p', 'rb') as F:
    ir = pickle.load(F)


def plot_saturated_activities(keys, params, savename):
    """Plots the saturated activities of the integral responses."""

    # grab the lengths from the parameters
    lengths = params['lengths']

    # initialize arrays for activity and error
    act = np.empty(len(lengths))
    err = np.empty(len(lengths))

    # loop through activities
    for i, key in enumerate(keys):
        act[i] = ir[key][2][0]
        err[i] = ir[key][2][1]

    # normalize data to flux at 1kW
    act *= 2.949E+05 * (1000 / 250)

    # convert from Bq to uCi
    act *= (1 / 3.7E4)

    # change err from relative to absolute
    err = err * act

    # set up plotting environment
    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Length $cm$')
    ax.set_ylabel('Saturated Activity $\mu Ci$')
    ax.set_yscale('log')

    # plot values
    ax.plot(lengths, act, ls='None', marker='o', ms=4, label=keys[0])
    ax.errorbar(lengths, act, err, ls='None')

    # add legend
    ax.legend()

    # save and then clear figure
    fig.savefig('../img/' + savename + '.png', dpi=300)

    return


keys0 = []
keys1 = []
keys2 = []
keys3 = []
keys4 = []
keys5 = []
for key in ir.keys():
    if 'In' in key and 'Cd' not in key:
        keys0.append(key)
    if 'In' in key and 'Cd' in key:
        keys1.append(key)
    if 'Au' in key and 'Cd' not in key:
        keys2.append(key)
    if 'Au' in key and 'Cd' in key:
        keys3.append(key)
    if 'Mo' in key and 'Cd' not in key:
        keys4.append(key)
    if 'Mo' in key and 'Cd' in key:
        keys5.append(key)


plot_saturated_activities(keys0, params, 'In')
plot_saturated_activities(keys1, params, 'InCd')
plot_saturated_activities(keys2, params, 'Au')
plot_saturated_activities(keys3, params, 'AuCd')
plot_saturated_activities(keys4, params, 'Mo')
plot_saturated_activities(keys5, params, 'MoCd')
