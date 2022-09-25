print('Welcome to my Quiz')

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
print("Okay, Let's Play!")

answer = input("What are two things you can never eat for breakfast? ").lower()
arr = sorted(answer.split())
arr_answer = sorted(['lunch', 'and', 'dinner'])
if arr == arr_answer:
    print("Correct! ✅")

else: 
    print("Wrong! ❌")