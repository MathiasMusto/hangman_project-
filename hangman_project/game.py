class HangmanGame:
    def __init__(self, word: str):
        """Inicializa los atributos del juego según los requerimientos."""
        self.word = word.lower()
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self) -> str:
        """Muestra el estado actual de la palabra con guiones bajos y letras adivinadas."""
        progress = []
        for char in self.word:
            if char in self.guessed_letters or not char.isalpha():
                progress.append(char)
            else:
                progress.append("_")
        return "".join(progress)
