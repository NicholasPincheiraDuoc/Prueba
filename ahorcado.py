import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")
        
        self.words = ["metallica", "megadeth", "slayer", "ironmaiden", "pantera"]
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

        self.hangman_images = [
            "  O  ",
            " /|\\ ",
            " / \\ "
        ]
        self.current_hangman_stage = 0

        self.hangman_image_label = tk.Label(root, text="\n".join(self.hangman_images[:self.current_hangman_stage + 1]))
        self.hangman_image_label.pack()

        self.update_attempts_label()
    
    def choose_word(self):
        return random.choice(self.words)

    def display(self):
        display_word = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_ "
        return display_word

    def update_attempts_label(self):
        attempts_label = tk.Label(self.root, text=f"Intentos restantes: {self.attempts}")
        attempts_label.pack()

    def make_guess(self):
        guess = self.input_entry.get().lower()

        if guess == self.word_to_guess:
            messagebox.showinfo("Victoria", f"¡Felicidades! ¡Has adivinado la palabra: {self.word_to_guess}")
            self.restart()
            return

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
                self.current_hangman_stage += 1
                self.update_attempts_label()
                self.update_hangman_image()
                messagebox.showinfo("Incorrecto", f"¡Incorrecto! Te quedan {self.attempts} intentos.")
        else:
            if "_" not in self.display():
                messagebox.showinfo("Victoria", f"¡Felicidades! ¡Has adivinado la palabra: {self.word_to_guess}")
                self.restart()
            else:
                self.update_word_label()

        self.input_entry.delete(0, tk.END)

    def update_hangman_image(self):
        self.hangman_image_label.config(text="\n".join(self.hangman_images[:self.current_hangman_stage + 1]))

    def update_word_label(self):
        self.word_label.config(text=self.display())

    def restart(self):
        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6
        self.current_hangman_stage = 0
        self.update_word_label()
        self.update_hangman_image()
        self.update_attempts_label()

root = tk.Tk()
game = HangmanGame(root)
root.mainloop()