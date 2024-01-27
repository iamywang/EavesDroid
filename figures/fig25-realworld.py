# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

# accuracy
apps = ['User 1', 'User 2', 'User 3', 'User 4', 'User 5', 'User 6']
devices = ['Model with noisy data', 'Model without noisy data']
accu = [
    [0.6667, 0.6875, 0.6316, 0.6190, 0.6842, 0.7059], # 0.6658
    [0.8571, 0.9412, 0.8125, 0.8333, 0.8750, 0.8421], # 0.8602
]

plt.rc('font', family='Arial', size=20)
for i in range(6):
    plt.ylabel('Accuracy')
    colors = ['tab:blue', 'tab:orange']
    bar_width = 0.3
    bar_x = np.arange(len(apps))
    bar1 = plt.bar(bar_x[i] - bar_width/2 - 0.02, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
    bar2 = plt.bar(bar_x[i] + bar_width/2 + 0.02, accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
plt.legend((bar1, bar2), devices, fontsize=16, labelspacing=0.2)
plt.xticks(bar_x, apps, rotation=30)
plt.ylim(0, 1.3)
plt.yticks(np.arange(0, 1.5, 0.5))
plt.tight_layout()
plt.savefig("../paper/ieee/fig25.pdf", format='pdf')
plt.close()
