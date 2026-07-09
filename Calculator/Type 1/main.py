from Calculation_Logic import maths_logics as logic

def options():
    '''Shows Options To The User For Terminal Run'''
    while True:
        print("1. Square")
        print("2. Check Even")
        print("3. Check Odd")
        print("4. Circumference of Circle")
        print("5. Area of Sphere")
        try:
            user_select = int(input("Choose :"))

            if user_select == 1:
                a = int(input("Enter A Number :"))
                print(logic.sq(a))

            elif user_select == 2:
                a = int(input("Enter Number To Check Even Or Not :"))
                print(logic.is_even(a))

            elif user_select == 3:
                a = int(input("Enter Number To Check Even Or Not :"))
                print(logic.is_odd(a))

            elif user_select == 4:
                a = int(input("Enter Radius :"))
                print(logic.circumference_circle(a))
                
            elif user_select == 5:
                a = int(input("Enter Radius :"))
                print(logic.area_sphere(a))
            break
        except ValueError:
            print("Enter Numbers only")
            break

if __name__ == "__main__":
    options()