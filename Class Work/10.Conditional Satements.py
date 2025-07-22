hrs,mins= list(map(int,input("Enter the HH:MM : ").split(":")))

if hrs>=0 and hrs<=24 and mins>=0 and mins<=60:
    if hrs>=0 and hrs<4:
        print("It's high time.Try to Sleep!")
    elif hrs>=4 and hrs<12:
        print("Good Morning. Have a nice day!")
    elif hrs>=12 and hrs<16:
        print("Good Afternoon. Have a great lunch!")
    elif hrs>=16 and hrs<20:
        print("Good Evening. Have some snacks!")
    elif hrs>=20 and hrs<24:
        print("Good Night. Sweet Dreams!")
else:
    print("Enter the proper input, Your input is invalid")
