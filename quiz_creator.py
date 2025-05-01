import tkinter as tk
from tkinter import messagebox

# --- Quiz Creator Window ---
def open_quiz_creator():
    creator_window = tk.Toplevel()
    creator_window.title("Quiz Creator")
    creator_window.geometry("500x500")

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

    tk.Button(creator_window, text="Save Question", command=save_question).pack(pady=10)

# --- Quiz Taker Window ---
def open_quiz_taker():
    quiz_window = tk.Toplevel()
    quiz_window.title("Take the Quiz")
    quiz_window.geometry("500x400")

    try:
        with open("quiz_data.txt", "r") as file:
            data = file.read().split("-" * 40 + "\n")

        questions = []
        for block in data:
            lines = block.strip().split("\n")
            if len(lines) >= 6:
                question_text = lines[0][10:]
                choices = {
                    'a': lines[1][3:],
                    'b': lines[2][3:],
                    'c': lines[3][3:],
                    'd': lines[4][3:],
                }
                correct_answer = lines[5][-1]
                questions.append((question_text, choices, correct_answer))

        if not questions:
            tk.Label(quiz_window, text="No questions found. Please create a quiz first.").pack(pady=20)
            return

        # Debug output to verify parsing
        for idx, (q, choices, correct) in enumerate(questions):
            tk.Label(quiz_window, text=f"Q{idx+1}: {q}").pack()
            for k in ['a', 'b', 'c', 'd']:
                tk.Label(quiz_window, text=f"{k}. {choices[k]}").pack()
            tk.Label(quiz_window, text=f"Correct: {correct}").pack()
            tk.Label(quiz_window, text="-"*30).pack()

    except FileNotFoundError:
        tk.Label(quiz_window, text="quiz_data.txt not found!").pack(pady=20)

# --- Main Start Menu ---
def main():
    window = tk.Tk()
    window.title("Quiz App Start Menu")
    window.geometry("400x300")

    tk.Label(window, text="Welcome to the Quiz App", font=("Arial", 16)).pack(pady=20)

    tk.Button(window, text="Create Quiz", width=20, command=open_quiz_creator).pack(pady=10)
    tk.Button(window, text="Take Quiz", width=20, command=open_quiz_taker).pack(pady=10)

    window.mainloop()

main()
