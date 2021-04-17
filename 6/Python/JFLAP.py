def jflap(DFA):
    string = input()
    state = "q0"

    for i in range(len(string)):
        state = DFA[state][string[i]]

    if DFA[state]["accept"]:
        print("Accept")
    else:
        print("Reject")
