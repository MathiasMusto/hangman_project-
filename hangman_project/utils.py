#!/usr/bin/env python3
# Funciones auxiliares (validación de entradas, lectura de archivos, etc.)
# TODO: Implementar las funciones auxiliares que correspondan a tu parte del equipo.
import random

def get_random_word():
    wordList = []
    with open("wordlist.txt", "r") as f:
        wordList = f.readlines()
    return random.choice(wordList).strip()
c