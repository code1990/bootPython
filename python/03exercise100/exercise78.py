# 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
if __name__ == "__main__":
    person = {"a": 18, "b": 20}
    m = "a"
    for key in person.keys():
        if person[m] < person[key]:
            m = key
    print(m, person[m])
