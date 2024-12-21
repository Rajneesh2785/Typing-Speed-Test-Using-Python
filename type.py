from time import *
import random as r


def mistake(partest, usertest):
    error = 0
    
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1 
                     
    return error


def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)


if __name__ == '__main__': 
       
    while True:        
        ck = input("Ready to Test you typing speed: yes/no : ") 
        
        if ck == "yes":             
            test = ["Lucknow blossomed into a city known for its architectural splendour and cultural diversity under the Nawabs of Awadh, especially the visionary Asaf-ud-Daula, who reigned from 1775 to 1797", "Lucknow is the capital and the largest city of the Indian state of Uttar Pradesh", "Lucknow is famous for its skilful embroidery of Chikankari"]

            test1 = r.choice(test)
            print("***** typing speed *****")
            print(test1)
            print()
            print()

            time_1 = time()
            testinput = input("Enter: ")
            time_2 = time()

            print('Speed : ', speed_time(time_1, time_2, testinput), "W/Sec")
            print("Error : ", mistake(test1, testinput))
            
        elif ck == "no":
            print("It seems like you don't want to test your typing speed. \nThankyou!")
            break
        
        else:
            print("Sorry! \nYou entered the wrong input.")