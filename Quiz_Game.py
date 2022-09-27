print('Welcome to my Quiz')

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
print("Okay, Let's Play!")
score = 0

answer1 = input("What are two things you can never eat for breakfast? ").lower()
arr = sorted(answer1.split())
arr_answer = sorted(['lunch', 'and', 'dinner'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer2 = input("If you had only one match and entered a dark room containing an oil lamp, some kindling wood, and a newspaper, which would you light first? ").lower()
arr = sorted(answer2.split())
arr_answer = sorted(['a', 'match'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer3 = input("I’m so fragile that if you say my name, you’ll break me. What am I? ").lower()
arr = sorted(answer3.split())
arr_answer = sorted(['silence'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer4 = input("I have teeth but can’t eat. What am I? ").lower()
arr = sorted(answer4.split())
arr_answer = sorted(['a', 'comb'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer5 = input("What runs, but never walks. Murmurs, but never talks. Has a bed, but never sleeps. And has a mouth, but never eats? ").lower()
arr = sorted(answer5.split())
arr_answer = sorted(['a', 'river'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer6 = input("What bird can lift the most weight? ").lower()
arr = sorted(answer6.split())
arr_answer = sorted(['a', 'crane'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer7 = input("What travels the world while stuck in one spot? ").lower()
arr = sorted(answer7.split())
arr_answer = sorted(['a', 'stamp'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer8 = input("What has one eye but can’t see anything at all? ").lower()
arr = sorted(answer8.split())
arr_answer = sorted(['a', 'needle'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer9 = input("Before Mount Everest was discovered, what was the tallest mountain on Earth?  ").lower()
arr = sorted(answer9.split())
arr_answer = sorted(['mount', 'everest'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer10 = input("What occurs once in a minute, twice in a moment, and never in one thousand years? ").lower()
arr = sorted(answer10.split())
arr_answer = sorted(['the', 'letter', 'm'])
if arr == arr_answer:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

answer11 = input("A cowboy rode into town on Friday. He stayed in town for three days and rode out on Friday. How is that possible? ").lower()
arr = sorted(answer11.split())
arr_answer = (["horse", "horse's", "friday"])
y = 0
for x in arr:
    if x in arr_answer:
        y += 1
if y >= 2:
    print("Correct! ✅")
    score += 1
else: 
    print("Wrong! ❌")

print('You got ' + str((score / 11) * 100) + "% of the questions correct!")
# Figure out how to end game and a message about the amount correct out of 11

