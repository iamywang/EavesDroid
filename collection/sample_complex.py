# =============================================================================
# This file is part of EavesDroid.
#
# Author: iamywang
# Date Created: Jan 27, 2024
# =============================================================================
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import time
from backend.backend.view import *


# =============================================================================
# Arguments
# =============================================================================
args_xiaomi_9 = ["data/Xiaomi Xiaomi MI 9/12 32/test/"]


# =============================================================================
# Set label
# =============================================================================
def data_set_label(path, num_groups, num_features, offset):
    """
    Set labels for data set.

    Args:
        num_groups: number of data in each group
        num_features: number of features

    Returns:
        none
    """
    flist = os.listdir(path)
    nums = len(flist)
    for i in range(nums):
        fpath = flist[i]
        index = int(fpath.split('.')[0])
        label = int(index / num_groups) * num_features + index % num_features + offset
        print(str(index), '->', label, str(int(index / num_features)))
        os.rename(path + fpath, path + str(label) + '_' +
                  str(int(index / num_features)) + '.txt')


# =============================================================================
# Move
# =============================================================================
def data_move(path_1, path_2):
    """
    Move data from path_1 to path_2.

    Args:
        path_1: source path
        path_2: destination path
    """
    flist = os.listdir(path_1)
    nums = len(flist)
    for i in range(nums):
        fpath = flist[i]
        os.rename(path_1 + fpath, path_2 + fpath)


def seq_2b(nums, args):
    timestamp1 = time.time()
    rounds = 0

    for i in range(nums):
    # kind 17: tg yt
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)
        
    # kind 18: tg gm
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')

    # kind 19: tg on
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            time.sleep(1)
    
    # kind 20: yt tg
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)
    
    # kind 21: yt gm
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            os.system('adb shell am force-stop com.google.android.gm')
            time.sleep(1)
    
    # kind 22: yt on
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            time.sleep(1)
    
    # kind 23: gm tg
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)
    
    # kind 24: gm yt
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)
        
    # kind 25: gm on
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            time.sleep(1)
    
    # kind 26: on tg
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)
    
    # kind 27: on yt
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)
    
    # kind 28: on gm
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(4)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            os.system('adb shell am force-stop com.google.android.gm')
            time.sleep(1)


def seq_3b(nums, args):
    timestamp1 = time.time()
    rounds = 0

    for i in range(nums):
    # kind 29: tg yt gm
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            os.system('adb shell am force-stop com.google.android.youtube')
            os.system('adb shell am force-stop com.google.android.gm')
            time.sleep(1)
        
    # kind 30: tg gm on
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am force-stop com.microsoft.office.onenote')

    # kind 31: tg on yt
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)
    
    # kind 32: yt tg gm
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            os.system('adb shell am force-stop com.google.android.gm')
            time.sleep(1)
    
    # kind 33: yt gm on
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            os.system('adb shell am force-stop com.google.android.gm')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            time.sleep(1)
    
    # kind 34: yt on tg
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)
    
    # kind 35: gm tg yt
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)
    
    # kind 36: gm yt on
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            os.system('adb shell am force-stop com.google.android.youtube')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            time.sleep(1)
        
    # kind 37: gm on tg
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)
    
    # kind 38: on tg yt
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)
    
    # kind 39: on yt gm
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            os.system('adb shell am force-stop com.google.android.youtube')
            os.system('adb shell am force-stop com.google.android.gm')
            time.sleep(1)
    
    # kind 40: on gm tg
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            os.system('adb shell am force-stop com.google.android.gm')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)


# =============================================================================
# Main
# =============================================================================
if __name__ == '__main__':
    if not os.path.exists('data/exp4-complex/sequence/17_0.txt'):
        seq_2b(200, args_xiaomi_9)
        data_set_label('data/Xiaomi Xiaomi MI 9/12 32/test/', 2400, 12, 17)
        data_move('data/Xiaomi Xiaomi MI 9/12 32/test/', 'data/exp4-complex/sequence/')
    if not os.path.exists('data/exp4-complex/sequence/29_0.txt'):
        seq_3b(200, args_xiaomi_9)
        data_set_label('data/Xiaomi Xiaomi MI 9/12 32/test/', 2400, 12, 29)
        data_move('data/Xiaomi Xiaomi MI 9/12 32/test/', 'data/exp4-complex/sequence/')
