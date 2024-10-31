
import random


def welcome_message():
    print("Welcome to the Quiz game!")
    print("You will be asked a series of questions. Each question you answer is worth one point.")


def get_user_consent():
    answer = input("Do you want to play this game? ").lower()
    if answer != "yes":
        print("Hopefully, next time. Goodbye!")
        quit()
    else:
        print("Enjoy!")


def ask_question(question):
    return input(question).lower()


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def continue_game_prompt():
    response = input("Do you want to continue playing or quit? (yes to continue, no to quit): ").lower()
    if response != "yes":
        print("Thank you for playing!")
        quit()


def game_loop(questions):
    score = 0
    answered_count = 0
    asked_questions = set()

    while len(asked_questions) < len(questions):
        # Select a random question that hasn't been asked yet
        random_question = random.choice(questions)
        if random_question["question"] in asked_questions:
            continue  # Skip if already asked

        user_answer = ask_question(random_question["question"])
        answered_count += 1
        asked_questions.add(random_question["question"])

        if check_answer(user_answer, random_question["answer"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            score -= 1

        print(f"Your score is {score}")

        # Check if it's time to ask the player if they want to continue
        if answered_count % 3 == 0:
            continue_game_prompt()

    print("You have answered all the questions!")
    print(f"Your final score is {score}")


def main():
    welcome_message()
    get_user_consent()

    questions = [
        {"question": "What does CPU stand for?", "answer": "central processing unit"},
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "william shakespeare"},
        {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
        {"question": "What is the chemical symbol for water?", "answer": "h2o"},
        {"question": "How many continents are there on Earth?", "answer": "seven"},
        {"question": "Who painted the Mona Lisa?", "answer": "leonardo da vinci"}
    ]

    game_loop(questions)


if __name__ == "__main__":
    main()
