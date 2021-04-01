import sys, os
import numpy as np
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from __init__ import *

sys.path.append("/Users/seunghyunoh/workplace/Data/")
data_path = "/Users/seunghyunoh/workplace/Data/wordlist/"
data_name = "1.xlsx"
data_sheet = "표제어 list"
data_result = "result/result.txt"


def search_mean(word):
    # Ref. https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/

    urlRef = ['https://translate.google.co.kr/?sl=en&tl=ko&text=', '&op=translate']
    url = urlRef[0] + str(word) + urlRef[1]
    print(url)
    # initiating the webdriver. Parameter includes the path of the webdriver.
    path_driver = './'
    if "chromedriver.exe" not in os.listdir(path_driver):
        print("error: install chromedriver")
        return 0
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)

    # if you search about dynamic driver, then you have to wait 'loading'
    # this is just to ensure that the page is loaded
    time.sleep(5)

    html = driver.page_source

    # this renders the JS code and stores all
    # of the information in static HTML code.

    # Now, we could simply apply bs4 to html variable, html.parser or lxml
    soup = BeautifulSoup(html, "lxml")
    all_divs = soup.find('div', class_='fw3eif')
    try:
        return all_divs.text
    except AttributeError:
        return 0


def enterDay():
    day = input("Enter which day: ")
    try:
        if day == "exit":
            return "exit"
        if ((int(day) > 30) or (int(day) < 0)):
            return 0
        else:
            return int(day)
    except ValueError:
        return 0


def enterType():
    print(f"1. New word 2. Wrong word 3.Research word(Preparing Service)")
    print(f"---------------------------------------------")
    answer = input("Enter which type: ")
    print(f"---------------------------------------------")
    try:
        if answer == "exit":
            return "exit"
        if (int(answer) == 1) or (int(answer) == 2) or (int(answer) == 3):
            return int(answer)
        else:
            return 0
    except ValueError:
        return 0


def make_problem(data, day):
    day = int(day - 1)
    day, word_list = data[day].__get__()

    problems = Words(day)
    num_random = np.random.randint(1, len(word_list) - 1, 30)

    for node in word_list:
        numbering, name, mean = node.__get__()

        if int(numbering) in num_random:
            problems.add(numbering, name, mean)

    return problems


def process_txt_v2(data):
    data = data.split('\n')
    for i in range(len(data) - 1):
        data[i] = data[i].split(',')[1:]
    data = data[:-2]

    # Day categorizing
    # {day(type: int): word(number, name, mean), ...}
    data_edit = {}
    for value_list in data:
        if not int(value_list[0].replace(" ", "")) in data_edit.keys():
            data_edit[int(value_list[0])] = []
            data_edit[int(value_list[0])].append(value_list[1:])
        else:
            data_edit[int(value_list[0])].append(value_list[1:])
    # print(data_edit[1])
    words = []
    for key in data_edit.keys():
        words_day = Words(key)

        data_list = data_edit[key]
        for data_node in data_list:
            words_day.add(data_node[0], data_node[1], data_node[2])

        words.append(words_day)

    # words =  [ Word(day_1), Word(day_2) ... , Word(day_30) ]

    # # Debug
    # for word_list in words:
    #     word_list.print_answer()

    return words


def save_problem(data_list, problems):
    weight = 1
    data_list.append([problems, weight])


def test_problem(data):
    day, word_list = data.__get__()

    print(f"--------QUIZ, DAY {day}--------")
    for val in word_list:
        print(val.name)
    print(f"---------------------------------------------")

    while True:
        ans = input("YOU KNOW ALL?(y or n): ")
        if (ans == "y") | (ans == "n"):
            break
        if ans == "exit":
            break
        else:
            print("error: wrong input")

    return ans


def processtxt(data):
    data = data.split('\n')
    for i in range(len(data) - 1):
        data[i] = data[i].split(',')

    data_dict = {}
    data_dict["index"] = []
    data_dict["day"] = []
    data_dict["numberOfWord"] = []
    data_dict["word"] = []
    data_dict["mean"] = []

    for i in range(len(data) - 1):
        data_dict["index"].append(int(data[i][0]))
        data_dict["day"].append(int(data[i][1]))
        data_dict["numberOfWord"].append(int(data[i][2]))
        data_dict["word"].append(data[i][3])
        data_dict["mean"].append(data[i][4])
    return data_dict


def saveWord(data_dict, problem_list, count):
    data_dict[count] = problem_list
    data_dict[count].append(1)


def printProblem(data_list):
    print(f"--------QUIZ, DAY {data_list[0][0]}--------")
    for val in data_list:
        print(val[1])
    print(f"---------------------------------------------")
    while (True):
        ans = input("YOU KNOW ALL?(y or n): ")
        if (ans == "y") | (ans == "n"): break
        if (ans == "exit"):
            break
        else:
            print("error: wrong input")

    return ans


