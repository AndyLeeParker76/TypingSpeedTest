from tkinter import *
from tkinter import font
from paragraph_text import *
import time
class TypingTest:
    window: Tk
    current_frame: Frame
    paragraph_text: str
    start_time: int
    end_time: int
    user_input: Text
    seconds: int
    minutes: int
    get_user_input: str
    backspace_count: int
    key_press_count: int

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1350x1000")
        self.window.title("Typing Speed Test")
        self.window.configure(bg="navajowhite")
        self.window.minsize(1500, 1000)
        self.current_frame = Frame(self.window, bg="sandybrown", width=1500, height=1500)
        self.current_frame.pack()
        self.text_number = IntVar()
        self.topic = StringVar()
        self.paragraph_topic = list(get_paragraph_topic())
        self.start_flag = 0
        self.seconds = 0
        self.minutes = 0
        self.backspace_count = 0

    def get_exit(self):
        self.window.quit()

    def clear_frame(self):
        for wid in self.current_frame.winfo_children():
            wid.destroy()

    def previous_text(self, backward, forward, title, place_holder):
        if (self.text_number.get() == 1):
            backward.config(state=DISABLED)
        else:
            backward.config(state=NORMAL)

        forward.config(state=NORMAL)

        self.text_number.set(self.text_number.get() - 1)
        self.topic.set(self.paragraph_topic[self.text_number.get()])
        title.config(text=self.topic.get())

        self.paragraph = get_paragraph_text(self.topic.get())
        place_holder.config(text=self.paragraph)

    def next_text(self, backward, forward, title, place_holder):
        if (self.text_number.get() == (len(self.paragraph_topic) - 2)):
            forward.config(state=DISABLED)
        else:
            forward.config(state=NORMAL)

        backward.config(state=NORMAL)

        self.text_number.set(self.text_number.get() + 1)
        self.topic.set(self.paragraph_topic[self.text_number.get()])
        title.config(text=self.topic.get())

        self.paragraph = get_paragraph_text(self.topic.get())
        place_holder.config(text=self.paragraph)

    def update_timer(self, s_time):
        current_time = time.time()

        if (int(current_time - s_time) >= 0):
            self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        min_p = '{:0>2d}'.format(int(self.minutes))
        sec_p = '{:0>2d}'.format(int(self.seconds))

        time_count.config(text=f'{min_p}:{sec_p}')
        time_count.after(1000, lambda: self.update_timer(s_time))

    def time_format(self, total_time):
        time_format = ""
        time_format = '{:0>2d}'.format(int(total_time / 60))
        time_format += ':' + '{:0>2d}'.format(int(total_time % 60))
        return time_format

    def calculate_speed(self):
        total_time = int(self.end_time - self.start_time)
        wpm = correct_letters = correct_words = accuracy = revised_accuracy = 0
        correct_flag = 1
        for para_char, user_char in zip(self.paragraph, self.get_user_text):
            if para_char == user_char:
                correct_letters += 1
            else:
                correct_flag = 0

            if para_char == ' ' or para_char == '\n' or para_char == '\t':
                correct_words += 1 if correct_flag == 1 else 0
                correct_flag = 1

        correct_words += 1 if correct_flag == 1 else 0
        wpm = correct_words / (float(total_time) / 60)

        accuracy = (correct_letters * 100) / len(self.paragraph)
        revised_accuracy = (correct_letters - self.backspace_count) * 100 / len(self.paragraph)

        return int(accuracy), int(revised_accuracy), int(wpm), self.time_format(total_time)

    def reset_test(self):
        self.start_flag = 0
        self.seconds = 0
        self.minutes = 0
        self.backspace_count = 0

    def back_to_home(self) -> None:
        self.reset_test()
        self.clear_frame()
        self.set_typing_home()

    def show_results(self):

        self.clear_frame()
        (accuracy, revised_accuracy, wpm, total_time) = self.calculate_speed()
        result = Label(self.current_frame, text="Results", fg='sienna', bg='khaki',
                       font='Times 30')
        result.grid(row=0, columnspan=3, pady=40)
        lb_accuracy = Label(self.current_frame, text='Accuracy', fg='sienna', bg='khaki', font='Times 20')
        lb_accuracy.grid(row=1, column=0)
        accuracy_val = Label(self.current_frame, text=f'{accuracy}%', fg='sienna', bg='khaki', font='Times 20')
        accuracy_val.grid(row=1, column=1, columnspan=2)

        lb_revised_accuracy = Label(self.current_frame, text='Revised Accuracy', fg='sienna', bg='khaki',
                                   font='Times 20')
        lb_revised_accuracy.grid(row=2, column=0, pady=(25, 0))
        revised_accuracy_val = Label(self.current_frame, text=f'{revised_accuracy}%', fg='sienna', bg='khaki',
                                    font='Times 20')
        revised_accuracy_val.grid(row=2, column=1, columnspan=2, pady=(25, 0))

        lb_wpm = Label(self.current_frame, text="WPM", fg='sienna', bg='khaki', font='Times 20')
        lb_wpm.grid(row=3, column=0)
        val_wpm = Label(self.current_frame, text=f'{wpm}', fg='sienna', bg='khaki', font='Times 20')
        val_wpm.grid(row=3, column=1, columnspan=2, pady=25)

        lb_time = Label(self.current_frame, text="Total Time", fg='sienna', bg='khaki', font='Times 20')
        lb_time.grid(row=4, column=0)
        val_time = Label(self.current_frame, text=f'{total_time}', fg='sienna', bg='khaki', font='Times 20')
        val_time.grid(row=4, column=1, columnspan=2)

        lb_exit = Button(self.current_frame, text='EXIT', fg='sienna', bg='khaki', font='Verdana 18',
                         borderwidth=3, command=self.get_exit)
        lb_exit.grid(row=5, column=0, pady=50, padx=30)
        lb_home = Button(self.current_frame, text='HOME', fg='sienna', bg='khaki', font='Verdana 18',
                         borderwidth=3, command=self.back_to_home)
        lb_home.grid(row=5, column=2, pady=50, padx=30)

    def key_release(self, event):
        if self.start_flag == 0:
            self.start_flag = 1
            self.start_time = time.time()
            self.update_timer(self.start_time)

        self.get_user_text = self.user_input.get('1.0', 'end - 1c')

        if self.paragraph.startswith(self.get_user_text):
            self.user_input.config(fg='green')
        else:
            self.user_input.config(fg='red')

        if event.keysym == 'BackSpace':
            self.backspace_count += 1

        self.key_press_count = len(self.get_user_text)
        if self.key_press_count >= len(self.paragraph):
            self.end_time = time.time()
            self.show_results()

    def start_typing(self):
        self.clear_frame()

        title = Label(self.current_frame, fg='sienna', bg='khaki', text=self.topic.get(),
                      font='Times 26')
        title.grid(row=0, column=0, columnspan=1, pady=50)

        global time_count
        time_count = Label(self.current_frame, fg='sienna', bg='khaki', text='Timer: 00:00', font='Times 24')
        time_count.grid(row=0, column=2, pady=50)

        place_holder = Message(self.current_frame, text=self.paragraph, fg='sienna', bg='cornsilk', width=1000,
                               justify='center', font='Times 16')
        place_holder.grid(row=2, column=0, columnspan=3, padx=40, pady=40)

        self.user_input = Text(self.current_frame, width=80, height=10, bg='khaki', fg='sienna',
                               insertbackground='cornsilk', borderwidth=5, relief=RAISED, padx=5, pady=5,
                               font='Times 16')

        self.user_input.grid(row=3, column=0, columnspan=3, padx=30)
        self.user_input.bind('<KeyRelease>', self.key_release)
        self.user_input.focus()
    def set_typing_home(self):
        if (self.current_frame != None):
            self.clear_frame()

        self.text_number.set(0)
        self.topic.set(self.paragraph_topic[0])

        backward = Button(self.current_frame,
                          text='Back',
                          bg='cornsilk', fg='sienna', relief=RAISED,
                          font='Times 20',
                          state=DISABLED, command=lambda: self.previous_text(backward, forward,title, place_holder))

        title = Label(self.current_frame, fg='sienna', bg='khaki', text=self.topic.get(), font='Times 22')

        forward = Button(self.current_frame,
                         text='Next',
                         bg='cornsilk', fg='sienna', relief=RAISED,
                         font='Times 20', command=lambda: self.next_text(backward, forward, title, place_holder))

        backward.grid(row=1, column=0, pady=35)
        title.grid(row=0, column=1, pady=35)
        forward.grid(row=1, column=2, pady=(35))

        self.paragraph = get_paragraph_text(self.topic.get())

        place_holder = Message(self.current_frame, text=self.paragraph, fg='sienna', bg='cornsilk', width=1000,
                               justify='center', font='Times 18')
        place_holder.grid(row=3, column=0, columnspan=3)

        start_test = Button(self.current_frame, text="Start Test", font='Times 16', borderwidth=3,
                            bg='navajowhite', fg='sienna', relief=RAISED, command=self.start_typing)
        start_test.grid(row=1, column=1, pady=10)

        exit = Button(self.current_frame,
                      text='Exit',
                      font='Times 16',
                      borderwidth=3,
                      bg='navajowhite', fg='sienna', relief=RAISED,
                      command=self.get_exit)
        exit.grid(row=5, column=1)


if __name__ == '__main__':
    '''Creating Typing Class Instance'''
    typing_test = TypingTest()
    typing_test.set_typing_home()
    typing_test.window.mainloop()