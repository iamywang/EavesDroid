# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import os
import numpy as np
import matplotlib.pyplot as plt

path = 'data/exp0-figures/OnePlus OnePlus GM1910/'
flist = os.listdir(path)
d_sets = np.zeros([len(flist), 5000, 4], int)
d_sets_scaled = np.zeros([len(flist), 5000, 4], np.double)
d_labels = np.zeros([len(flist)], int)

ab = ['a', 'b', 'c', 'd']

for i in range(len(flist)):
    d_labels[i] = flist[i].split('_')[0]
    for j in range(4):
        d_sets[i, :, j] = np.loadtxt(path + flist[i], delimiter=',', usecols=j)
        d_sets_scaled[i, :, j] = (d_sets[i, :, j] - np.min(d_sets[i, :, j])) / (np.max(d_sets[i, :, j]) - np.min(d_sets[i, :, j]))

plt.rc('font', family='Arial', size=28)
for i in range(2):
    # 4 feature
    plt.ylabel('normalized value')
    plt.xlabel('timestamp (ms)')
    colors = ['tab:blue', 'tab:red', 'tab:green']
    line_styles = ['-', '--']
    markers = ['o', 's', 'D']
    for c in range(2):
        # 4 category
        plt.plot(np.mean(d_sets_scaled[d_labels == (c+1)*4, :, i], axis=0),
                 lw=3, color=colors[c], linestyle=line_styles[c],
                 marker=markers[c], markevery=500)
    plt.legend(['Playing', 'Pausing'], fontsize=20, labelspacing=0.2)
    # plt.title('feature ' + str(i))
    plt.tight_layout()
    plt.ylim(0, 1.49999)
    plt.xticks(np.arange(0, 5001, 2500))
    plt.savefig("../paper/ieee/fig6" + ab[i] + ".pdf", format='pdf')
    plt.close()

plt.rc('font', family='Arial', size=28)
for i in range(2):
    # 4 feature
    plt.ylabel('normalized value')
    plt.xlabel('timestamp (ms)')
    colors = ['tab:blue', 'tab:red', 'tab:green']
    line_styles = ['-', '--']
    for c in range(2):
        # 4 category
        plt.plot(np.mean(d_sets_scaled[d_labels == 4 + c, :, i], axis=0),
                 lw=3, color=colors[c], linestyle=line_styles[c],
                 marker=markers[c], markevery=500)
    plt.legend(['Launch', 'View'], fontsize=20, labelspacing=0.2, loc='upper right')
    # plt.title('feature ' + str(i))
    plt.tight_layout()
    plt.ylim(0, 1.49999)
    plt.xticks(np.arange(0, 5001, 2500))
    plt.savefig("../paper/ieee/fig6" + ab[i+2] + ".pdf", format='pdf')
    plt.close()