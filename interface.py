import tkinter as tk
from function import *


class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("数学题目生成器")

        self.questions = []
        self.answers = []

        # 创建题目数量输入框和标签
        self.num_questions_label = tk.Label(root, text="题目数量:")
        self.num_questions_label.pack()

        self.num_questions_entry = tk.Entry(root)
        self.num_questions_entry.pack()

        # 创建最大值输入框和标签
        self.max_value_label = tk.Label(root, text="最大值:")
        self.max_value_label.pack()

        self.max_value_entry = tk.Entry(root)
        self.max_value_entry.pack()

        # 创建生成题目按钮
        self.generate_button = tk.Button(root, text="开始生成题目", command=self.generate_questions)
        self.generate_button.pack()

        # 创建题目和答案显示区域
        self.questions_label = tk.Label(root, text="题目:")
        self.questions_label.pack()

        self.questions_text = tk.Text(root, height=10, width=40)
        self.questions_text.pack()

        self.answers_label = tk.Label(root, text="答案:")
        self.answers_label.pack()

        self.answers_text = tk.Text(root, height=10, width=40)
        self.answers_text.pack()

        # 创建提交答案按钮
        self.submit_button = tk.Button(root, text="提交答案", command=self.check_answers)
        self.submit_button.pack()

        # 创建答题结果显示区域
        self.results_label = tk.Label(root, text="答题结果:")
        self.results_label.pack()

        self.results_text = tk.Text(root, height=5, width=40)
        self.results_text.pack()

    def generate_questions(self):
        # 获取题目数量和最大值输入并存储为全局变量
        global num_questions
        global max_value
        num_questions = int(self.num_questions_entry.get())
        max_value = int(self.max_value_entry.get())

        # 调用 function.py 中的函数生成题目
        exp = Expression(max_value, num_questions)
        self.questions, self.answers = exp.run()

        # 清空题目和答案文本框
        self.questions_text.delete(1.0, tk.END)
        self.answers_text.delete(1.0, tk.END)

        # 在界面上显示题目，并标注序号
        for i, question in enumerate(self.questions, start=1):
            self.questions_text.insert(tk.END, f"{i}. {question}\n")

        # 将正确答案保存到文件 "answer.txt"
        with open("answer.txt", "w") as answer_file:
            for answer in self.answers:
                answer_file.write(answer + "\n")

        # 将问题保存到文件 "question.txt"
        with open("question.txt", "w") as question_file:
            for question in self.questions:
                question_file.write(question + "\n")

    def check_answers(self):
        # 获取用户输入的答案
        user_answers = self.answers_text.get(1.0, tk.END).splitlines()

        # 初始化正确和错误答案列表
        correct = []
        incorrect = []

        # 比较用户答案和正确答案，并记录结果
        for i, (user_answer, correct_answer) in enumerate(zip(user_answers, self.answers), start=1):
            if user_answer.strip() == correct_answer.strip():
                correct.append(i)
            else:
                incorrect.append(i)

        # 清空答题结果文本框，并显示结果
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"正确题号: {', '.join(map(str, correct))}\n")
        self.results_text.insert(tk.END, f"错误题号: {', '.join(map(str, incorrect))}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
