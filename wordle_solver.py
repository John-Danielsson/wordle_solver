from re import match


class WordleHelper:
    def __init__(self):
        with open("dictionary.txt", 'r') as file:
            content = file.read()
        self.dict = content.split("\n")
        self.guesses = []

    def pattern_match(self, hint, word, excluded):
        if match(hint.replace("-", "[a-z]"), word) is not None:
            return all(c not in excluded for c in word)
        return False

    def add_guess(self, word, hint):
        self.guesses.append([word, hint])

    def matches(self):
        excluded = set()
        green_letters = ["-", "-", "-", "-", "-"]
        for i in range(len(self.guesses)):
            for j in range(5):
                if self.guesses[i][1][j] == "0":
                    excluded.add(self.guesses[i][0][j])
                elif self.guesses[i][1][j] == "2":
                    green_letters[j] = self.guesses[i][0][j]
        pattern = "".join(green_letters)
        result = []
        for w in self.dict:
            if self.pattern_match(pattern, w, excluded):
                result.append(w)
        return result


if __name__ == "__main__":
    wh = WordleHelper()
    wh.add_guess("adieu", "10010")
    wh.add_guess("heart", "02200")
    wh.add_guess("beans", "02200")
    wh.add_guess("leafy", "22202")
    print(len(wh.dict))
    print(wh.matches())