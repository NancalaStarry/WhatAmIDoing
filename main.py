import tkinter as tk
import time


class ReminderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(200, 100)
        self.root.maxsize(400, 200)
        self.root.title("你正在做...")
        self.root.attributes('-topmost', True)
        self.root.configure(bg='black')
        self.root.attributes('-alpha', 0.5)

        self.start_time = time.time()
        self.task_label = tk.Label(self.root, text="你正在做：\n", fg="white", bg="black", wraplength=200)
        self.task_label.pack()

        self.task_entry = tk.Entry(self.root, fg="black", bg="white")
        self.task_entry.pack()
        self.task_entry.bind('<Return>', self.update_task)  # 绑定回车键到update_task函数

        self.time_label = tk.Label(self.root, text="", fg="white", bg="black")
        self.time_label.pack()

        self.root.bind('<Enter>', self.on_enter)
        self.root.bind('<Leave>', self.on_leave)

        self.update_time()

    def update_task(self, event):
        self.start_time = time.time()
        self.task_label.config(text="你正在做：\n" + self.task_entry.get())

    def update_time(self):
        elapsed_time = time.time() - self.start_time
        self.time_label.config(text=f"已用时间：{int(elapsed_time)}秒")
        if int(elapsed_time) % 60 == 0:
            self.task_entry.configure(bg='red')
        if (int(elapsed_time)-1) % 60 == 0:
            self.task_entry.configure(bg='white')
        self.root.after(1000, self.update_time)

    def on_enter(self, event):
        self.root.attributes('-alpha', 1.0)
        self.time_label.config(text=f"已用时间：{round((time.time() - self.start_time)//60)}分")

    def on_leave(self, event):
        self.root.attributes('-alpha', 0.5)
        self.time_label.config(text=f"已用时间：{int((time.time() - self.start_time))}秒")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ReminderApp()
    app.run()
