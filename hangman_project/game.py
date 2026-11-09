class HangmanGame:
    def init(self, word: str):
        """Inicializa los atributos del juego según los requerimientos."""
        self.word = word.lower()
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self) -> str:
        """Muestra el estado actual de la palabra con guiones bajos y letras adivinadas."""
        progress = []
        for char in self.word:
            if char in self.guessedletters or not char.isalpha():
                progress.append(f"{char} ")
            else:
                progress.append(" ")
        return "".join(progress)

    def process_guess(self, letter: str) -> bool:
        """Procesa la letra adivinada por el usuario."""
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.errors +=1
            return False

    def is_won(self) -> bool:
        win = True
        index = 0
        while win and index < len(self.word):
            if self.word[index] not in self.guessed_letters:
                win = False
            index += 1
        return win

    def is_lost(self) -> bool:
        if self.errors == self.max_errors:
            return True
        else:
            return False
