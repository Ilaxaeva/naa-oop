choice = ''
while choice != 'q':    
    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.")
    
    choice = input("What would you like to do? ")

    if choice == '1':
        print("\nHere are the people I know.\n")
    elif choice == '2':
        print("\nI can't wait to meet this person!\n")
    elif choice == 'q':
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")