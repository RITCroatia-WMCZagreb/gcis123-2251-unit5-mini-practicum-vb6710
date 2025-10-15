def pi_tester():
   value_pi = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
def pi_tester():
    correct_count = 0
    for i in range(len(value_pi)):
        digit_number = i + 1
        pi_input = input("Enter digit number:" + str(digit_number) + "-th digit of pi:")

    if pi_input == value_pi[i]:
       correct_count = correct_count + 1
    else:
        print("Not correct digit!!! Correct digit is:" + value_pi[i] + ".")
        break


    
    return correct_count  

def display_score(score):
    print("Number of correct decimal digits: " + str(score))

    if score >= 0 and score <= 4:
        title = "PI Neophyte"
    elif score >= 5 and score <= 9:
        title = "PI Novice"
    elif score >= 10 and score <= 24:
        title = "PI Journeyman"
    elif score >= 25 and score <= 49:
        title = "PI Enthusiast"
    elif score >= 50 and score <= 96:
        title = "PI Connoisseur"
    elif score >= 97 and score <= 100:
        title = "PI Expert"
    else:
        title = "PI Imposter"
    print("Your title: " + title)

def main():
    score = pi_tester()
    display_score(score)

if _name_ == "_main_":
    main()