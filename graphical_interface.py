import tkinter as tk


class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("数学题目生成器")  # 设置窗口标题

        # 创建标签和输入框用于输入题目数量
        self.num_questions_label = tk.Label(root, text="题目数量：")
        self.num_questions_label.pack()  # 将标签添加到窗口并显示

        self.num_questions_entry = tk.Entry(root)  # 创建输入框
        self.num_questions_entry.pack()  # 将输入框添加到窗口并显示

        # 创建标签和输入框用于输入数字的最大值
        self.max_value_label = tk.Label(root, text="最大值：")
        self.max_value_label.pack()  # 将标签添加到窗口并显示

        self.max_value_entry = tk.Entry(root)  # 创建输入框
        self.max_value_entry.pack()  # 将输入框添加到窗口并显示

        # 创建生成题目的按钮
        self.start_button = tk.Button(root, text="开始生成题目", command=self.generate_questions)
        self.start_button.pack()  # 将按钮添加到窗口并显示

        # 创建用于显示当前题目的标签
        self.current_question_label = tk.Label(root, text="当前题号：")
        self.current_question_label.pack()  # 将标签添加到窗口并显示

        # 创建用于显示题目文本的文本框
        self.current_question_text = tk.Text(root, height=5, width=30)
        self.current_question_text.pack()  # 将文本框添加到窗口并显示

        # 创建一个容器框架用于包含上一题和下一题按钮以及它们之间的空白
        button_frame = tk.Frame(root)
        button_frame.pack()  # 将容器框架添加到窗口并显示

        # 创建 "上一题" 按钮
        self.prev_button = tk.Button(button_frame, text="上一题", command=self.prev_question)
        self.prev_button.pack(side=tk.LEFT, padx=10)  # 将按钮添加到容器框架并显示，左对齐并设置水平间距

        # 在按钮之间插入一个空白的 Frame 来增加间距
        spacer_frame = tk.Frame(button_frame, width=20)  # 创建空白的 Frame 并调整宽度以增加间距
        spacer_frame.pack(side=tk.LEFT)  # 将空白的 Frame 添加到容器框架并显示

        # 创建 "下一题" 按钮
        self.next_button = tk.Button(button_frame, text="下一题", command=self.next_question)
        self.next_button.pack(side=tk.LEFT, padx=10)  # 将按钮添加到容器框架并显示，左对齐并设置水平间距

        # 创建用于输入答案的标签和输入框
        self.answer_label = tk.Label(root, text="请输入答案：")
        self.answer_label.pack()  # 将标签添加到窗口并显示

        self.answer_entry = tk.Entry(root)  # 创建输入框
        self.answer_entry.pack()  # 将输入框添加到窗口并显示

        # 创建提交答案的按钮
        self.submit_button = tk.Button(root, text="提交答案", command=self.submit_answer)
        self.submit_button.pack()  # 将按钮添加到窗口并显示

        # 创建用于显示结果的文本框
        self.result_text = tk.Text(root, height=5, width=30)
        self.result_text.pack()  # 将文本框添加到窗口并显示

        self.questions = []  # 用于存储生成的题目
        self.current_question_index = 0  # 当前题目的索引

    def generate_questions(self):
        num_questions = int(self.num_questions_entry.get())  # 获取题目数量输入框的值
        max_value = int(self.max_value_entry.get())  # 获取最大值输入框的值

        # 在这里生成题目并将其存储在self.questions列表中
        # 你需要实现生成题目的逻辑，并将题目添加到self.questions中

        self.current_question_index = 0  # 重置当前题目的索引
        self.show_current_question()  # 显示当前题目

    def show_current_question(self):
        if 0 <= self.current_question_index < len(self.questions):
            self.current_question_label.config(text=f"当前题号：{self.current_question_index + 1}")  # 更新当前题号标签的文本
            self.current_question_text.delete(1.0, tk.END)  # 清空题目文本框
            self.current_question_text.insert(tk.END, self.questions[self.current_question_index])  # 显示当前题目
        else:
            self.current_question_label.config(text="当前题号：")  # 清空当前题号标签的文本
            self.current_question_text.delete(1.0, tk.END)  # 清空题目文本框

    def prev_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1  # 切换到上一题
            self.show_current_question()  # 显示当前题目

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1  # 切换到下一题
            self.show_current_question()  # 显示当前题目

    def submit_answer(self):
        if 0 <= self.current_question_index < len(self.questions):
            user_answer = self.answer_entry.get()  # 获取用户输入的答案
            correct_answer = self.questions[self.current_question_index].get_correct_answer()  # 替换成获取正确答案的方法
            is_correct = user_answer == correct_answer  # 检查答案是否正确
            result_text = f"第{self.current_question_index + 1}题：{'正确' if is_correct else '错误'}\n"  # 构建结果文本
            result_text += f"你的答案：{user_answer}\n"
            result_text += f"正确答案：{correct_answer}\n\n"
            self.result_text.insert(tk.END, result_text)  # 在结果文本框中显示结果


if __name__ == "__main__":
    root = tk.Tk()  # 创建Tkinter窗口
    app = MathQuizApp(root)  # 创建应用程序对象
    # 进入主事件循环，启动应用程序
    root.mainloop()
