import tkinter as tk
from tkinter import messagebox
import random

# --- Quiz Creator Window ---
def open_quiz_creator():
    creator_window = tk.Toplevel()
    creator_window.title("Quiz Creator")
    creator_window.geometry("500x500")
    creator_window.configure(bg="#f0f0f0")  # Set background color

    tk.Label(creator_window, text="Enter your question:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    entry_question = tk.Entry(creator_window, width=50, font=("Arial", 12))
    entry_question.pack(pady=5)

    tk.Label(creator_window, text="Choice a:", font=("Arial", 12), bg="#f0f0f0").pack()
    entry_a = tk.Entry(creator_window, width=50, font=("Arial", 12))
    entry_a.pack(pady=5)

    tk.Label(creator_window, text="Choice b:", font=("Arial", 12), bg="#f0f0f0").pack()
    entry_b = tk.Entry(creator_window, width=50, font=("Arial", 12))
    entry_b.pack(pady=5)

    tk.Label(creator_window, text="Choice c:", font=("Arial", 12), bg="#f0f0f0").pack()
    entry_c = tk.Entry(creator_window, width=50, font=("Arial", 12))
    entry_c.pack(pady=5)

    tk.Label(creator_window, text="Choice d:", font=("Arial", 12), bg="#f0f0f0").pack()
    entry_d = tk.Entry(creator_window, width=50, font=("Arial", 12))
    entry_d.pack(pady=5)

    tk.Label(creator_window, text="Correct answer (a/b/c/d):", font=("Arial", 12), bg="#f0f0f0").pack()
    entry_correct = tk.Entry(creator_window, width=50, font=("Arial", 12))
    entry_correct.pack(pady=5)

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

        # Clear entry fields
        entry_question.delete(0, tk.END)
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)
        entry_d.delete(0, tk.END)
        entry_correct.delete(0, tk.END)

    # Save Button with custom style
    tk.Button(creator_window, text="Save Question", command=save_question, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised").pack(pady=10)

    # Back to Main Menu Button with custom style
    def back_to_menu():
        creator_window.destroy()

    tk.Button(creator_window, text="Back to Menu", command=back_to_menu, font=("Arial", 12), bg="#f44336", fg="white", relief="raised").pack(pady=10)

# --- Quiz Taker Window ---
def open_quiz_taker():
    quiz_window = tk.Toplevel()
    quiz_window.title("Take the Quiz")
    quiz_window.geometry("500x400")
    quiz_window.configure(bg="#f0f0f0")  # Set background color

    try:
        with open("quiz_data.txt", "r") as file:
            data = file.read().split("-" * 40 + "\n")

        # Handle case where quiz data is empty
        if not data or all(line.strip() == '' for line in data):
            tk.Label(quiz_window, text="No questions found. Please create a quiz first.", font=("Arial", 14), bg="#f0f0f0").pack(pady=20)
            return

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

        # Shuffle questions
        random.shuffle(questions)
        current_index = tk.IntVar(value=0)
        score = tk.IntVar(value=0)

        def show_question():
            for widget in quiz_window.winfo_children():
                widget.destroy()

            if current_index.get() < len(questions):
                question_text, choices, correct_answer = questions[current_index.get()]

                tk.Label(quiz_window, text=f"Q{current_index.get() + 1}: {question_text}",
                         wraplength=400, font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

                answer_var = tk.StringVar(value="")  # Reset variable

                radio_buttons = []
                for key in ['a', 'b', 'c', 'd']:
                    rb = tk.Radiobutton(quiz_window, text=f"{key}. {choices[key]}", variable=answer_var, value=key,
                                        anchor="w", justify="left", bg="white", indicatoron=True, font=("Arial", 12))
                    rb.pack(fill="x", padx=20, pady=2)
                    radio_buttons.append(rb)

                submit_button = tk.Button(quiz_window, text="Submit", font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised")
                submit_button.pack(pady=20)

                def submit_answer():
                    selected = answer_var.get()
                    if selected == "":
                        messagebox.showwarning("No Answer", "Please select an answer.")
                        return

                    # Disable further input
                    submit_button.config(state="disabled")
                    for rb in radio_buttons:
                        rb.config(state="disabled")

                    if selected == correct_answer:
                        score.set(score.get() + 1)
                        messagebox.showinfo("Result", "Correct!")
                    else:
                        messagebox.showerror("Result", f"Wrong! Correct answer was: {correct_answer}")

                    # Advance after 1 second
                    quiz_window.after(1000, lambda: current_index.set(current_index.get() + 1))
                    quiz_window.after(1100, show_question)

                submit_button.config(command=submit_answer)

            else:
                tk.Label(quiz_window, text="Quiz Complete!", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
                tk.Label(quiz_window, text=f"Your Score: {score.get()} out of {len(questions)}",
                         font=("Arial", 14), bg="#f0f0f0").pack()

                # Back to Main Menu Button with custom style
                def back_to_menu():
                    quiz_window.destroy()

                tk.Button(quiz_window, text="Back to Menu", command=back_to_menu, font=("Arial", 12), bg="#f44336", fg="white", relief="raised").pack(pady=10)

        show_question()

    except FileNotFoundError:
        tk.Label(quiz_window, text="quiz_data.txt not found!", font=("Arial", 14), bg="#f0f0f0").pack(pady=20)

# --- Main Start Menu ---
def main():
    window = tk.Tk()
    window.title("Quiz App Start Menu")
    window.geometry("400x300")
    window.configure(bg="#f0f0f0")  # Set background color

    tk.Label(window, text="Welcome to the Quiz App", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)

    tk.Button(window, text="Create Quiz", width=20, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", command=open_quiz_creator).pack(pady=10)
    tk.Button(window, text="Take Quiz", width=20, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", command=open_quiz_taker).pack(pady=10)

    window.mainloop()

main()
