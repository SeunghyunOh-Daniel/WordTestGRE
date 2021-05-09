def word_test():
    day = 6
    text = open("text_wordlist/"+str(day)+".txt", "r")
    text = text.read().split("\n")
    # print(text)
    text = [v for v in text if v]
    # print(text)

    text = [t.split(":") for t in text]

    print("----TEST----")
    for problem in text:
        print(problem[0])


if __name__ == '__main__':
    word_test()
