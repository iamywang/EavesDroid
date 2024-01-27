# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

types = ['minmax', 'cnngru', 'dimension', 'interval', 'minmax2']


def minmax():
    apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
    devices = ['D-K (raw)', 'D-K (nor)', 'C-G (raw)', 'C-G (nor)']
    accu = [
        # DTW-KNN
        [0.8833, 0.7767, 0.9292, 0.5500, 0.6892],
        [0.9542, 0.8833, 0.9833, 0.7375, 0.8510],
        # CNN-GRU
        [0.9167, 0.9200, 0.9708, 0.9375, 0.9206],
        [0.9792, 0.9667, 1.0000, 0.9750, 0.9755]
    ]

    plt.rc('font', family='Arial', size=24)
    for i in range(5):
        plt.ylabel('Accuracy')
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
        bar_width = 0.15
        bar_x = np.arange(len(apps))
        bar1 = plt.bar(bar_x[i] - 3 * bar_width/2 - 0.06, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
        bar2 = plt.bar(bar_x[i] - bar_width/2 - 0.02, accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
        bar3 = plt.bar(bar_x[i] + bar_width/2 + 0.02, accu[2][i], width=bar_width, color=colors[2], edgecolor='black', hatch='o')
        bar4 = plt.bar(bar_x[i] + 3 * bar_width/2 + 0.06, accu[3][i], width=bar_width, color=colors[3], edgecolor='black', hatch='*')
    plt.legend((bar1, bar2, bar3, bar4), devices, fontsize=18, labelspacing=0.2, ncol=2)
    plt.xticks(bar_x, apps, rotation=30)
    plt.ylim(0, 1.499999)
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig11.pdf", format='pdf')
    plt.close()


def cnngru():
    apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
    devices = ['D-K (1)', 'D-K (3)', 'D-K (5)', 'CNN-GRU']
    accu = [
        [0.9542, 0.8833, 0.9833, 0.7375, 0.8510],
        [0.9500, 0.8767, 0.9875, 0.7542, 0.8441],
        [0.9375, 0.8867, 0.9875, 0.7333, 0.8461],
        [0.9792, 0.9667, 1.0000, 0.9750, 0.9755]
    ]

    plt.rc('font', family='Arial', size=24)
    for i in range(5):
        plt.ylabel('Accuracy')
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
        bar_width = 0.15
        bar_x = np.arange(len(apps))
        bar1 = plt.bar(bar_x[i] - 3 * bar_width/2 - 0.06, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
        bar2 = plt.bar(bar_x[i] - bar_width/2 - 0.02, accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
        bar3 = plt.bar(bar_x[i] + bar_width/2 + 0.02, accu[2][i], width=bar_width, color=colors[2], edgecolor='black', hatch='o')
        bar4 = plt.bar(bar_x[i] + 3 * bar_width/2 + 0.06, accu[3][i], width=bar_width, color=colors[3], edgecolor='black', hatch='*')
    plt.legend((bar1, bar2, bar3, bar4), devices, fontsize=18, labelspacing=0.2, ncol=2)
    plt.xticks(bar_x, apps, rotation=30)
    plt.ylim(0, 1.499999)
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig9.pdf", format='pdf')
    plt.close()


def cnngru2():
    apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
    devices = ['1d-CNN', 'LSTM', 'GRU', 'CNN-GRU']
    accu = [
        [0.9050, 0.9033, 0.9698, 0.8740, 0.9118],
        [0.7185, 0.7491, 0.8213, 0.5731, 0.7137],
        [0.9757, 0.9661, 0.9487, 0.9508, 0.9608],
        [0.9792, 0.9667, 1.0000, 0.9750, 0.9755]
    ]

    plt.rc('font', family='Arial', size=24)
    for i in range(5):
        plt.ylabel('Accuracy')
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
        bar_width = 0.15
        bar_x = np.arange(len(apps))
        bar1 = plt.bar(bar_x[i] - 3 * bar_width/2 - 0.06, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
        bar2 = plt.bar(bar_x[i] - bar_width/2 - 0.02, accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
        bar3 = plt.bar(bar_x[i] + bar_width/2 + 0.02, accu[2][i], width=bar_width, color=colors[2], edgecolor='black', hatch='o')
        bar4 = plt.bar(bar_x[i] + 3 * bar_width/2 + 0.06, accu[3][i], width=bar_width, color=colors[3], edgecolor='black', hatch='*')
    plt.legend((bar1, bar2, bar3, bar4), devices, fontsize=18, labelspacing=0.2, ncol=2)
    plt.xticks(bar_x, apps, rotation=30)
    plt.ylim(0, 1.499999)
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig10.pdf", format='pdf')
    plt.close()


def dimension():
    apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
    devices = ['1 feature', '2 features', '5 features']
    accu = [
        [0.8875, 0.8867, 0.9250, 0.8875, 0.9029],
        [0.9708, 0.9367, 0.9708, 0.9375, 0.9255],
        [0.9958, 0.9700, 1.0000, 0.9917, 0.9863]
    ]

    plt.rc('font', family='Arial', size=24)
    for i in range(5):
        plt.ylabel('Accuracy')
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
        bar_width = 0.2
        bar_x = np.arange(len(apps))
        bar1 = plt.bar(bar_x[i] - bar_width - 0.04, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
        bar2 = plt.bar(bar_x[i], accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
        bar3 = plt.bar(bar_x[i] + bar_width + 0.04, accu[2][i], width=bar_width, color=colors[2], edgecolor='black', hatch='o')
    plt.legend((bar1, bar2, bar3), devices, fontsize=18, labelspacing=0.2, ncol=2)
    plt.xticks(bar_x, apps, rotation=30)
    plt.ylim(0, 1.499999)
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig13.pdf", format='pdf')
    plt.close()


def interval():
    apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
    devices = ['1ms', '2ms', '4ms', '5ms']
    accu = [
        [0.9958, 0.9700, 1.0000, 0.9917, 0.9863],
        [0.8083, 0.4967, 0.6500, 0.3833, 0.5902],
        [0.5375, 0.3167, 0.3375, 0.2625, 0.3549],
        [0.5250, 0.3167, 0.3000, 0.2292, 0.3363]
    ]

    plt.rc('font', family='Arial', size=24)
    for i in range(5):
        plt.ylabel('Accuracy')
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
        bar_width = 0.15
        bar_x = np.arange(len(apps))
        bar1 = plt.bar(bar_x[i] - 3 * bar_width/2 - 0.06, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
        bar2 = plt.bar(bar_x[i] - bar_width/2 - 0.02, accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
        bar3 = plt.bar(bar_x[i] + bar_width/2 + 0.02, accu[2][i], width=bar_width, color=colors[2], edgecolor='black', hatch='o')
        bar4 = plt.bar(bar_x[i] + 3 * bar_width/2 + 0.06, accu[3][i], width=bar_width, color=colors[3], edgecolor='black', hatch='*')
    plt.legend((bar1, bar2, bar3, bar4), devices, fontsize=18, labelspacing=0.2, ncol=2)
    plt.xticks(bar_x, apps, rotation=30)
    plt.ylim(0, 1.499999)
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig14.pdf", format='pdf')
    plt.close()


def minmax2():
    apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
    devices = ['raw', 'min-max nor', 'mean nor', 'z-score', 'mean sub']
    accu = [
        [0.9167, 0.9200, 0.9708, 0.9375, 0.9206], # raw
        [0.9792, 0.9667, 1.0000, 0.9750, 0.9755], # min-max nor
        [0.9848, 0.9545, 0.9297, 0.9821, 0.9588], # mean nor
        [0.9747, 0.9389, 0.9375, 0.9821, 0.9480], # z-score
        [0.9394, 0.9279, 0.9028, 0.9342, 0.9255]  # mean sub
    ]

    plt.rc('font', family='Arial', size=24)
    for i in range(5):
        plt.ylabel('Accuracy')
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
        bar_width = 0.12
        bar_x = np.arange(len(apps))
        bar1 = plt.bar(bar_x[i] - 4 * bar_width/2 - 0.08, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
        bar2 = plt.bar(bar_x[i] - 2 * bar_width/2 - 0.04, accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
        bar3 = plt.bar(bar_x[i], accu[2][i], width=bar_width, color=colors[2], edgecolor='black', hatch='o')
        bar4 = plt.bar(bar_x[i] + 2 * bar_width/2 + 0.04, accu[3][i], width=bar_width, color=colors[3], edgecolor='black', hatch='*')
        bar5 = plt.bar(bar_x[i] + 4 * bar_width/2 + 0.08, accu[4][i], width=bar_width, color=colors[4], edgecolor='black', hatch='xx')
    plt.legend((bar1, bar2, bar3, bar4, bar5), devices, fontsize=18, labelspacing=0.2, ncol=2)
    plt.xticks(bar_x, apps, rotation=30)
    plt.ylim(0, 1.65)
    plt.yticks(np.arange(0, 1.5, 0.5))
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig12.pdf", format='pdf')
    plt.close()

minmax()
cnngru()
cnngru2()
dimension()
interval()
minmax2()
