import tkinter as tk
from tkinter import messagebox

questions = [
    ("Какая компания производит модель мотоцикла Hayabusa?", "Suzuki"),
    ("Как называется мотоцикл Harley-Davidson с двигателем объемом 1 883 куб. см?", "Iron 883"),
    ("Какая компания производит модель мотоцикла Ninja?", "Kawasaki"),
    ("Как называется модель мотоцикла Ducati, известная своим красным цветом?", "Panigale"),
    ("Какая компания производит модель мотоцикла Gold Wing?", "Honda"),
]

class MotoQuizApp:
    def init(self, root):
        self.root = root
        self.root.title("Тест на тему мотоциклы")
        
        self.question_index = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", wraplength=400, font=('Arial', 14))
        self.question_label.pack(pady=20)
        
        self.answer_entry = tk.Entry(root, font=('Arial', 14))
        self.answer_entry.pack(pady=20)
        
        self.submit_button = tk.Button(root, text="Ответить", command=self.check_answer, font=('Arial', 14))
        self.submit_button.pack(pady=20)
        
        self.next_button = tk.Button(root, text="Следующий вопрос", command=self.next_question, state=tk.DISABLED, font=('Arial', 14))
        self.next_button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", wraplength=400, font=('Arial', 14))
        self.result_label.pack(pady=20)
        
        self.show_question()
    
    def show_question(self):
        self.answer_entry.delete(0, tk.END)
        self.question_label.config(text=questions[self.question_index][0])
        self.result_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
    
    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = questions[self.question_index][1]
        if user_answer.lower() == correct_answer.lower():
            self.result_label.config(text="Правильно!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f"Неправильно! Правильный ответ: {correct_answer}", fg="red")
        
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
    
    def next_question(self):
        self.question_index += 1
        if self.question_index < len(questions):
            self.show_question()
        else:
            self.show_result()
    
    def show_result(self):
        self.question_label.config(text=f"Вы ответили на {self.score} из {len(questions)} вопросов правильно.")
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.next_button.pack_forget()
        self.result_label.pack_forget()

if name == "main":
    root = tk.Tk()
    app = MotoQuizApp(root)
    root.mainloop()
