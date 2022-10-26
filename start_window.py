from tkinter import Tk, Radiobutton, Label, StringVar
from flash_card import FlashCardsWindow

languages = [
    "french",
    "german",
    "italian",
    "portuguese",
    "spanish",
]
BG_COLOR = "#ffca18"
FONT_COLORS = ["#000000", "#fff"]


class StartWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("FlashLearn")
        self.config(width=100, height=200, padx=50, pady=50, bg=BG_COLOR)

        self.prompt = Label(
            self,
            text="""Which language do you wish to learn?""",
            justify="center",
            pady=25,
            bg=BG_COLOR,
            fg=FONT_COLORS[0],
            font=("Arial", 30, "bold"),
        )
        self.prompt.grid(column=1, row=1, columnspan=2)

        self.radio_choice = StringVar()
        self.make_language_list()

    def start_game(self):
        chosen_language = self.radio_choice.get()
        self.destroy()
        game = FlashCardsWindow(chosen_language)
        game.new_card()
        game.mainloop()

    def make_language_list(self):

        for idx, language in enumerate(languages):
            new_radio = Radiobutton(
                self,
                text=language.title(),
                width=10,
                justify="center",
                variable=self.radio_choice,
                command=self.start_game,
                value=language,
                indicatoron=0,
                bg="#91C2AF",
                fg=FONT_COLORS[1],
                font=("Arial", 15, "bold"),
            )
            new_radio.grid(column=1, row=idx + 2, columnspan=2)
