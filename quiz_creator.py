import tkinter as tk

#Added save function and file write
def save_question():
    question = entry_question.get()
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    d = entry_d.get()
    correct = entry_correct.get().strip().lower()

    if question == "" or a == "" or b == "" or c == "" or d == "" or correct not in ['a', 'b', 'c', 'd']:
        messagebox.showwarning("Incomplete", "All fields must be filled and correct")
    else:
        with open("quiz_data.txt", "a") as file:
            file.write("Question: " + question + "\n")
            file.write("a. " + a + "\n")
            file.write("b. " + b + "\n")
            file.write("c. " + c + "\n")
            file.write("d. " + d + "\n")
            file.write("Correct answer: " + correct + "\n")
            file.write("-" * 40 + "\n")

        messagebox.showinfo("Saved", "Question saved!")

        #Clear entry field
        entry_question.delete(0, tk.END)
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)
        entry_d.delete(0, tk.END)
        entry_correct.delete(0, tk.END)

#Main window
window = tk.Tk()
window.title("Quiz Creator")
window.geometry("500x500")

#Labels and entry boxes for question, choices, and correct answer. Save button does nothing yet.
tk.Label(window, text="Enter your question:").pack()
entry_question = tk.Entry(window)
entry_question.pack()

tk.Label(window, text="Choice a:").pack()
entry_a = tk.Entry(window)
entry_a.pack()

tk.Label(window, text="Choice b:").pack()
entry_b = tk.Entry(window)
entry_b.pack()

tk.Label(window, text="Choice c:").pack()
entry_c = tk.Entry(window)
entry_c.pack()

tk.Label(window, text="Choice d:").pack()
entry_d = tk.Entry(window)
entry_d.pack()

tk.Label(window, text="Correct answer (a/b/c/d):").pack()
entry_correct = tk.Entry(window)
entry_correct.pack()

tk.Button(window, text="Save Question").pack()

#Loop
window.mainloop()