# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

file1 = 'data/exp0-figures/OPPO OPPO PGJM10/0_280.txt'
file2 = 'data/exp0-figures/OPPO OPPO PGJM10/0_224.txt'
file3 = 'data/exp0-figures/OPPO OPPO PGJM10/0_136.txt'

# norm
d_sets = np.zeros([4, 5000, 4], np.double)
d_sets_scaled = np.zeros([4, 5000, 4], np.double)
colors = ['tab:blue', 'tab:red', 'tab:green']
for i in range(4):
    d_sets[0, :, i] = np.loadtxt(file1, delimiter=',', usecols=i)
    d_sets[1, :, i] = np.loadtxt(file2, delimiter=',', usecols=i)
    d_sets[2, :, i] = np.loadtxt(file3, delimiter=',', usecols=i)

    d_sets_scaled[0, :, i] = (d_sets[0, :, i] - np.min(d_sets[0, :, i])) / (np.max(d_sets[0, :, i]) - np.min(d_sets[0, :, i]))
    d_sets_scaled[1, :, i] = (d_sets[1, :, i] - np.min(d_sets[1, :, i])) / (np.max(d_sets[1, :, i]) - np.min(d_sets[1, :, i]))
    d_sets_scaled[2, :, i] = (d_sets[2, :, i] - np.min(d_sets[2, :, i])) / (np.max(d_sets[2, :, i]) - np.min(d_sets[2, :, i]))

plt.rc('font', family='Arial', size=28)
plt.ylabel('processes (number)')
plt.xlabel('timestamp (ms)')
line_styles = ['-', '--', '-.']
markers = ['o', 's', 'D']
plt.plot(d_sets[0, :, 0], lw = 3, color = colors[0], linestyle=line_styles[0], marker=markers[0], markevery=500)
plt.plot(d_sets[1, :, 0], lw = 3, color = colors[1], linestyle=line_styles[1], marker=markers[1], markevery=500)
plt.plot(d_sets[2, :, 0], lw = 3, color = colors[2], linestyle=line_styles[2], marker=markers[2], markevery=500)
plt.legend(['Launch (1)', 'Launch (2)', 'Launch (3)'], fontsize=20, labelspacing=0.2)
plt.tight_layout()
plt.ylim(4490, 4555)
plt.xticks(np.arange(0, 5001, 2500))
plt.savefig("../paper/ieee/fig5a.pdf", format='pdf')
plt.close()

plt.ylabel('normalized value')
plt.xlabel('timestamp (ms)')
line_styles = ['-', '--', '-.']
markers = ['o', 's', 'D']
plt.plot(d_sets_scaled[0, :, 0], lw = 3, color = colors[0], linestyle=line_styles[0], marker=markers[0], markevery=500)
plt.plot(d_sets_scaled[1, :, 0], lw = 3, color = colors[1], linestyle=line_styles[1], marker=markers[1], markevery=500)
plt.plot(d_sets_scaled[2, :, 0], lw = 3, color = colors[2], linestyle=line_styles[2], marker=markers[2], markevery=500)
plt.legend(['Launch (1)', 'Launch (2)', 'Launch (3)'], fontsize=20, labelspacing=0.2)
plt.tight_layout()
plt.ylim(0, 1.199999)
plt.xticks(np.arange(0, 5001, 2500))
plt.savefig("../paper/ieee/fig5b.pdf", format='pdf')
plt.close()
