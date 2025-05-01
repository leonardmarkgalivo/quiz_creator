import tkinter as tk
from tkinter import messagebox

# Save function and file write
def save_question():
    # Get the user's input 
    question = entry_question.get().strip()
    choice_a = entry_a.get().strip()
    choice_b = entry_b.get().strip()
    choice_c = entry_c.get().strip()
    choice_d = entry_d.get().strip()
    correct = entry_correct.get().strip().lower()

    # Validate inputs
    if (question == "" or choice_a == "" or choice_b == "" or 
        choice_c == "" or choice_d == "" or correct not in ['a', 'b', 'c', 'd']):
        messagebox.showwarning("Incomplete", 
            "Fill in all fields and use a, b, c, or d as the correct answer.")
    else:
        # Write data to a file
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

# Main window setup
window = tk.Tk()
window.title("Quiz Creator")
window.geometry("500x500")

# Labels and Entry Fields
tk.Label(window, text="Enter your question:").pack(pady=5)
entry_question = tk.Entry(window, width=50)
entry_question.pack()

tk.Label(window, text="Choice a:").pack()
entry_a = tk.Entry(window, width=50)
entry_a.pack()

tk.Label(window, text="Choice b:").pack()
entry_b = tk.Entry(window, width=50)
entry_b.pack()

tk.Label(window, text="Choice c:").pack()
entry_c = tk.Entry(window, width=50)
entry_c.pack()

tk.Label(window, text="Choice d:").pack()
entry_d = tk.Entry(window, width=50)
entry_d.pack()

tk.Label(window, text="Correct answer (a/b/c/d):").pack()
entry_correct = tk.Entry(window, width=50)
entry_correct.pack()

# Save Button
tk.Button(window, text="Save Question", command=save_question).pack(pady=10)

# Main loop
window.mainloop()
