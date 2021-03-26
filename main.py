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


def makeProblem_txt(data, day):
    numRandom = np.random.randint(1, 102, 30)
    problem_list = []

    for word in data:
        index, day = word.getattr()
        print(index, day)
    # for index, dayLocal, numberofword, word, meaning in zip(data[index_day].__getattr__()):
    # 	if(numberofword in numRandom):
    # 		problem_list.append(data)
    return problem_list


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
            data_edit[int(value_list[0])] = value_list[1:]
        else:
            data_edit[int(value_list[0])].append(value_list[1:])

    word_list = []
    # for value_list in data:
    # 	print(value_list)
    # 	word = Words(int(data[i][0]), int(data[i][1]), int(data[i][2]), data[i][3], data[i][4])
    # 	wordlist.append(word)
    # [ Word(), Word() ... , Word() ]

    # Debug
    # for i in range(len(wordlist)):
    # 	index, day, numbering, name, mean = wordlist[i].__getattr__()
    # 	print(index, day, numbering, name, mean)

    return wordlist


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


def printNonSolvedWord(data_dict):
    if (len(data_dict) == 0):
        return 0
    elif (len(data_dict) == 1):
        pNumber = 1
    else:
        pNumber = np.random.randint(1, len(data_dict))

    data_list = data_dict[pNumber]

    print(f"--------QUIZ, DAY {data_list[0][0]}--------")
    for val in data_list:
        if (type(val) == int): continue
        print(val[1])
    print(f"---------------------------------------------")

    while (True):
        ans = input("YOU KNOW ALL?(y or n): ")
        if (ans == "y") | (ans == "n"): break
        if (ans == "exit"):
            break
        else:
            print("error: wrong input")

    return [ans, pNumber]


def printAnswer(data_list):
    print(f"--------Answer, DAY {data_list[0][0]}--------")
    for val in data_list:
        if (type(val) == int): continue
        print(f"{val[1]} -> {val[2]}")
    print(f"---------------------------------------------")


def addWeightWord(data_dict, index):
    data_dict[index][-1] = data_dict[index][-1] + 1


def removeWord(data_dict, index):
    del data_dict[index]


def subtractWeightWord(nonSolvedWord, index):
    if (nonSolvedWord[index][-1] == 1):
        removeWord(nonSolvedWord, index)
    else:
        nonSolvedWord[index][-1] = nonSolvedWord[index][-1] - 1


def edit_answer(nonSolvedWord):
    print(f"--------------Problem List---------------")
    for index, val in enumerate(nonSolvedWord.keys()):
        print(f"{index + 1}. DAY {nonSolvedWord[val][0][0]}")
    print(f"-----------------------------------------")

    wordtoedit = input("Which number do you want?")
    # Need to make exceptional case(if enter out of list)
    index_words = int(wordtoedit) - 1
    index_words = list(nonSolvedWord.keys())[index]
    # printAnswer(nonSolvedWord[index])
    print(nonSolvedWord[index_words])
    while (True):
        print(f"-------------------------------------")
        wordtoedit = input("What do you want to edit? ")
        indexEdit = -1
        for index, val in enumerate(nonSolvedWord[index_words][:-1]):
            if (val[1].replace(" ", "") == wordtoedit): indexEdit = index
        if (indexEdit == -1):
            print("no Word in list...Try again?(1)")
            answer = input()
            if (int(answer) == 1):
                continue
            else:
                break
        print(f"-------------------------------------")
        print(f"{nonSolvedWord[index_words][indexEdit][1]} -> {nonSolvedWord[index_words][indexEdit][2]}")
        print(f"-------------------------------------")
        print("Mean you want to change:")
        meantoedit = input()
        print(f"-------------------------------------")
        nonSolvedWord[index_words][indexEdit][2] = meantoedit
        # -ing
        print(nonSolvedWord[index_words][indexEdit])
        print("Want a more editing? 1(yes) or 0(no)")
        answer = input()
        if ((int(answer) == 0)): break


def main():
    # https://realpython.com/python-timer/
    # tic = time.perf_counter()

    nonSolvedWord = {}
    nonSolvedWord_v2 = []
    count = 1
    f = open("./1.txt", encoding='utf-8')
    data = process_txt_v2(f.read())


# while(True):
# 	print(f"---------------------------------------------")
# 	print(f"|		 GRE WORD TEST	 	    |")
# 	print(f"---------------------------------------------")
#
# 	problemType = enterType()
#
# 	if (problemType == "exit"): break
# 	if (problemType == "cls" or problemType == "clear"):os.system("cls")
#
# 	if problemType == 1:
#
# 		if len(nonSolvedWord) > 10:
# 			print(f"Please solve the probelm...")
# 			problemType = 2
#
# 		day = enterDay()
#
# 		# Exit command
# 		if (day == "exit"): break
#
# 		# Clear command
# 		if (problemType == "cls" or problemType == "clear"):os.system("cls")
#
# 		# Exception Error for day 1-30
# 		elif not((day > 0) and (day <= 30)):
# 			print(f"error: enter another day...day is from 1 to 30....")
#
# 		# Execute
# 		else:
# 			problem_list = makeProblem_txt(data, day)
# 			answer = printProblem(problem_list)
# 			answer = str(answer)
# 			if(answer=='exit'):break
# 			if(answer=='y'):continue
# 			elif(answer=='n'):
# 				saveWord(nonSolvedWord, problem_list, count)
# 				printAnswer(problem_list)
# 				count = count+1
#
# 	elif problemType == 2:
#
# 		if len(nonSolvedWord) < 1:
# 			print(f"NON PROBLEM: GREAT JOB!!!")
# 			continue
#
# 		print("HELLO REVIEW WORLD")
#
# 		ans_list = printNonSolvedWord(nonSolvedWord)
# 		answer = ans_list[0]
# 		index = ans_list[1]
# 		answer = str(answer)
# 		if (answer == 'exit'): break
# 		elif (answer == 'y'):
# 			subtractWeightWord(nonSolvedWord, index)
# 			continue
# 		elif (answer == 'n'):
# 			addWeightWord(nonSolvedWord, index)
# 			printAnswer(nonSolvedWord[index])
#
# 	elif problemType == 3:
# 		word = input("Which word do you want to search: ")
# 		print(f"The meaning...{search_mean(word)}")
# 	else:
# 		print("*error: check the exception in source")
#
# 	while(True):
# 		ansNextStep = input("Next Step?(y or n): ")
# 		if(ansNextStep == "exit"):break
# 		elif(ansNextStep == "cls" or problemType == "clear"):os.system("cls")
# 		elif(ansNextStep == "y"):break
# 		elif(ansNextStep == "n"):
# 			ansNextStep = input("What do you want to do?(1. edit the answer 2. next step)")
# 		if(ansNextStep == "2"):break
# 		elif(ansNextStep == "1"):edit_answer(nonSolvedWord)
# 		print("We are Waiting for U... If you want to next step, then press y")
#
# 	if(ansNextStep == "cls" or problemType == "clear"):os.system("cls")
# 	if(ansNextStep == "exit"):break
#
#
# # toc = time.perf_counter()
# # print(f"Process time in {toc - tic:0.4f} secondes")

if __name__ == "__main__":
    main()

# Weight
# Sorting word list
