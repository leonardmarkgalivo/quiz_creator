import tkinter as tk
from tkinter import messagebox

# --- Quiz Creator Window ---
def open_quiz_creator():
    creator_window = tk.Toplevel()
    creator_window.title("Quiz Creator")
    creator_window.geometry("500x500")

    # Labels and Entry Fields
    tk.Label(creator_window, text="Enter your question:").pack(pady=5)
    entry_question = tk.Entry(creator_window, width=50)
    entry_question.pack()

    tk.Label(creator_window, text="Choice a:").pack()
    entry_a = tk.Entry(creator_window, width=50)
    entry_a.pack()

    tk.Label(creator_window, text="Choice b:").pack()
    entry_b = tk.Entry(creator_window, width=50)
    entry_b.pack()

    tk.Label(creator_window, text="Choice c:").pack()
    entry_c = tk.Entry(creator_window, width=50)
    entry_c.pack()

    tk.Label(creator_window, text="Choice d:").pack()
    entry_d = tk.Entry(creator_window, width=50)
    entry_d.pack()

    tk.Label(creator_window, text="Correct answer (a/b/c/d):").pack()
    entry_correct = tk.Entry(creator_window, width=50)
    entry_correct.pack()

    # Save function
    def save_question():
        question = entry_question.get().strip()
        choice_a = entry_a.get().strip()
        choice_b = entry_b.get().strip()
        choice_c = entry_c.get().strip()
        choice_d = entry_d.get().strip()
        correct = entry_correct.get().strip().lower()

        if (question == "" or choice_a == "" or choice_b == "" or
            choice_c == "" or choice_d == "" or correct not in ['a', 'b', 'c', 'd']):
            messagebox.showwarning("Incomplete", "Fill in all fields and use a, b, c, or d.")
            return

        with open("quiz_data.txt", "a") as file:
            file.write("Question: " + question + "\n")
            file.write("a. " + choice_a + "\n")
            file.write("b. " + choice_b + "\n")
            file.write("c. " + choice_c + "\n")
            file.write("d. " + choice_d + "\n")
            file.write("Correct answer: " + correct + "\n")
            file.write("-" * 40 + "\n")

        messagebox.showinfo("Saved", "Question saved!")

        entry_question.delete(0, tk.END)
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)
        entry_d.delete(0, tk.END)
        entry_correct.delete(0, tk.END)

    # Save Button
    tk.Button(creator_window, text="Save Question", command=save_question).pack(pady=10)

# --- Main Start Menu ---
def main():
    window = tk.Tk()
    window.title("Quiz App Start Menu")
    window.geometry("400x300")

    tk.Label(window, text="Welcome to the Quiz App", font=("Arial", 16)).pack(pady=20)

    tk.Button(window, text="Create Quiz", width=20, command=open_quiz_creator).pack(pady=10)
    tk.Button(window, text="Take Quiz", width=20, command=lambda: None).pack(pady=10)  # Placeholder

    window.mainloop()

main()
