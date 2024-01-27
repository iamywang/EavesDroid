# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt


apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
devices = ['OPPO K10', 'Redmi K50']
accu = [
    [0.9792, 0.9667, 1.0000, 0.9750, 0.9755],
    [0.9958, 0.9700, 1.0000, 0.9917, 0.9863]
]

plt.rc('font', family='Arial', size=20)
for i in range(5):
    plt.ylabel('Accuracy')
    colors = ['tab:blue', 'tab:orange']
    bar_width = 0.3
    bar_x = np.arange(len(apps))
    bar1 = plt.bar(bar_x[i] - bar_width/2 - 0.02, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
    bar2 = plt.bar(bar_x[i] + bar_width/2 + 0.02, accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
plt.legend((bar1, bar2), devices, fontsize=16, labelspacing=0.2, ncol=2)
plt.xticks(bar_x, apps, rotation=30)
plt.ylim(0, 1.3)
plt.yticks(np.arange(0, 1.5, 0.5))
plt.tight_layout()
plt.savefig("../paper/ieee/fig7.pdf", format='pdf')
plt.close()