# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import os
import numpy as np
import matplotlib.pyplot as plt

path = 'data/exp1-accuracy_additional_impact/normal/OPPO OPPO PGJM10/'
flist = os.listdir(path)
d_sets = np.zeros([len(flist), 5000, 5], int)
d_sets_scaled = np.zeros([len(flist), 5000, 5], np.double)
d_labels = np.zeros([len(flist)], int)

ab = ['a', 'b', 'c', 'd']

for i in range(len(flist)):
    d_labels[i] = int(flist[i].split('_')[0])
    for j in range(5):
        d_sets[i, :, j] = np.loadtxt(path + flist[i], delimiter=',', usecols=j)
        d_sets_scaled[i, :, j] = (d_sets[i, :, j] - np.min(d_sets[i, :, j])) / (np.max(d_sets[i, :, j]) - np.min(d_sets[i, :, j]))

plt.rc('font', family='Arial', size=28)
y_labels = ["free inodes (number)", "avail memory (Byte)"]
for i in range(2):
    # 4 feature
    plt.ylabel(y_labels[i])
    plt.xlabel('timestamp (ms)')
    colors = ['tab:blue', 'tab:red', 'tab:green']
    line_styles = ['-', '--']
    markers = ['o', 's', 'D']
    for c in range(2):
        # 4 category
        plt.plot(np.mean(d_sets[d_labels == c+1, :, i+3], axis=0), lw=3, color=colors[c],
                    linestyle=line_styles[c], marker=markers[c], markevery=500)

    plt.legend(['View', 'Send'], fontsize=20, labelspacing=0.2)
    # plt.title('feature ' + str(i))
    plt.xticks(np.arange(0, 5001, 2500))
    if i == 1:
        plt.gca().yaxis.set_major_formatter(lambda x, pos: str(int(x/1e6)) + 'M')
        plt.ylim(3e8, 4.5e8)
        plt.gca().tick_params(axis='y')
    if i == 0:
        plt.gca().yaxis.set_major_formatter(lambda x, pos: str(int(x - 1.27911e7)))
        plt.ylim(15 + 1.27911e7, 45 + 1.27911e7)
        plt.text(0.00, 1.02, '+12.7911M', transform=plt.gca().transAxes, ha='left')
        plt.gca().tick_params(axis='y')
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig3" + ab[i] + ".pdf", format='pdf')
    plt.close()

d_sets_0 = np.zeros([int(len(flist)/2), 5000, 5], int)
d_sets_1 = np.zeros([int(len(flist)/2), 5000, 5], int)
d_labels_0 = np.zeros([int(len(flist)/2)], int)
d_labels_1 = np.zeros([int(len(flist)/2)], int)

for i in range(int(len(flist)/2)):
    d_labels_0[i] = d_labels[i]
    d_labels_1[i] = d_labels[i+int(len(flist)/2)]
    for j in range(5):
        d_sets_0[i, :, j] = d_sets[i, :, j]
        d_sets_1[i, :, j] = d_sets[i+int(len(flist)/2), :, j]

def fig4c():
    plt.rc('font', family='Arial', size=28)
    plt.ylabel(y_labels[0])
    plt.xlabel('timestamp (ms)')
    colors = ['tab:blue', 'tab:red', 'tab:green']
    line_styles = ['-', '--']
    markers = ['o', 's', 'D']
    plt.plot(np.mean(d_sets_0[d_labels_0 == 1, :, 3], axis=0), lw=3, color=colors[0],
                linestyle=line_styles[0], marker=markers[0], markevery=500)
    plt.plot(np.mean(d_sets_1[d_labels_1 == 1, :, 3], axis=0), lw=3, color=colors[1],
                linestyle=line_styles[1], marker=markers[1], markevery=500)
    plt.legend(['View (1)', 'View (2)'], fontsize=20, labelspacing=0.2)
    plt.xticks(np.arange(0, 5001, 2500))
    plt.gca().yaxis.set_major_formatter(lambda x, pos: str(int(x - 1.27911e7)))
    plt.ylim(15 + 1.27911e7, 45 + 1.27911e7)
    plt.text(0.00, 1.02, '+12.7911M', transform=plt.gca().transAxes, ha='left')
    plt.gca().tick_params(axis='y')
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig3c.pdf", format='pdf')
    plt.close()

def fig4d():
    plt.rc('font', family='Arial', size=28)
    plt.ylabel(y_labels[1])
    plt.xlabel('timestamp (ms)')
    colors = ['tab:blue', 'tab:red', 'tab:green']
    line_styles = ['-', '--']
    markers = ['o', 's', 'D']
    plt.plot(np.mean(d_sets_0[d_labels_0 == 1, :, 4], axis=0), lw=3, color=colors[0],
                linestyle=line_styles[0], marker=markers[0], markevery=500)
    plt.plot(np.mean(d_sets_1[d_labels_1 == 1, :, 4], axis=0), lw=3, color=colors[1],
                linestyle=line_styles[1], marker=markers[1], markevery=500)
    plt.legend(['View (1)', 'View (2)'], fontsize=20, labelspacing=0.2)
    plt.xticks(np.arange(0, 5001, 2500))
    plt.gca().yaxis.set_major_formatter(lambda x, pos: str(int(x/1e6)) + 'M')
    plt.ylim(3e8, 4.5e8)
    plt.gca().tick_params(axis='y')
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig3d.pdf", format='pdf')
    plt.close()

fig4c()
fig4d()
