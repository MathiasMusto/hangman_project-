#!/usr/bin/env python3

# Bucle principal del juego
# TODO: Importar la clase HangmanGame e integrar la lógica principal de ejecución.

import game as game
# [ToDo] Cambiarle el nombre de utilsss a algo útil realmente.
import utils as utilsss

def startGame():
    hangman = game.HangmanGame(utilsss.get_random_word())
    while (hangman.errors < hangman.max_errors):
        letter = giveMeLetter()
        if len(letter) == 1 and letter.isalpha() and letter not in hangman.guessed_letters:
            print("¡Bien hecho!")
            break
        else:
            print(f"Carácter inválido.")
            hangman.errors += 1

def giveMeLetter():
    return input("Ingresá una letra: ")

startGame()