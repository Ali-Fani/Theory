import random
# words=['Home']
words = ['apple', 'winter', 'Home', 'thory', 'python']
random_index = random.randint(0, len(words)-1)
selected_word = words[random_index]

print(selected_word)
chances = 10
correct_guesed_words = []
wrong_guesed_words = []
while True:
    for i in range(len(selected_word)):
        if selected_word[i].lower() in correct_guesed_words:
            # print(len(selected_word))
            print(selected_word[i], end='')
            continue
        print("_ ", end='')
    print('\n')
    userInput = input("Enter a word: ")
    if userInput.isalpha() and len(userInput) < 1:
        userInput = userInput.lower()
    elif len(userInput) > 1:
        print("Enter only one Letter")
        continue
    else:
        print("Enter only one Letter")
        continue

    if userInput in wrong_guesed_words:
        print("You have Guesed This Wrong Letter Before!")
        continue
    elif userInput in correct_guesed_words:
        print("Letter Already Chosen and is correct")
        continue
    elif userInput.lower() in selected_word.lower():
        if userInput not in correct_guesed_words:
            correct_guesed_words.append(userInput)
            print("Letter is Correct")
            print(correct_guesed_words)
            notfoundAll = True
            for i in range(len(selected_word)):
                if selected_word[i].lower() not in correct_guesed_words:
                    notfoundAll = False
                    break
            if notfoundAll:
                print("You Have Won!")
                print(f"Complete Word is {selected_word}")
                print(
                    f"You have guessed Correct answer with {10-chances} wrong answers")
                break
    else:
        chances -= 1
        if userInput not in wrong_guesed_words:
            wrong_guesed_words.append(userInput)
        if chances == 0:
            print("Wrong !Game Over!")
            break
        else:
            print(f"Wrong! Chanes Remaining: {chances}")
