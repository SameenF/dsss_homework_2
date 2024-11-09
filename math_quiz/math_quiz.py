import random

def random_int(min, max):
    """
    Generate a random integer between min and max (inclusive).

    Args:
    min (int): The lower bound of the random integer.
    max (int): The upper bound of the random integer.

    Returns:
    int: A random integer between min and max.
    """
    return random.randint(min, max)

def random_operator():
    """
    Select a random operator from the list of possible operators: '+', '-', or '*'.

    Returns:
    str: A randomly selected operator.
    """
    return random.choice(['+', '-', '*'])

def calculate(n1, n2, operator):
    """
    Calculate the result of applying the given operator on n1 and n2.

    Args:
    n1 (int): The first number.
    n2 (int): The second number.
    operator (str): The operator to apply ('+', '-', or '*').

    Returns:
    tuple: A tuple containing the problem as a string and the result as an integer.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    else:
        result = n1 * n2
    return problem, result

def math_quiz():
    """
    Run the math quiz game where the player answers random math questions.
    """
    score = 0
    total_questions = 3 # Number of questions in the quiz, should be an integer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the number of questions
    for _ in range(total_questions):
        # Generate two random integers and a random operator
        num1 = random_int(1, 10);
        num2 = random_int(1, 5); # Adjusted to avoid non-integer n2 values
        operator = random_operator()

        # Compute the correct result for the question
        PROBLEM, ANSWER = calculate(num1, num2, operator)

        # Display the problem to the user
        print(f"\nQuestion: {PROBLEM}")

        try:
            # Get user's answer and check if it is valid
            user_answer = int(input("Your answer: "))

            # Check if the answer is correct
            if user_answer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")

        except ValueError:
            # Handle invalid input (non-integer answers)
            print("Invalid input! Please enter a valid integer answer.")


    print(f"\nGame over! Your average score is: {score} // {total_questions} = {score / total_questions}")

if __name__ == "__main__":
    math_quiz()
