########################################
# Name: Anna Bikle
# Collaborators (if any): Quad center,  Connor
# GenAI Transcript (if any):
# Estimated time spent (hr): 12 hours
# Description of any added extensions: Makes keyboard fun colors (spaced themed) when game is won
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * #ENGLISH_WORDS, is_english_word
import random

#Picks hidden word
HIDDEN_WORD = random.choice(ENGLISH_WORDS).upper()

while len(HIDDEN_WORD) != 5: #Makes hidden word 5 letters
    HIDDEN_WORD = random.choice(ENGLISH_WORDS).upper()

print(f"Hidden Word: {HIDDEN_WORD}")

key_colors = {}

def wordle(): # The main function to play the Wordle game

    def space(): #Extension to make keyboard space themed when win
        letterss = "abcdefghijklmnopqrstuvwxyz"
        colors = ["#1d1135", "#0c164f", "#ba1e68", "#5643fd", "#7649fe", "#114499"]
        for i in range(len(letterss)):
            gw.set_key_color(letterss[i], colors[i%6])
                            
    def update_key_color(letter, new_color): #Changes keyboard colors during the game
        current_color = key_colors.get(letter, UNKNOWN_COLOR)
        if current_color == CORRECT_COLOR:
            return
        if current_color == PRESENT_COLOR and new_color == MISSING_COLOR:
            return
        gw.set_key_color(letter, new_color)
        key_colors[letter] = new_color
        
    def enter_action(): # What should happen when RETURN/ENTER is pressed.
        guess = ""
        row = gw.get_current_row()
        for i in range(5):
            guess += gw.get_square_letter(row, i)
        guess = guess.lower()
        print(f"Guessed Word: {guess.upper()}")

        if len(guess) != 5:
            gw.show_message("Word not long enough :(")
            return

        if guess in ENGLISH_WORDS: #If word is in the word list
            remaining_hidden_letters = list(HIDDEN_WORD)
            correct_positions = [False] * 5
            for i in range(5): #Colors correct letters in the correct spot
                if guess[i].upper() == HIDDEN_WORD[i]:
                    gw.set_square_color(row, i, CORRECT_COLOR)
                    correct_positions[i] = True
                    remaining_hidden_letters[i] = None
                    update_key_color(guess[i].upper(), CORRECT_COLOR)
                    
            for i in range(5): #Colors correct letters in the incorrect spot
                if not correct_positions[i]:
                    if guess[i].upper() in remaining_hidden_letters:
                        gw.set_square_color(row, i, PRESENT_COLOR)
                        remaining_hidden_letters[remaining_hidden_letters.index(guess[i].upper())] = None
                        update_key_color(guess[i].upper(), PRESENT_COLOR)
                    else: #Colors incorrect letters
                        gw.set_square_color(row, i, MISSING_COLOR)
                        update_key_color(guess[i].upper(), MISSING_COLOR)
                        
            if guess.upper() == HIDDEN_WORD: #What happens when guess is correct
                gw.show_message("Wooww, Very nice! Correct")
                gw.set_current_row(N_ROWS)
                space()
                return
            else: #What happens when guess is incorrect
                if row + 1 < N_ROWS:
                    gw.set_current_row(row + 1)
                else: #What happens when guesses run out
                    gw.show_message(f"Wrong :( word the correct word was {HIDDEN_WORD}.")
                    gw.set_current_row(N_ROWS)
        else: #If word is not in the word list
            gw.show_message("Not a real word!")
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Milestone 0:
#    gw.set_square_letter(0,0,'p')
#    gw.set_square_letter(0,1,'l')
#    gw.set_square_letter(0,2,'a')
#    gw.set_square_letter(0,3,'n')
#    gw.set_square_letter(0,4,'e')

# Startup boilerplate
if __name__ == "__main__":
    wordle()