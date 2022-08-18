import tkinter
import random
import word_data
import pandas

BACKGROUND_COLOR = "#B1DDC6"
size_of_canvas = (800, 526)


class AppUI:
    def __init__(self, cards_to_learn: word_data.to_learn):

        self.cards_to_learn = cards_to_learn
        self.current_card = random.choice(self.cards_to_learn)
        self.window = tkinter.Tk()
        self.window.title("FLASHY")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.flip_timer = self.window.after(ms=3000, func=self.flip_card)

        # DISPLAYING CARD STUFF
        self.canvas = tkinter.Canvas(width=size_of_canvas[0], height=size_of_canvas[1], bg=BACKGROUND_COLOR,
                                     highlightthickness=0)
        self.back_card_image = tkinter.PhotoImage(file="images/card_back.png")
        self.front_card_image = tkinter.PhotoImage(file="images/card_front.png")
        self.card = self.canvas.create_image(
            size_of_canvas[0] / 2,
            size_of_canvas[1] / 2,
            image=self.front_card_image
        )
        self.language = self.canvas.create_text(
            size_of_canvas[0] / 2,
            size_of_canvas[1] * 0.30,
            text="French",
            font=("Arial", 40, "italic"),
            fill="#000000"
        )
        self.word = self.canvas.create_text(
            size_of_canvas[0] / 2,
            size_of_canvas[1] / 2,
            text=" ",
            font=("Arial", 60, "bold"),
            fill="#000000"
        )
        self.canvas.grid(row=0, column=0, columnspan=2)

        # DISPLAYING BUTTONS
        wrong_button_image = tkinter.PhotoImage(file="images/wrong.png")
        right_button_image = tkinter.PhotoImage(file="images/right.png")

        self.wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0, command=self.next_card)
        self.wrong_button.grid(row=1, column=0)
        self.right_button = tkinter.Button(image=right_button_image, highlightthickness=0, command=self.is_known)
        self.right_button.grid(row=1, column=1)

        self.next_card()
        self.window.mainloop()

    def is_known(self):
        self.cards_to_learn.remove(self.current_card)

        print(len(self.cards_to_learn))
        data = pandas.DataFrame(self.cards_to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        self.next_card()

    def next_card(self):
        self.window.after_cancel(self.flip_timer)
        self.current_card = random.choice(self.cards_to_learn)
        self.canvas.itemconfig(self.language, text="French")
        self.canvas.itemconfig(self.word, text=self.current_card["French"])
        self.canvas.itemconfig(
            self.card,
            image=self.front_card_image
        )
        self.flip_timer = self.window.after(ms=3000, func=self.flip_card)

    def flip_card(self):
        self.canvas.itemconfig(self.language, text="English")
        self.canvas.itemconfig(self.word, text=self.current_card["English"])
        self.canvas.itemconfig(
            self.card,
            image=self.back_card_image
        )
