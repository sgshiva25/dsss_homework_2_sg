import random


def get_random_number(min, max):
    """
    Generate a random integer between min and max 
    """
    return random.randint(min, max)


def get_random_operator():
    ## Selects a operator from '+', '-', '*'
    return random.choice(['+', '-', '*'])


def generate_problem(num_1, num_2, oper):

    """
    Generate a math problem and its answer based on the inputs.

    Parameters:
    - num_1 (int): The first operand.
    - num_2 (int): The second operand.
    - oper (str): The operator, which can be '+', '-', or '*'.

    """
    
    problem = f"{num_1} {oper} {num_2}"
    
    if operator == '+':
        ans = num_1 + num_2
    elif operator == '-':
        ans = num_1 - num_2
    else:
        ans = num_1 * num_2
        
    return problem, ans

def math_quiz():
    """
    This function runs a maths quiz where the user answers randomly generated math problems.
    Keeps track of the score and gives feedback based on the user's input.
    """
    
    score = 0
    num_ques = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        number1 = get_random_number(1, 10)
        number2 = get_random_number(1, 5)
        operator = get_random_operator()

        PROBLEM, ANSWER = generate_problem(number1, number2, operator)
        
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = int(input("Your answer: "))
            
            # Check the user's answer and update the score
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Display the final score after the quiz
    print(f"\nGame over! Your score is: {score}/{num_ques}")

if __name__ == "__main__":
    math_quiz()
