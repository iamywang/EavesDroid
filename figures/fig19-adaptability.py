# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
devices = ['SM SV', 'SM DV', 'DM SV', 'DM DV']
accu = [
      [0.9792, 0.9667, 1.0000, 0.9750, 0.9755],
      [0.5663, 0.4590, 0.6025, 0.3025, 0.3076],
      [0.9688, 0.9060, 0.9388, 0.9262, 0.8212],
      [0.6162, 0.3650, 0.5028, 0.6700, 0.2183]
      ]

plt.rc('font', family='Arial', size=20)
for i in range(5):
        plt.ylabel('Accuracy')
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
        bar_width = 0.15
        bar_x = np.arange(len(apps))
        bar1 = plt.bar(bar_x[i] - 3 * bar_width/2 - 0.06, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
        bar2 = plt.bar(bar_x[i] - bar_width/2 - 0.02, accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
        bar3 = plt.bar(bar_x[i] + bar_width/2 + 0.02, accu[2][i], width=bar_width, color=colors[2], edgecolor='black', hatch='o')
        bar4 = plt.bar(bar_x[i] + 3 * bar_width/2 + 0.06, accu[3][i], width=bar_width, color=colors[3], edgecolor='black', hatch='*')
plt.legend((bar1, bar2, bar3, bar4), devices, fontsize=16, labelspacing=0.2, ncol=2)
plt.xticks(bar_x, apps, rotation=30)
plt.ylim(0, 1.4)
plt.yticks(np.arange(0, 1.5, 0.5))
plt.tight_layout()
plt.savefig("../paper/ieee/fig19.pdf", format='pdf')
plt.close()
