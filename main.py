import os,sys
import random
import time
import pandas as pd
import numpy as np

sys.path.append("C:/workplace/wordlist/data")
data_path = "C:/workplace/wordlist/data/"
data_name = "1.xlsx"
data_sheet = "표제어 list"
data_result = "result/result.txt"
def enterDay():
	day = input("Enter which day: ")
	if(int(day) > 30):
		print(f"error:out of range")
		return 0
	else:
		return int(day)

def makeProblem(pd_frame, day):
	numRandom = np.random.randint(1, 102, 30)
	problem_list = []
	for value in pd_frame.values:
		if(value[0] == day):
			if(value[2] in numRandom):
				problem_list.append([value[0], value[2], value[3]])
	return problem_list

def printProblem(data_list):
	print(f"--------QUIZ, DAY {data_list[0][0]:d}--------")
	for val in data_list:
		print(val[2])
	print(f"---------------------------------------------")

def main():
	#https://realpython.com/python-timer/
	tic = time.perf_counter()

	day = enterDay()
	if(day == 0):
		print(f"enter another value")

	df = pd.read_excel(data_path + data_name, sheet_name=data_sheet)
	problem_list = makeProblem(df, day)

	toc = time.perf_counter()
	print(f"Process time in {toc - tic:0.4f} secondes")

	printProblem(problem_list)

if __name__=="__main__":
	main()
