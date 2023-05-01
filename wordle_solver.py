ATTEMPTS = 6

explainer = """
This is the Wordle helper. It will help you solve the NYT wordle game.
Here is how to use it:
- Type in what you typed in the Wordle game.
    - E.g. if you wrote "adieu", write "adieu".
- If Wordle indicates that there is no A or I in the word,
but the D and U are in the secret word (just in the wrong place)
and the E is in the right place, type this in:
01021
    - 0 = gray
    - 1 = yellow
    - 2 = green
The program will find all the words that meet this criteria.
"""


def trim_dictionary(dictionary: set, guess: str, condition: str) -> set:
    pass
    # for word in dictionary:
    #     hits = 0
    #     for i in range(5):
    #         if condition[i] > 0

def play(dictionary: set) -> None:
    for i in range(ATTEMPTS):
        input1 = ""
        while len(input1) != 5:
            input1 = input("Type in your guess:")
        input2 = ""
        while len(input2) != 5:
            input2 = input("Type in the colors:")
        print(
            trim_dictionary(
                dictionary=dictionary,
                guess=input1,
                condition=input2
            )
        )
    print("Game over.")


if __name__ == "__main__":
   print(explainer)
   words = open(file="dictionary.txt", mode="r")
   dictionary = list(word[:5] for word in words)
   # print(dictionary)
   play(dictionary)