import random
import requests
from bs4 import BeautifulSoup as bs



def display_hangman(status):
    HANGMAN_PICS = ['''
    +---+
        |
        |
        |
        ===''', '''
    +---+
    O   |
        |
        |
        ===''', '''
    +---+
    O   |
    |   |
        |
        ===''', '''
    +---+
     O  |
    /|  |
        |
        ===''', '''
    +---+
     O  |
    /|\ |
        |
        ===''', '''
    +---+
     O  |
    /|\ |
    /   |
        ===''', '''
    +---+
     O  |
    /|\ |
    / \ |
        ===''']
    return HANGMAN_PICS[status]


URL = "https://www.enchantedlearning.com/wordlist/sports.shtml"
r = requests.get(URL)
soup = bs(r.content, "html.parser")
soup.prettify()

word_list_item = soup.find_all("div", {"class":"wordlist-item"})


words = [item.get_text() for item in word_list_item]

def get_word():
    word_to_guess = random.choice(words)
    return word_to_guess.upper()


def play(word):
    words_guessed = []
    hangman_status = 0
    guessed = False
    go = True
    
   
    rep = convert_letter(word)
    print(rep)
    
    while not guessed and hangman_status >= 0:
        print(display_hangman(hangman_status))
        answer = input("Please enter a letter: ").upper()
        print("\n")
        if answer == "":
            print("Please enter a word.")
            print(rep)
        if answer in words_guessed and answer != "":
            print("You already picked that word. Please try again.")
            print(rep)
        if answer not in word:
            words_guessed.append(answer)
            print(f"Sorry, {answer} is not in the word. Please try again")
            print("\n")
            hangman_status += 1
            print(rep)
            print("\n")
            if hangman_status == 6:
                print(display_hangman(6))
                print(f"I\'m sorry, you ran out of lives. The word was {word}")
                print("\n")
                guessed = True
        if answer in word and answer not in words_guessed:
            words_guessed.append(answer)
            print(f"{answer} was in the word!")
        
            print("\n")
            word_as_list = list(rep)
            indices = [i for i, letter in enumerate(word) if letter == answer]
            for index in indices:
                word_as_list[index] = answer


            word_completion = "".join(word_as_list)
            rep = word_completion
            print(rep)

            if "_" not in word_completion:
                
                print("You Won!")
                print(f"Total won: {wins}")
                print("\n")
                guessed = True
             

def main():
    word = get_word()
    play(word)
    while input("Do you wanna play again? (Y|N): ").upper() == "Y":
        word = get_word()
        play(word)
    print("Thanks for playing!!")
   


if __name__ == '__main__':
    main()
