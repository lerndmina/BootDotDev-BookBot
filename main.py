bookPath = "books/frankenstein.txt"


def main():
    with open(bookPath) as file:
        text = file.read()
        words = text.split()
        letters = {}
        for word in words:
            for letter in word:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1

        print(f"--- Begin report of ${bookPath} ---")
        print(f"Total words: {len(words)}")
        for letter, count in letters.items():
            print(f"{letter}: {count}")


main()
