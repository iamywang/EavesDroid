# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

file1 = 'data/exp0-figures/OPPO OPPO PGJM10/2_286.txt'
file2 = 'data/exp0-figures/OPPO OPPO PGJM10/2_202.txt'
file3 = 'data/exp0-figures/OPPO OPPO PGJM10/2_142.txt'
file4 = 'data/exp0-figures/OPPO OPPO PGJM10/1_157.txt'
file5 = 'data/exp0-figures/OPPO OPPO PGJM10/2_226.txt'
file6 = 'data/exp0-figures/OPPO OPPO PGJM10/3_159.txt'


# norm
d_sets = np.zeros([6, 5000, 4], np.double)
colors = ['tab:blue', 'tab:red', 'tab:green']
for i in range(4):
    d_sets[0, :, i] = np.loadtxt(file1, delimiter=',', usecols=i)
    d_sets[1, :, i] = np.loadtxt(file2, delimiter=',', usecols=i)
    d_sets[2, :, i] = np.loadtxt(file3, delimiter=',', usecols=i)
    d_sets[3, :, i] = np.loadtxt(file4, delimiter=',', usecols=i)
    d_sets[4, :, i] = np.loadtxt(file5, delimiter=',', usecols=i)
    d_sets[5, :, i] = np.loadtxt(file6, delimiter=',', usecols=i)


plt.rc('font', family='Arial', size=28)
plt.ylabel('processes (number)')
plt.xlabel('timestamp (ms)')
line_styles = ['-', '--', '-.']
markers = ['o', 's', 'D']
plt.plot(d_sets[3, :, 0], lw = 3, color = colors[0], linestyle=line_styles[0], marker=markers[0], markevery=500)
plt.plot(d_sets[4, :, 0], lw = 3, color = colors[1], linestyle=line_styles[1], marker=markers[1], markevery=500)
plt.plot(d_sets[5, :, 0], lw = 3, color = colors[2], linestyle=line_styles[2], marker=markers[2], markevery=500)
plt.legend(['View', 'Send', 'Info'], fontsize=20, labelspacing=0.2, ncol=1)
plt.ylim(4490, 4650)
plt.xticks(np.arange(0, 5001, 2500))
plt.tight_layout()
plt.savefig("../paper/ieee/fig2a.pdf", format='pdf')
plt.close()

plt.rc('font', family='Arial', size=28)
plt.ylabel('processes (number)')
plt.xlabel('timestamp (ms)')
line_styles = ['-', '--', '-.']
markers = ['o', 's', 'D']
plt.plot(d_sets[0, :, 0], lw = 3, color = colors[0], linestyle=line_styles[0], marker=markers[0], markevery=500)
plt.plot(d_sets[1, :, 0], lw = 3, color = colors[1], linestyle=line_styles[1], marker=markers[1], markevery=500)
plt.plot(d_sets[2, :, 0], lw = 3, color = colors[2], linestyle=line_styles[2], marker=markers[2], markevery=500)
plt.legend(['Send (1)', 'Send (2)', 'Send (3)'], fontsize=20, labelspacing=0.2, ncol=1)
plt.ylim(4540, 4620)
plt.xticks(np.arange(0, 5001, 2500))
plt.tight_layout()
plt.savefig("../paper/ieee/fig2b.pdf", format='pdf')
plt.close()
