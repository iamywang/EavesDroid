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
# Telegram
# =============================================================================
args_oppo_k10_telegram = ["600 600", "600 400", "200 2350", "1000 1500",
                          "100 200", "200 300", "data/OPPO OPPO PGJM10/12 31/test/"]
args_redmi_k50_telegram = ["600 600", "600 400", "200 3000", "1350 1950",
                           "100 200", "200 300", "data/Xiaomi Redmi 22041211AC/12 31/test/"]
args_xiaomi_9_telegram = ["600 500", "600 300", "200 2250", "1000 1450", # miui 1350
                            "100 150", "150 200", "data/Xiaomi Xiaomi MI 9/12 32/test/"]


def telegram(nums, args):
    timestamp1 = time.time()
    rounds = 0

    # kind 0: launch
    for i in range(nums):
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system(
                'adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)

    # kind 1: view
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system(
                'adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[0])
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)

    # kind 2: send
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system("adb shell input tap" + " " + args[1])
            time.sleep(1)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system(
                'adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[2])
            os.system("adb shell input text 'hello:" + str(i) + "'")
            time.sleep(0.5)
            os.system("adb shell input keyevent 62")
            time.sleep(0.5)
            os.system("adb shell input tap" + " " + args[3])
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)

    # kind 3: info
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system(
                'adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[4])
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[5])
            time.sleep(3)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop org.telegram.messenger.web')
            time.sleep(1)


# =============================================================================
# Youtube
# =============================================================================
args_oppo_k10_youtube = ["500 500 500 1000", "600 1700",
                         "300 2350", "850 200", "data/OPPO OPPO PGJM10/12 31/test/"]
args_redmi_k50_youtube = ["500 500 500 1500", "700 2000",
                          "450 3050", "1150 180", "data/Xiaomi Redmi 22041211AC/12 31/test/"]
args_xiaomi_9_youtube = ["500 500 500 1500", "600 1700",
                            "300 2250", "850 150", "data/Xiaomi Xiaomi MI 9/12 32/test/"]


def youtube(nums, args):
    timestamp1 = time.time()
    rounds = 0

    # kind 0: launch
    for i in range(nums):
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system(
                'adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)

    # kind 1: refersh
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system("adb shell input swipe" + " " + args[0])
            time.sleep(0.5)
            os.system("adb shell input swipe" + " " + args[0])
            os.system("adb shell input swipe" + " " + args[0])
            time.sleep(4)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)

    # kind 2: view
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(2)
            os.system("adb shell input tap" + " " + args[1])
            time.sleep(4)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)

    # kind 3: short
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[2])
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)

    # kind 4: search
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))
        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.youtube/.HomeActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[3])
            time.sleep(1)
            os.system("adb shell input text 'computer'")
            time.sleep(0.5)
            os.system("adb shell input keyevent 66")
            os.system("adb shell input keyevent 66")
            time.sleep(3)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.youtube')
            time.sleep(1)


# =============================================================================
# Gmail
# =============================================================================
args_oppo_k10_gmail = ["300 500", "800 2200", "900 200",
                       "300 200", "data/OPPO OPPO PGJM10/12 31/test/"]
args_redmi_k50_gmail = ["300 500", "1100 2800", "1200 200",
                        "300 200", "data/Xiaomi Redmi 22041211AC/12 31/test/"]
args_xiaomi_9_gmail = ["300 500", "800 2050", "900 150",
                        "300 150", "data/Xiaomi Xiaomi MI 9/12 32/test/"]