def print_problems_failed(data):
    if len(data) == 0:
        return 0
    elif len(data) == 1:
        p_number = 1
    else:
        p_number = np.random.randint(1, len(data))

    problem = data[p_number][0]
    day, word_list = problem.__get__()

    print(f"--------QUIZ, DAY {day}--------")
    problem.print_test()
    print(f"---------------------------------------------")

    while True:
        ans = input("YOU KNOW ALL?(y or n): ")
        if ans == "y" | ans == "n" | ans == "exit":
            break
        else:
            print("error: wrong input")

    return ans, p_number


def printAnswer(data_list):
    print(f"--------Answer, DAY {data_list[0][0]}--------")
    for val in data_list:
        if (type(val) == int): continue
        print(f"{val[1]} -> {val[2]}")
    print(f"---------------------------------------------")


def add_word_weight(data_list, index):
    data_list[index][-1] = data_list[index][-1] + 1


def remove_problem(data_list, index):
    del data_list[index]


def subtract_word_weight(problems_failed, index):
    if problems_failed[index][-1] < 1:
        print(f"error: out of range in problem list")
    if problems_failed[index][-1] == 1:
        remove_problem(problems_failed, index)
    else:
        problems_failed[index][-1] = problems_failed[index][-1] - 1


def edit_answer(nonSolvedWord):
    while True:
        print(f"--------------Problem List---------------")
        for word in nonSolvedWord[0].wordlist:
            word.print_answer()
        print(f"-----------------------------------------")

        index_edit = input("Which number do you want? ")
        for word in nonSolvedWord[0].wordlist:
            print(word.numbering)
            if int(word.numbering) == int(index_edit):
                print(f"-------------------------------------")
                mean_edit = input("Mean you want to change: ")
                word.mean = mean_edit
                print(f"{word.numbering}, {word.name} -> {word.mean}")
                print(f"Saved")

        answer = input("Want a more editing? 1(yes) or 0(no): ")
        if int(answer) == 0:
            break
        else:
            continue


def main():
    # https://realpython.com/python-timer/
    # tic = time.perf_counter()

    nonSolvedWord = []
    f = open("./1.txt", encoding='utf-8')
    data = process_txt_v2(f.read())

    while True:
        print(f"---------------------------------------------")
        print(f"|		        GRE WORD TEST	    	    |")
        print(f"---------------------------------------------")

        current_index = 0
        problemType = enterType()

        if problemType == "exit":
            break
        if problemType == "cls" or problemType == "clear":
            os.system("cls")

        if problemType == 1:

            if len(nonSolvedWord) > 10:
                print(f"Please solve the problem...")
                problemType = 2

            day = enterDay()

            # Exit command
            if day == "exit":
                break

            # Clear command
            if problemType == "cls" or problemType == "clear":
                os.system("cls")

            # Exception Error for day 1-30
            elif not ((day > 0) and (day <= 30)):
                print(f"error: enter another day...day is from 1 to 30....")

            else:
                problems = make_problem(data, day)
                answer = test_problem(problems)
                answer = str(answer)
                if answer == 'exit':
                    break
                if answer == 'y':
                    continue
                elif answer == 'n':
                    save_problem(nonSolvedWord, problems)
                    problems.print_answer()


        elif problemType == 2:
            if len(nonSolvedWord) < 1:
                print(f"NON PROBLEM: GREAT JOB!!!")
                continue
            else:
                print("HELLO REVIEW WORLD")
                # editing...
                answer, index = print_problems_failed(nonSolvedWord)
                current_index = index
                answer = str(answer)
                if answer == 'exit':
                    break
                elif answer == 'y':
                    subtract_word_weight(nonSolvedWord, index)
                    continue
                elif answer == 'n':
                    add_word_weight(nonSolvedWord, index)
                    nonSolvedWord[index][0].print_answer()

        elif problemType == 3:
            word = input("Which word do you want to search: ")
            print(f"The meaning...{search_mean(word)}")

        else:
            print("*error: check the exception in source")

        ###

        # -ing
        while True:
            answer_next = input("Next Step?(y or n): ")

            if answer_next == "exit":
                break

            elif answer_next == "cls" or problemType == "clear":
                os.system("cls")

            elif answer_next == "y":
                break

            elif answer_next == "n":
                answer_next = input("What do you want to do?(1. edit the answer 2. next step)")
                if answer_next == "2":
                    break
                elif answer_next == "1":
                    edit_answer(nonSolvedWord[current_index])

            print("We are Waiting for U... If you want to next step, then press y")

        if answer_next == "cls" or problemType == "clear":
            os.system("cls")
        if answer_next == "exit":
            break

    # toc = time.perf_counter()
    # print(f"Process time in {toc - tic:0.4f} secondes")


if __name__ == "__main__":
    main()

# Weight
# Sorting word list
