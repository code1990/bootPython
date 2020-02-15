# Python 五人分鱼
def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1)
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 1


if __name__ == "__main__":
    main()
