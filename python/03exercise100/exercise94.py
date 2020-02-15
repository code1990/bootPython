# 时间函数举例4,一个猜数游戏，判断一个人反应快慢。
if __name__ == "__main__":
    import time
    import random

    play_it = input("play")
    while play_it != "y":
        c = input("\n")
        i = random.randint(0, 2 ** 32) % 100
        start = time.clock()
        a = time.time()
        guess = int(input("\n"))
        while guess != i:
            if guess > i:
                print("aaa")
                guess = int(input("\n"))
            else:
                print("input\n")
                guess = int(input())
        end = time.time()
        b = time.time()
        var = (end - start) / 18.2
        print(var)
        if var < 15:
            print("xxx")
        elif var < 25:
            print("xxx")
        else:
            print("")
        print("")
        print("")
        play_it = input("")
