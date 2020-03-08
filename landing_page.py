from tkinter import *
from tkinter import messagebox


class LandingPage():

    def __init__(self, root):
        self.root = root
        self.root.title("Remembering Steve Jobs - Think Different.")
        self.root.geometry("1000x1100+100+100")

        self.photo = PhotoImage(file='think_diff.gif')
        self.image = Label(self.root, image=self.photo)
        self.image.pack(side=TOP)

        self.frame1 = Frame(root, width=450, height=50, pady=3)
        self.frame2 = Frame(root, width=450)
        self.frame3 = Frame(root, width=450, height=10)
        self.frame1.pack(side=TOP)
        self.frame2.pack(fill=X, expand=True)
        self.frame3.pack(fill=X, expand=True)

        self.desc1 = Label(self.frame1, text="On a n x n board, find words that can be formed by a sequence of adjacent letters.",
                           font=('Helvetica', '20'))
        self.desc2 = Label(self.frame1, text="Words must be 3 or more letters.",
                           font=('Helvetica', '20'))
        self.desc1.pack(side=TOP, padx=15)
        self.desc2.pack(side=TOP, padx=15)
        self.desc3 = Label(self.frame1)
        self.desc3.pack(side=TOP, padx=15, pady=15)

        # Textbox that ask questions
        self.desc4 = Label(self.frame2, text="Choose n :             ", font=('Helvetica', '20'))
        self.desc4.pack(side=LEFT, padx=15, pady=1)
        self.entry2 = Entry(self.frame2)
        self.entry2.pack(fill=X, padx=15)

        self.desc5 = Label(self.frame3, text="Enter alphabetical inputs :   ", font=('Helvetica', '20'))
        self.desc5.pack(side=LEFT, padx=15)
        self.entry3 = Entry(self.frame3)
        self.entry3.pack(fill=X, padx=5)

        self.desc6 = Label(self.frame3, text="Example: n = 3, input = 'abcabcabc'.(9 alphabets)",
                           font=('Helvetica', '14'))
        self.desc6.pack(side=LEFT, padx=5)

        self.button_widget = Button(root, text="I'm ready to put a ding in the universe -  ", height=3,
                                    font=('Helvetica', '23'),
                                    fg="red", command=self.action)
        self.button_widget.pack(fill=X, side=BOTTOM)

        self.num = 0
        self.str = ""
        self.board_size = self.num * self.num

    def action(self):
        '''Check input and proceed to the game.'''

        words = self.entry3.get()
        words = words.replace(" ", "").lower()
        temp = ""
        for char in words:
            if char.isalpha():
                temp += char

        if not self.entry2.get().isnumeric():
            messagebox.showerror(message="n value should be a numeric value.")

        self.num = int(self.entry2.get())
        self.board_size = self.num * self.num
        if self.num < 2 or self.num > 10:
            messagebox.showerror(message="Recommendation: select a n value between 2 and 10.")
        elif len(temp) != self.board_size:
            messagebox.showerror(message="The input string is not enough to form a board of size {}.".format(self.board_size))
        else:
            self.str = temp
            messagebox.showinfo('Congrats!', 'The rest of the game will be run in your terminal!')
            self.root.quit()

    def retrieve_val(self):
        return (self.num, self.board_size, self.str)
