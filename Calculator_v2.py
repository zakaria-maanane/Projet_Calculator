import os  # Pour effacer l'écran
import time  # Pour introduire un délai
import random

# Main function to run the program
def main():
    calculator()

# Calculation history
history = []  

# Manage history
def show_history():
    if len(history) == 0:  # len sert à vérifier la longueur de l'historique
        return "No history available"
    else:
        print("\n----------------- Calculation History -----------------")
        return "\n".join(history)

def clear_history():
    history.clear()
    return "History cleared"

# Last result
last_result = None 

# Define calculation functions
def addition(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1 - number_2

def multiplication(number_1, number_2):
    return number_1 * number_2

def division(number_1, number_2):
    if number_2 != 0:
        return number_1 / number_2
    else:
        return "Division by zero is not allowed"

def square(number):
    return number ** 2

def square_root(number):
    if number >= 0:
        return number ** 0.5
    else:
        return "Square root of a negative number is not allowed"

def power(base, exponent):
    return base ** exponent

def logarithm_base10(number):
    if number > 0:
        return (number ** (1 / 10)) - 1  # Simplified logarithmic approximation
    else:
        return "Logarithm of a number <= 0 is undefined"

def factorial(number):
    if number >= 0 and number == int(number):
        result = 1
        for i in range(1, int(number) + 1):
            result *= i
        return result
    else:
        return "Factorial is only defined for positive integers"

def modulo(number_1, number_2):
    return number_1 % number_2

def floor_division(number_1, number_2):
    if number_2 != 0:
        return number_1 // number_2
    else:
        return "Floor division by zero is not allowed"

def absolute_value(number):
    return number if number >= 0 else -number

def sine(number):
    return round(sum((-1) ** k * (number ** (2 * k + 1)) / factorial(2 * k + 1) for k in range(10)), 6)

def cosine(number):
    return round(sum((-1) ** k * (number ** (2 * k)) / factorial(2 * k) for k in range(10)), 6)

def tangent(number):
    try:
        return sine(number) / cosine(number)
    except ZeroDivisionError:
        return "Undefined tangent"

# Math quiz
def math_quiz():
    print("\nBienvenue dans le jeu de questions-réponses mathématiques!")
    print("Répondez correctement aux questions pour gagner des points.")
    print("Tapez 'exit' pour quitter le jeu.\n")

    score = 0

    while True:
        question_type = random.choice(['multiplication', 'square_root'])

        if question_type == 'multiplication':
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            correct_answer = num1 * num2
            question = f"Combien font {num1} x {num2} ? "

        elif question_type == 'square_root':
            num = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
            correct_answer = int(num ** 0.5)
            question = f"Quelle est la racine carrée de {num} ? "

        user_input = input(question)

        if user_input.lower() == 'exit':
            print(f"\nMerci d'avoir joué ! Votre score final est de {score} point(s).")
            break

        try:
            user_answer = int(user_input)
            if user_answer == correct_answer:
                print("Bonne réponse ! +1 point.\n")
                score += 1
            else:
                print(f"Mauvaise réponse. La bonne réponse était {correct_answer}.\n")
        except ValueError:
            print("Veuillez entrer un nombre valide ou 'exit' pour quitter.\n")

    print("Au revoir et à bientôt pour un autre quiz !")

# Display options menu
def menu():
    print("""\r
---------------------- Welcome to the Calculator -------------------
Choose an operation:
 1. Addition        2. Subtraction     3. Multiplication   4. Division
 5. Square          6. Square Root     7. Power            8. Logarithm (base 10)
 9. Factorial       10. Modulo        11. Floor Division   12. Absolute Value
13. Sine           14. Cosine        15. Tangent           16. Show History
17. Clear History  18. Exit          J. Math Quiz
""")

# Calculator function
def calculator():
    global last_result  # Use global variable for last result
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Effacer l'écran apres chaque itération ( mais le menu reste)
        menu()
        choice = input("\rEnter your choice: ")

        try:
            if choice in ['1', '2', '3', '4', '7', '10', '11']:
                if last_result is not None:
                    use_last_result = input("\rUse the last result? (y/n): ").lower()
                    if use_last_result == 'y':
                        number_1 = last_result
                    else:
                        number_1 = float(input("Enter the first number: "))
                else:
                    number_1 = float(input("Enter the first number: "))

                number_2 = float(input("Enter the second number: "))

                operations = {
                    '1': (addition, "+"),
                    '2': (subtraction, "-"),
                    '3': (multiplication, "*"),
                    '4': (division, "/"),
                    '7': (power, "^"),
                    '10': (modulo, "%"),
                    '11': (floor_division, "//")
                }
                operation, symbol = operations[choice]
                
                result = operation(number_1, number_2)

                print(f"{number_1} {symbol} {number_2} = {result}")
                history.append(f"{number_1} {symbol} {number_2} = {result}")
                last_result = result

            elif choice in ['5', '6', '8', '9', '12', '13', '14', '15']:
                if last_result is not None:
                    use_last_result = input("Use the last result? (y/n): ").lower()
                    if use_last_result == 'y':
                        number = last_result
                    else:
                        number = float(input("Enter a number: "))
                else:
                    number = float(input("Enter a number: "))

                if choice == '5':
                    result = square(number)
                    print(f"Square of {number} = {result}")
                elif choice == '6':
                    result = square_root(number)
                    print(f"Square root of {number} = {result}")
                elif choice == '8':
                    result = logarithm_base10(number)
                    print(f"Logarithm (base 10) of {number} = {result}")
                elif choice == '9':
                    result = factorial(number)
                    print(f"Factorial of {number} = {result}")
                elif choice == '12':
                    result = absolute_value(number)
                    print(f"Absolute value of {number} = {result}")
                elif choice == '13':
                    result = sine(number)
                    print(f"Sine of {number} degrees = {result}")
                elif choice == '14':
                    result = cosine(number)
                    print(f"Cosine of {number} degrees = {result}")
                elif choice == '15':
                    result = tangent(number)
                    print(f"Tangent of {number} degrees = {result}")

                history.append(f"Result: {result}")
                last_result = result

            elif choice == '16':
                print(show_history())

            elif choice == '17':
                print(clear_history())
                last_result = None
            
            elif choice == 'J':
                math_quiz()

            elif choice == '18':
                print("--------------- Thank you for using the calculator ---------------")
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Invalid input, please enter a number.")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(6)  # Délai de 6 secondes avant de passer au suivant
        os.system('cls' if os.name == 'nt' else 'clear')  # Effacer l'écran après le délai

# Run the main function
if __name__ == "__main__":
    main()
