name = input("what's your name?")
while name.isalpha() != True :
    print('enter a string , please')
    name = input("what's your name?")

age = input("How old are you?")
while age.isdigit() != True :
    print('enter an iteger , please')
    age = input("How old are you?")

adress = input('where do you live?')
while adress.isalpha() != True :
    print('enter a string , please')
    adress = input("what's your adress?")

print("Hello Mr/Ms",name,"age",age,"located in",adress,)
print("thanks for beening one of our community, \t enjoy ")