def gmail(nums, args):
    timestamp1 = time.time()
    rounds = 0

    # kind 0: launch
    for i in range(nums):
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            time.sleep(1)

    # kind 1: view
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[0])
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            time.sleep(1)

    # kind 2: send
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[1])
            time.sleep(1)
            os.system("adb shell input text 'kingwang2021@gmail.com'")
            time.sleep(0.5)
            os.system("adb shell input tap" + " " + args[2])
            time.sleep(4)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            time.sleep(1)

    # kind 3: search
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system('adb shell am start com.google.android.gm/.GmailActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[3])
            time.sleep(1)
            os.system("adb shell input text 'onedrive'")
            time.sleep(0.5)
            os.system("adb shell input keyevent 66")
            time.sleep(4)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.google.android.gm')
            time.sleep(1)


# =============================================================================
# OneNote
# =============================================================================
args_oppo_k10_onenote = ["200 300", "950 2150", "550 2350", "data/OPPO OPPO PGJM10/12 31/test/"]
args_redmi_k50_onenote = ["200 400", "1250 2750", "750 3050", "data/Xiaomi Redmi 22041211AC/12 31/test/"]
args_xiaomi_9_onenote = ["200 300", "950 2000", "550 2250", "data/Xiaomi Xiaomi MI 9/12 32/test/"]
args_xiaomi_9_onenote2 = ["200 500", "150 2200", "1000 150", "data/Xiaomi Xiaomi MI 9/12 32/test/"]

def onenote(nums, args):
    timestamp1 = time.time()
    rounds = 0

    # kind 0: launch
    for i in range(nums):
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system(
                'adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            time.sleep(1)

    # kind 1: view
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system(
                'adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[0])
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            time.sleep(1)

    # kind 2: new
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system(
                'adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[1])
            time.sleep(1)
            os.system("adb shell input text 'new note: " + str(i) + "'")
            time.sleep(5)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            time.sleep(1)

    # kind 3: search
        rounds += 1
        timestamp2 = time.time()
        print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

        while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
            os.system(
                'adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(3)
            os.system('adb shell am start com.iamywang.sampler/.MainActivity')
            time.sleep(1)
            os.system(
                'adb shell am start com.microsoft.office.onenote/.ui.EntryActivity')
            time.sleep(1)
            os.system("adb shell input tap" + " " + args[2])
            time.sleep(1)
            os.system("adb shell input text 'aaaa'")
            time.sleep(0.5)
            os.system("adb shell input keyevent 66")
            time.sleep(4)

            os.system('adb shell am force-stop com.iamywang.sampler')
            os.system('adb shell am force-stop com.microsoft.office.onenote')
            time.sleep(1)


# =============================================================================
# Telegram - patterns 6.7.3
# =============================================================================
def telegram_patterns(nums, args):
    timestamp1 = time.time()
    rounds = 0

    intervals = [0.2, 0.4, 0.6, 0.8, 1.0]
    characters = [1, 2, 3, 4]

    # 0~199: 0.2s, 1 character
    # 200~399: 0.2s, 2 characters
    # 400~599: 0.2s, 3 characters
    # 600~799: 0.2s, 4 characters
    # 800~999: 0.4s, 1 character
    # 1000~1199: 0.4s, 2 characters
    # 1200~1399: 0.4s, 3 characters
    # 1400~1599: 0.4s, 4 characters
    # 1600~1799: 0.6s, 1 character
    # 1800~1999: 0.6s, 2 characters
    # 2000~2199: 0.6s, 3 characters
    # 2200~2399: 0.6s, 4 characters
    # 2400~2599: 0.8s, 1 character
    # 2600~2799: 0.8s, 2 characters
    # 2800~2999: 0.8s, 3 characters
    # 3000~3199: 0.8s, 4 characters
    # 3200~3399: 1.0s, 1 character
    # 3400~3599: 1.0s, 2 characters
    # 3600~3799: 1.0s, 3 characters
    # 3800~3999: 1.0s, 4 characters

    # kind 2: send
    for iv in intervals:
        for cr in characters:
            for i in range(nums):
                rounds += 1
                timestamp2 = time.time()
                print("round %d: %fs" % (rounds, timestamp2 - timestamp1))

                while not os.path.exists(args[-1] + str(rounds - 1) + '.txt'):
                    os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
                    time.sleep(3)
                    os.system("adb shell input tap" + " " + args[1])
                    time.sleep(1)
                    os.system("adb shell input text '" + str(rounds - 1) + ": '")
                    time.sleep(0.5)
                    os.system('adb shell am start com.iamywang.sampler/.MainActivity')
                    time.sleep(1)
                    os.system('adb shell am start org.telegram.messenger.web/org.telegram.ui.LaunchActivity')
                    time.sleep(1)
                    os.system("adb shell input tap" + " " + args[2])
                    for c in range(cr):
                        os.system("adb shell input text 'a'")
                        time.sleep(iv)
                    os.system("adb shell input keyevent 62")
                    time.sleep(iv)
                    os.system("adb shell input tap" + " " + args[3])
                    time.sleep(4)

                    os.system('adb shell am force-stop com.iamywang.sampler')
                    os.system('adb shell am force-stop org.telegram.messenger.web')
                    time.sleep(1)

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
    # test/ files
    flist = os.listdir(path)
    nums = len(flist)
    for i in range(nums):
        fpath = flist[i]
        index = int(fpath.split('.')[0])
        label = int(index / num_groups) * num_features + index % num_features + offset
        # rename
        print(str(index), '->', label, str(int(index / num_features)))
        os.rename(path + fpath, path + str(label) + '_' +
                  str(int(index / num_features)) + '.txt')


# =============================================================================
# Revert label
# =============================================================================
def data_revert_label(path, num_groups, num_features):
    flist = os.listdir(path)
    nums = len(flist)
    for i in range(nums):
        fpath = flist[i]
        label = int(fpath.split('_')[0]) - 9
        pos = int(fpath.split('_')[1].split('.')[0])
        index = pos * num_features + label
        # rename
        print(str(label), str(pos), '->', str(index))
        os.rename(path + fpath, path + str(index) + '.txt')

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

# =============================================================================
# Main - 4 apps in total
# =============================================================================
def exp_noise(background_processes):
    if not os.path.exists('data/exp-noise/'+ str(background_processes) + '/0_0.txt'):
        telegram(200, args_xiaomi_9_telegram)
        data_set_label('data/Xiaomi Xiaomi MI 9/12 32/test/', 800, 4, 0)
        data_move('data/Xiaomi Xiaomi MI 9/12 32/test/', 'data/exp-noise/' + str(background_processes) + '/')

    if not os.path.exists('data/exp-noise/'+ str(background_processes) + '/4_0.txt'):
        youtube(200, args_xiaomi_9_youtube)
        data_set_label('data/Xiaomi Xiaomi MI 9/12 32/test/', 1000, 5, 4)
        data_move('data/Xiaomi Xiaomi MI 9/12 32/test/', 'data/exp-noise/' + str(background_processes) + '/')

    if not os.path.exists('data/exp-noise/'+ str(background_processes) + '/9_0.txt'):
        gmail(200, args_xiaomi_9_gmail)
        data_set_label('data/Xiaomi Xiaomi MI 9/12 32/test/', 800, 4, 9)
        data_move('data/Xiaomi Xiaomi MI 9/12 32/test/', 'data/exp-noise/' + str(background_processes) + '/')
    
    if not os.path.exists('data/exp-noise/'+ str(background_processes) + '/13_0.txt'):
        onenote(200, args_xiaomi_9_onenote2)
        data_set_label('data/Xiaomi Xiaomi MI 9/12 32/test/', 800, 4, 13)
        data_move('data/Xiaomi Xiaomi MI 9/12 32/test/', 'data/exp-noise/' + str(background_processes) + '/')


def exp_noise_main():
    os.system('adb shell am force-stop com.android.chrome')
    os.system('adb shell am force-stop com.taobao.taobao')
    os.system('adb shell am force-stop com.sina.weibo')
    exp_noise(0)
    time.sleep(3)

    os.system('adb shell am force-stop com.android.chrome')
    os.system('adb shell am force-stop com.taobao.taobao')
    os.system('adb shell am force-stop com.sina.weibo')
    os.system('adb shell am start com.android.chrome/com.google.android.apps.chrome.Main')
    exp_noise(1)
    time.sleep(3)


    os.system('adb shell am force-stop com.android.chrome')
    os.system('adb shell am force-stop com.taobao.taobao')
    os.system('adb shell am force-stop com.sina.weibo')
    os.system('adb shell am start com.android.chrome/com.google.android.apps.chrome.Main')
    os.system('adb shell am start com.taobao.taobao/com.taobao.tao.TBMainActivity')
    exp_noise(2)
    time.sleep(3)

    os.system('adb shell am force-stop com.android.chrome')
    os.system('adb shell am force-stop com.taobao.taobao')
    os.system('adb shell am force-stop com.sina.weibo')
    os.system('adb shell am start com.android.chrome/com.google.android.apps.chrome.Main')
    os.system('adb shell am start com.taobao.taobao/com.taobao.tao.TBMainActivity')
    os.system('adb shell am start com.sina.weibo/com.sina.weibo.SplashActivity')
    exp_noise(3)
    time.sleep(3)

exp_noise_main()
