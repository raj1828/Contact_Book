names = []
phone_numbers = []

while True:
    print('\n Choose an Option'
            '\n 1. Add Contact'
            '\n 2. Search Contact'
            '\n 3. View All Contact'
            '\n q for Quit')
    choice = input("Enter The Option : ")

    if choice == '1':
        print("You choose One")

        name = input("Enter Name Of Contact : ")
        phone_number = input("Enter Phone Number : ")

        names.append(name)
        phone_numbers.append(phone_number)

        print("Contact Added Successfully!!!!")
    
    elif choice == '2':
        print("You choose two")

        search = input("Enter The Name : ")

        print("Search Result: \n")
        if search in names:
            index = names.index(search);
            phone_number = phone_numbers[index]

            print("Name : {}, Phone Number : {}".format(search,phone_number))

        else:
            print("No Result Founnd :(")
    
    elif choice == '3':
        print("You Choose 3")

        print("\nName\t\t\tPhone Number\n")
        for x in range (len(names)):
            print("{}\t\t\t{}".format(names[x], phone_numbers[x]))
    
    elif choice == 'q':
        break

    else:
        print("Invalid Choice")