
def calculate_bmi(height,weight):
    print("Value of height is: "+str(height)) #print("Value of height is: ",height)
    print("Value of weight is: "+str(weight)) #print("Value of weight is: ",weight)

    bmi=weight/(height*height)
    print("Value of bmi is: "+str(bmi))

    

    if bmi_output < 18.5:
        print("Under Weight")
    elif bmi_output >=18.5 and bmi_output < 24.9:
        print("Normal Weight")
    else:
        print("Over Weight")
    return bmi

bmi_output = calculate_bmi(weight=54,height=1.60)
print("BMI output is: ",bmi_output)

def display_main_menu():
    print("display main menu")

def get_user_input():
    print("user input")

def main():
    print("ET0735 (DevOps for AIoT) Lab 2 - Introduction to Python")
    display_main_menu()
    num_list=get_user_input
