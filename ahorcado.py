import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")
        
        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6

        self.word_label = tk.Label(root, text=self.display())
        self.word_label.pack()

        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        self.guess_button = tk.Button(root, text="Adivinar", command=self.make_guess)
        self.guess_button.pack()

        self.restart_button = tk.Button(root, text="Reiniciar", command=self.restart)
        self.restart_button.pack()

        self.update_attempts_label()
    
    def choose_word(self):
        words = ["python", "programming", "hangman", "developer", "coding"]
        return random.choice(words)

    def display(self):
        display_word = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_ "
        return display_word

    def update_attempts_label(self):
        attempts_label = tk.Label(root, text=f"Intentos restantes: {self.attempts}")
        attempts_label.pack()

    def make_guess(self):
        guess = self.input_entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showinfo("Error", "Ingresa una única letra válida.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Advertencia", "Ya has adivinado esa letra.")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word_to_guess:
            self.attempts -= 1
            if self.attempts == 0:
                messagebox.showinfo("Perdiste", f"¡Perdiste! La palabra era: {self.word_to_guess}")
                self.restart()
            else:
                messagebox.showinfo("Incorrecto", f"¡Incorrecto! Te quedan {self.attempts} intentos.")
                self.update_attempts_label()
        else:
            if "_" not in self.display():
                messagebox.showinfo("Victoria", f"¡Felicidades! ¡Has adivinado la palabra: {self.word_to_guess}")
                self.restart()
            else:
                self.update_word_label()

        self.input_entry.delete(0, tk.END)

    def update_word_label(self):
        self.word_label.config(text=self.display())

    def restart(self):
        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6
        self.update_word_label()
        self.update_attempts_label()

root = tk.Tk()
game = HangmanGame(root)
root.mainloop()