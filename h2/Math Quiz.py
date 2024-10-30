import random

def math_quiz():
    score = 0
    for _ in range(5):
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "/"])
        correct_answer = eval(f"{num1} {operator} {num2}")
        
        if operator == "/":
            correct_answer = round(correct_answer, 1)
        
        answer = float(input(f"What is {num1} {operator} {num2}? "))
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was:", correct_answer)
    
    print("You scored", score, "out of 5.")

math_quiz()
