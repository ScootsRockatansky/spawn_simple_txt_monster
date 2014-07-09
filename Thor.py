cmd = raw_input("Please Enter Command")

while cmd != "quit":
    istr = raw_input("You walk by a monster!  What will you do?")

    if istr == "attack":
        print("You dealt with the monster and continue on")

    elif istr == "run":
        print('''The monster chases you down in its infinite stamina while you tire.
          It catches up to you then slowly, painfully devours you until you die a tortured death.''')

    else:
        print("Your button mashing has saved your life.")

        cmd = raw_input("Play Again?")

