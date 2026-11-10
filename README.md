🕹️ Hangman Game (Juego del Ahorcado)

Proyecto modular desarrollado en Python para el juego clásico del ahorcado. Está estructurado bajo una arquitectura limpia que separa la lógica de juego (motor), las utilidades/datos y el control de ejecución por consola.

📂 Estructura del Proyecto

hangman_project/
├── hangman_project/
│   ├── game.py          # Motor del juego (Clase HangmanGame)
│   ├── main.py          # Script principal / Lanzador
│   ├── utils.py         # Módulo de funciones auxiliares
│   └── wordlist.txt     # Banco de palabras
└── README.md            # Documentación del proyecto


Descripción de los archivos:

main.py (Lanzador e Interfaz): Es el punto de entrada del programa. Administra el flujo del juego, la interacción con el usuario mediante la consola (input y print), la validación de caracteres ingresados y el bucle principal.

game.py (Motor del Juego): Define la clase HangmanGame. Almacena y gestiona el estado interno de la partida (palabra secreta, letras adivinadas, lista de fallos, límite de intentos, así como la verificación de victoria o derrota).

utils.py (Utilidades): Contiene funciones auxiliares de soporte. Su función principal (get_random_word) interactúa con archivos externos para seleccionar una palabra aleatoria.

wordlist.txt (Recurso de Datos): Archivo de texto plano que contiene la lista de palabras disponibles para ser elegidas en cada partida.
