
from __future__ import print_function
import random


def main():
    num = random.randint(1, 100)
    play_game(num)


def play_game(num):
    print(num)
    while True:
        a = int(input('请输入1~100任意一个数:'))
        if a > num:
            print('猜的有点大哦')
        elif a < num:
            print('猜的有点小哦')
        else:
            print('恭喜你猜对了')
            play_again()


def play_again():
    q = input('在玩儿一次？Y/N')
    if q == 'Y':
        main()
    elif q == 'N':
        exit()
    else:
        print('请输入Y/N')
        play_again()

if __name__ == '__main__':
    main()

