#!/usr/bin/env python3

""" Bucle principal del juego"""

import game as game
import utils as useful

def startGame():
    hangman = game.HangmanGame(useful.get_random_word())
    while (hangman.errors < hangman.max_errors):
        print("------------------------------------------")
        letter = giveMeLetter()
        """
            Si no es una letra, no debería contar como intento.
            En caso de que la letra ya fue acertada, se muestra su mensaje correspondiente y se aumentan los errores.
        """
        if len(letter) != 1 or not letter.isalpha():
            print("Carácter inválido. Intente nuevamente.")
        elif letter in hangman.guessed_letters:
            print("La letra ya fue adivinada.")
            hangman.errors += 1
            hangman.errorsList.append(letter)
        else:
            """
                Si ninguna de las dos condiciones de arriba se cumplen, entonces la letra es válida y no fue ingresada
                en la lista de letras aceptada, entonces se ejecuta el método process_guess.
            """
            hangman.process_guess(letter)
        if hangman.is_won():
            showFeedback(hangman)
            print("¡Ganaste!")
            break
        elif hangman.is_lost():
            showFeedback(hangman)
            print("Fin del juego")
            break
        else:
            showFeedback(hangman)

def giveMeLetter():
    return input("Ingresá una letra: ")

def showFeedback(hangman):
    print(f"Letras adivinadas: {', '.join(hangman.guessed_letters)}")
    print(f"Intentos incorrectos: {', '.join(hangman.errorsList)}")
    print(hangman.display_progress())
    print(f"Intentos restantes: {hangman.max_errors - hangman.errors}")

startGame()
