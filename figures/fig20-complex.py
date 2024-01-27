# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

def noise():
    apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
    devices = ['0 proc', '1 proc', '2 procs', '3 procs']
    accu = [
        [1.0000, 1.0000, 0.9887, 0.9438, 0.9841], # 0
        [0.9663, 0.8380, 0.8525, 0.8112, 0.8653], # 1
        [0.8375, 0.7010, 0.6913, 0.7188, 0.7350], # 2
        [0.8062, 0.6850, 0.6000, 0.7575, 0.6993], # 3
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
    plt.savefig("../paper/ieee/fig20.pdf", format='pdf')
    plt.close()


def noise2():
    apps = ['Telegram', 'Youtube', 'Gmail', 'OneNote', 'All']
    devices = ['0 proc', '1 proc', '2 procs', '3 procs']
    accu = [
        [0.9711, 0.9641, 0.9877, 0.9912, 0.9775], # 0
        [0.9959, 0.9837, 0.9754, 0.9605, 0.9794], # 1
        [0.9380, 0.9379, 0.9221, 0.8947, 0.9245], # 2
        [0.9421, 0.8529, 0.8975, 0.9298, 0.9020], # 3
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
    plt.savefig("../paper/ieee/fig21.pdf", format='pdf')
    plt.close()


def pattern():
    apps = ['1 char', '2 chars', '3 chars', '4 chars']
    devices = ['0.2s', '0.4s', '0.6s', '0.8s', '1.0s']
    accu = [
        [0.9550, 0.9450, 0.9700, 0.9700], # 0.2
        [0.9900, 0.9700, 0.9650, 0.9600], # 0.4
        [0.9400, 0.9600, 0.9400, 0.9600], # 0.6
        [0.9400, 0.9700, 0.9400, 0.9600], # 0.8
        [0.9400, 0.9200, 0.9300, 0.9200], # 1.0
    ]

    plt.rc('font', family='Arial', size=24)
    for i in range(4):
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
    plt.ylim(0, 1.599999)
    plt.yticks(np.arange(0, 1.5, 0.5))
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig22.pdf", format='pdf')
    plt.close()

noise()
noise2()
pattern()