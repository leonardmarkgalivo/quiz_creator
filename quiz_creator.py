import tkinter as tk
from tkinter import messagebox
import random

#UI Helpers 
def labeled_entry(container, label_text):
    tk.Label(container, text=label_text, font=("Arial", 12), bg="#f0f0f0").pack(pady=2)
    entry = tk.Entry(container, width=50, font=("Arial", 12))
    entry.pack(pady=2)
    return entry

def styled_button(container, text, command, bg="#4CAF50"):
    return tk.Button(container, text=text, command=command, font=("Arial", 12), bg=bg, fg="white", relief="raised")

#Data Loader
def load_quiz_data():
    try:
        with open("quiz_data.txt", "r") as file:
            blocks = file.read().split("-" * 40 + "\n")
        questions = []
        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) >= 6:
                q = lines[0][10:]
                choices = {k: lines[i][3:] for i, k in enumerate(['a', 'b', 'c', 'd'], start=1)}
                answer = lines[5][-1]
                questions.append((q, choices, answer))
        return questions
    except FileNotFoundError:
        return None

#Quiz Creator Window 
def open_quiz_creator():
    creator = tk.Toplevel()
    creator.title("Quiz Creator")
    creator.geometry("500x500")
    creator.configure(bg="#f0f0f0")

    entry_question = labeled_entry(creator, "Enter your question:")
    entry_a = labeled_entry(creator, "Choice a:")
    entry_b = labeled_entry(creator, "Choice b:")
    entry_c = labeled_entry(creator, "Choice c:")
    entry_d = labeled_entry(creator, "Choice d:")
    entry_correct = labeled_entry(creator, "Correct answer (a/b/c/d):")

    def save_question():
        question = entry_question.get().strip()
        choices = [entry_a.get().strip(), entry_b.get().strip(), entry_c.get().strip(), entry_d.get().strip()]
        correct = entry_correct.get().strip().lower()

        if not question or any(c == '' for c in choices) or correct not in ['a', 'b', 'c', 'd']:
            messagebox.showwarning("Incomplete", "Fill in all fields and use a, b, c, or d as the correct answer.")
            return

        with open("quiz_data.txt", "a") as file:
            file.write(f"Question: {question}\n")
            file.write(f"a. {choices[0]}\n")
            file.write(f"b. {choices[1]}\n")
            file.write(f"c. {choices[2]}\n")
            file.write(f"d. {choices[3]}\n")
            file.write(f"Correct answer: {correct}\n")
            file.write("-" * 40 + "\n")

        messagebox.showinfo("Saved", "Question saved!")
        for entry in [entry_question, entry_a, entry_b, entry_c, entry_d, entry_correct]:
            entry.delete(0, tk.END)

    styled_button(creator, "Save Question", save_question).pack(pady=10)
    styled_button(creator, "Back to Menu", creator.destroy, bg="#f44336").pack(pady=10)

#Quiz Taker Window
def open_quiz_taker():
    taker = tk.Toplevel()
    taker.title("Take the Quiz")
    taker.geometry("500x400")
    taker.configure(bg="#f0f0f0")

    questions = load_quiz_data()
    if not questions:
        tk.Label(taker, text="No questions found or file missing.", font=("Arial", 14), bg="#f0f0f0").pack(pady=20)
        return

    random.shuffle(questions)
    current_index = tk.IntVar(value=0)
    score = tk.IntVar(value=0)

    def show_question():
        for widget in taker.winfo_children():
            widget.destroy()

        if current_index.get() < len(questions):
            question_text, choices, correct_answer = questions[current_index.get()]

            tk.Label(taker, text=f"Q{current_index.get()+1}: {question_text}", font=("Arial", 14), wraplength=400, bg="#f0f0f0").pack(pady=10)

            answer_var = tk.StringVar(value="")
            for key in ['a', 'b', 'c', 'd']:
                tk.Radiobutton(taker, text=f"{key}. {choices[key]}", variable=answer_var, value=key,
                               anchor="w", justify="left", bg="#f0f0f0", font=("Arial", 12)).pack(fill="x", padx=20, pady=2)

            def submit_answer():
                selected = answer_var.get()
                if not selected:
                    messagebox.showwarning("No Answer", "Please select an answer.")
                    return

                if selected == correct_answer:
                    score.set(score.get() + 1)
                    messagebox.showinfo("Result", "Correct!")
                else:
                    messagebox.showerror("Result", f"Wrong! Correct answer was: {correct_answer}")

                current_index.set(current_index.get() + 1)
                taker.after(500, show_question)

            styled_button(taker, "Submit", submit_answer).pack(pady=10)

        else:
            tk.Label(taker, text="Quiz Complete!", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
            tk.Label(taker, text=f"Your Score: {score.get()} out of {len(questions)}", font=("Arial", 14), bg="#f0f0f0").pack()
            styled_button(taker, "Back to Menu", taker.destroy, bg="#f44336").pack(pady=10)

    show_question()

#Main Window 
def main():
    root = tk.Tk()
    root.title("Quiz App Start Menu")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")

    tk.Label(root, text="Welcome to the Quiz App", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
    styled_button(root, "Create Quiz", open_quiz_creator).pack(pady=10)
    styled_button(root, "Take Quiz", open_quiz_taker).pack(pady=10)

    root.mainloop()

main()
