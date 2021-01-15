import pprint
import re
from random import shuffle
import random
answers = {"1": "D", "2": "C", "3": "C", "4": "A", "5": "C", "6": "A", "7": "D", "8": "A", "9": "D", "10": "A", "11": "C", "12": " B", "13": "D", "14": "D", "15": "B", "16": "D", "17": "B", "18": "B", "19": "B", "20": "C", "21": "C", "22": "D", "23": "C", "24": "A", "25": "D", "26": "D", "27": "B", "28": "A", "29": "D", "30": "D", "31": "B", "32": "D", "33": "B", "34": "D", "35": "B", "36": "C", "37": " A", "38": "A", "39": " C", "40": "D", "41": "A", "42": "B", "43": "B", "44": "D", "45": "C", "46": "D", "47": "A", "48": "C", "49": "B", "50": "C", "51": "A", "52": "D", "53": "D", "54": "B", "55": "C", "56": "A", "57": "D", "58": "A", "59": " B", "60": "C"}
print("Quiz App Using Python")
print("*"*50)

def main():
    score = 0
    user = input("Enter your name :")
    confirm = input("Start Quiz : Y/N")
    if confirm.upper() == "Y":
        print(f"Welcome {user}")
        q = pick_questions("pro-t.txt")

        for _q in q:
            print(_q)
            answer = input("Enter your choice :")
            if answer.upper() not in ["A","B","C","D"]:
                print("Please select from available options.")
            else:
                question_number = re.findall('\d+',_q)[0]
                if answer == answers[question_number]:
                    print("Correct Answer!")
                    score =score+1
                    print("Your Score: ",score)
                else:
                    print("Wrong answer!")
                    score = score - .25
                    print("Your Score: ",score)
        print("You have completed the Quiz! Your Final Score is ",score)
        
    elif confirm.upper() == "N":
        print("Hope to see you later! {user}")
    else:
        print("Invalid key pressed!")
        

def get_question(file):
    file =  open(file)
    q = file.readlines()
    r_q = random.choice(q)
    return r_q

def pick_questions(fname):
    question_list = []
    for question in open(fname):
        question_list.append(question)
    return random.sample(question_list,20)

main()