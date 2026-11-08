#!/usr/bin/env python3

# Bucle principal del juego
# TODO: Importar la clase HangmanGame e integrar la lógica principal de ejecución.

import game as game
# [ToDo] Cambiarle el nombre de useful a algo útil realmente.
import utils as useful

def startGame():
    hangman = game.HangmanGame(useful.get_random_word())
    while (hangman.errors < hangman.max_errors):
        print("------------------------------------------")
        print(f"Palabra: {hangman.word}") # Sacar
        letter = giveMeLetter()
        # Si no es una letra, no debería contar como intento.
        if len(letter) != 1 or not letter.isalpha():
            print("Carácter inválido. Intente nuevamente.")
        # En caso de que la letra ya fue acertada, se muestra su mensaje correspondiente.
        elif letter in hangman.guessed_letters:
            print("La letra ya fue adivinada.")
        # Hay que mostrar las letras incorrectas???? To Check
        hangman.process_guess(letter)
        print(f"Letras adivinadas: {', '.join(hangman.guessed_letters)}")
        print(hangman.display_progress())
        print(f"Intentos restantes: {hangman.max_errors - hangman.errors}")

def giveMeLetter():
    return input("Ingresá una letra: ")

startGame()