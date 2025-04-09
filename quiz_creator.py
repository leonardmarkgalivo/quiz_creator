import tkinter as tk

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

window.mainloop()

#Loop
window.mainloop()