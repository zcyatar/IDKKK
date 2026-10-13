def display_header():
    print("")
    print("==================================================")
    print("")
def student_info():
    name = (input("WHAT IS YOUR NAME? "))
    SCR1 = int(input("WHAT'S YOUR ASSESSMENT SCORE (1-100) 1?  "))
    SCR2 = int(input("WHAT'S YOUR ASSESSMENT SCORE (1-100) 2? "))
    SCR3 = int(input("WHAT'S YOUR ASSESSMENT SCORE (1-100) 3? "))

def eval_perm():
    avg = (SCR1 + SCR2 + SCR3) /3
    if 90 <= avg <= 100:
        print("OUTSTANDING")
    elif 85 <= avg <= 90:
        print("VERY SATISFACTORY")
    elif 80 <= avg <= 85:
        print("Satisfactory")
    elif 75 <= avg <= 80:
        print("Fairly Satisfactory")
    else:
        print("You need improvement.")
def report():
    display_header()
    student_info()
    eval_perm()
display_header()
student_info()
eval_perm()
report()