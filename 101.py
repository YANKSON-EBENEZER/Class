import random    
try:
    
    name = str(input("please enter your name: "))
    if name.isdigit():
        print(random.choice(["please enter a valid name ",
                      "please enter a name ",
                      "this is not a name"
                      ]))
    else: 
        while True:
             phone_input = input("please enter number: ")
             if phone_input.isdigit() and len(phone_input) ==10:
                 phone = phone_input
                 break
             else:
                  print("please enter a valid phone number: ")         
        print(f"please your name is {name} and your number is {phone_input} " ) 

except ValueError as err:
    print(err)