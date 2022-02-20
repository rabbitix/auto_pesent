import time
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo
import pyautogui


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Auto Hazeri")
        self.master.rowconfigure(10, weight=1)
        self.master.columnconfigure(15, weight=1)
        self.grid(sticky=W + E + N + S)
        self.button = Button(self, text="Browse", command=self.load_file, width=10)
        self.button.grid(row=1, column=0, sticky=W)

    def load_file(self):
        fname = askopenfilename(filetypes=(
            ("text files", "*.txt"),
            ("All files", "*.*")))
        if fname:
            try:

                with open(fname, 'r') as file:
                    lst = file.read().splitlines()

                print(lst)
                showinfo("find input", "you have 10 sec to put mouse on input..")
                time.sleep(10)
                input_pos_x, input_pos_y = pyautogui.position()
                showinfo("input ok | btn 1", "ok, you have 10 sec to put mouse on btn 1")
                time.sleep(10)
                btn_1_pos_x, btn_1_pos_y = pyautogui.position()
                showinfo("btn1 ok | btn 2", "so, you have 10 sec to go to btn2")
                time.sleep(10)
                btn2_pos_x, btn2_pos_y = pyautogui.position()
                showinfo("all set", "ok all set.. lets start")
                for code in lst:
                    print("sleep 3 sec for each..")
                    time.sleep(3)
                    pyautogui.click(input_pos_x, input_pos_y)
                    pyautogui.typewrite(code, interval=0.1)
                    pyautogui.click(btn_1_pos_x, btn_1_pos_y)
                    time.sleep(2)  # sleep 2 sec for each erquest
                    pyautogui.click(btn2_pos_x, btn2_pos_y)
                    print(f"done {code}")

                showinfo("done all", "done all")
                return


            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return


if __name__ == "__main__":
    MyFrame().mainloop()
