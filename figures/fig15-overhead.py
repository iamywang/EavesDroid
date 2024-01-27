# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import os
import numpy as np
import matplotlib.pyplot as plt

types = ['time', 'power', 'traffic', 'compute']

def time_overhead():
    accu = np.loadtxt('data/exp2-overhead/time_total.txt', delimiter=',')
    accu = accu * 1000
    accu = accu.astype(int)

    less_40 = 0
    for i in range(25, 40):
        less_40 += np.sum(accu == i)
    print(less_40, len(accu), less_40/len(accu))
    print(np.average(accu))
    print(np.min(accu), np.max(accu))

    plt.rc('font', family='Arial', size=28)
    for i in range(25, 81):
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
        plt.bar(i, np.sum(accu == i), color=colors[0], edgecolor='black')
    plt.ylabel('Number of behaviors')
    plt.xlabel('Inference time (ms)')
    plt.xticks(np.arange(26, 81, 18))
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig15.pdf", format='pdf')
    plt.close()


def power_overhead():
    devices = ['OPPO K10', 'Redmi K50']
    labels = ['With EavesDroid', 'Without EavesDroid']
    accu = [
        [320.6, 377.1],
        [295.7, 348.6]
    ]

    print(accu[0][0]-accu[1][0], (accu[0][0]-accu[1][0])/accu[0][0])
    print(accu[0][1]-accu[1][1], (accu[0][1]-accu[1][1])/accu[0][1])
    print(((accu[0][0]-accu[1][0])/accu[0][0] + (accu[0][1]-accu[1][1])/accu[0][1])/2)

    plt.rc('font', family='Arial', size=28)
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    bar_width = 0.3
    bar_x = np.arange(len(labels))
    for i in range(2):
        bar1 = plt.bar(bar_x[i] - bar_width/2 - 0.02, accu[0][i], width=bar_width, color=colors[0], edgecolor='black', hatch='/')
        bar2 = plt.bar(bar_x[i] + bar_width/2 + 0.02, accu[1][i], width=bar_width, color=colors[1], edgecolor='black', hatch='\\')
    plt.legend((bar1, bar2), labels, fontsize=20, labelspacing=0.2)
    plt.ylabel('Power consumption (mA)')
    plt.xticks(bar_x, devices)
    plt.ylim(0, 599)
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig16.pdf", format='pdf')
    plt.close()


def compute_overhead():
    labels = ['CPU', 'Memory']

    cpu_overhead = np.loadtxt('data/exp2-overhead/cpu_overhead.txt')[0:960]
    cpu_overhead = cpu_overhead / 10
    print(np.min(cpu_overhead), np.max(cpu_overhead), np.average(cpu_overhead))
    cpu_overhead = cpu_overhead.reshape(-1, 60)
    cpu_overhead = np.average(cpu_overhead, axis=1)
    mem_overhead = np.loadtxt('data/exp2-overhead/memory_overhead.txt')[0:960]
    mem_overhead = mem_overhead / 10
    print(np.min(mem_overhead), np.max(mem_overhead), np.average(mem_overhead))
    mem_overhead = mem_overhead.reshape(-1, 60)
    mem_overhead = np.average(mem_overhead, axis=1)
    index = np.arange(len(cpu_overhead))
    index += 1

    plt.rc('font', family='Arial', size=28)
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    plt.xlabel('Time (min)')

    ax1 = plt.subplot(111)
    ax1.plot(index, cpu_overhead, color=colors[0], marker='o', lw=2, label=labels[0])
    ax1.set_ylabel('CPU overhead (%)')
    ax1.set_ylim(0, 149)

    ax2 = ax1.twinx()
    ax2.bar(index, mem_overhead, width=0.6, color=colors[1], label=labels[1], edgecolor='black')
    ax2.set_ylabel('Memory overhead (MB)')
    ax2.set_ylim(0, 59)

    plt.legend((ax1.lines[0], ax2.patches[0]), labels, fontsize=20, labelspacing=0.2)
    
    plt.xticks(np.arange(1, 17, 5))
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig17.pdf", format='pdf')
    plt.close()


def network_overhead():
    path = ['data/exp3-adaptability/cross/OPPO OPPO PGJM10/', 'data/exp3-adaptability/cross/Xiaomi Redmi 22041211AC/', 'data/exp3-adaptability/cross/Xiaomi Xiaomi MI 9/12 32/']
    devices = ['OPPO K10', 'Redmi K50', 'Xiaomi 9']
    sizes = []
    plt.rc('font', family='Arial', size=28)
    for i in range(len(devices)):
        files = os.listdir(path[i])

        files_size = []
        for file in files:
            files_size.append(os.path.getsize(path[i] + file))
        files_size = np.array(files_size)
        files_size = files_size / 1024
        sizes.append(files_size)

    
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    bar_width = 0.3
    bar_x = np.arange(len(devices))
    plt.barh(bar_x[0], np.max(sizes[0]) - np.min(sizes[0]), height=bar_width, color=colors[0], edgecolor='black', left=np.min(sizes[0]))
    plt.barh(bar_x[1], np.max(sizes[1]) - np.min(sizes[1]), height=bar_width, color=colors[0], edgecolor='black', left=np.min(sizes[1]))
    plt.barh(bar_x[2], np.max(sizes[2]) - np.min(sizes[2]), height=bar_width, color=colors[0], edgecolor='black', left=np.min(sizes[2]))
    plt.vlines(np.mean(sizes[0]), bar_x[0] - bar_width/2, bar_x[0] + bar_width/2, color=colors[1], linestyles='--', linewidth=2)
    plt.vlines(np.mean(sizes[1]), bar_x[1] - bar_width/2, bar_x[1] + bar_width/2, color=colors[1], linestyles='--', linewidth=2)
    plt.vlines(np.mean(sizes[2]), bar_x[2] - bar_width/2, bar_x[2] + bar_width/2, color=colors[1], linestyles='--', linewidth=2)
    plt.xlabel('Packet size (KB)')
    plt.yticks(bar_x, devices)
    plt.xlim(181, 196)
    plt.xticks(np.arange(181, 197, 5))
    plt.tight_layout()
    plt.savefig("../paper/ieee/fig18.pdf", format='pdf')
    plt.close()

    print(np.mean(sizes[0]), np.mean(sizes[1]), np.mean(sizes[2]), np.mean(sizes))
    print(np.min(sizes), np.max(sizes))

time_overhead()
power_overhead()
network_overhead()
compute_overhead()