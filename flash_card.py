from tkinter import Tk, Label, PhotoImage, Canvas, Button, N, E, S, W
import pandas as pd
import os
import random

BG_COLOR = "#ffca18"
FONT_COLORS = ["#000000", "#fff"]


class FlashCardsWindow(Tk):
    def __init__(self, chosen_language):
        super().__init__()

        self.chosen_language = chosen_language
        self.data = self.read_csv_data()
        self.word_list = self.data.values.tolist()
        self.headers = [self.data.columns[0], self.data.columns[1]]
        self.current_card_type_index = 1
        self.current_item_index = 0

        self.title("FlashLearn")
        self.config(width=900, height=730, padx=50, pady=50, bg=BG_COLOR)
        self.flip_timer = self.after(8000, self.show_buttons)

        # Canvas Images
        self.card_front = PhotoImage(file="images/card_front.png")
        self.card_back = PhotoImage(file="images/card_back.png")
        self.card_images = [self.card_front, self.card_back]

        self.wrong_image = PhotoImage(file="images/wrong.png")
        self.correct_image = PhotoImage(file="images/correct.png")

        self.flip_to_test_card = PhotoImage(file="images/flip_to_test.png")
        self.flip_to_answer_card = PhotoImage(file="images/flip_to_answer.png")
        self.flip_images = [self.flip_to_answer_card, self.flip_to_test_card]

        self.save_image = PhotoImage(file="images/save.png")

        # Card Canvas
        self.card = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
        self.card.grid(column=0, row=1, columnspan=4)
        self.card_img = self.card.create_image(400, 263, image=self.card_front)
        self.language_text = self.card.create_text(
            400,
            150,
            text=str(self.headers[self.current_card_type_index]),
            font=("Arial", 40, "italic"),
        )
        self.word_text = self.card.create_text(
            400,
            253,
            text=self.word_list[self.current_item_index][self.current_card_type_index],
            font=("Arial", 55, "bold"),
        )

        # Top Elements

        self.counter = Label(
            self,
            text=f"Remaining Cards: {len(self.word_list)}",
            pady=20,
            bg=BG_COLOR,
            fg=FONT_COLORS[0],
            font=("Arial", 25, "bold"),
        )
        self.counter.grid(column=0, row=0, sticky=W, columnspan=2)

        self.reset_button = Button(
            text=f"Restart with all {self.chosen_language.title()} words",
            highlightthickness=0,
            bg=BG_COLOR,
            fg=FONT_COLORS[0],
            command=self.reset_words,
            pady=15,
            font=("Arial", 12, "bold"),
        )
        self.reset_button.grid(column=2, row=3, columnspan=2, sticky=S + E)

        # Buttons
        self.wrong_button = Button(
            image=self.wrong_image, highlightthickness=0, command=self.new_card, pady=20
        )

        self.flip_button = Button(
            image=self.flip_images[self.current_card_type_index],
            highlightthickness=0,
            command=self.show_buttons,
            pady=20,
        )
        self.flip_button.grid(column=1, row=2, columnspan=2)

        self.correct_button = Button(
            image=self.correct_image,
            highlightthickness=0,
            command=self.known_answer,
            pady=20,
        )

        self.save_button = Button(
            image=self.save_image,
            highlightthickness=0,
            command=self.save_progress,
            pady=20,
        )
        self.save_button.grid(column=3, row=0, columnspan=2, sticky=N + E)

    def read_csv_data(self):
        try:
            data = pd.read_csv(f"saved_data/{self.chosen_language}_words_to_learn.csv")
        except FileNotFoundError:
            data = pd.read_csv(
                f"word_data/{self.chosen_language}_200_most_common_words.csv"
            )

        return data

    def reset_words(self):
        try:
            os.remove(f"saved_data/{self.chosen_language}_words_to_learn.csv")
            self.data = self.read_csv_data()
            self.word_list = self.data.values.tolist()
            self.counter.config(text=f"Remaining Cards: {len(self.word_list)}")

        except FileNotFoundError:
            print("No words have been discarded yet")
        finally:
            self.new_card()

    def save_progress(self):
        test_items = [word[0] for word in self.word_list]
        answers = [word[1] for word in self.word_list]
        words_to_learn = {
            self.data.columns[0]: test_items,
            self.data.columns[1]: answers,
        }
        words_to_learn_data = pd.DataFrame(words_to_learn)
        words_to_learn_data.to_csv(
            f"saved_data/{self.chosen_language}_words_to_learn.csv", index=False
        )
        self.card.itemconfig(self.language_text, text="Progress Saved")
        self.card.itemconfig(
            self.word_text,
            text="Close Window or\nFlip card to continue",
        )

    def new_card(self):
        self.wrong_button.grid_forget()
        self.correct_button.grid_forget()
        self.next_word()

    def known_answer(self):

        del self.word_list[self.current_item_index]
        self.counter.config(text=f"Remaining Cards: {len(self.word_list)}")
        self.new_card()

    def next_word(self):
        self.after_cancel(self.flip_timer)
        if self.current_card_type_index == 1:
            self.flip_card()
        self.current_item_index = self.word_list.index(random.choice(self.word_list))
        self.card.itemconfig(
            self.word_text,
            text=self.word_list[self.current_item_index][self.current_card_type_index],
        )
        self.flip_timer = self.after(8000, self.show_buttons)

    def flip_card(self):

        if self.current_card_type_index == 0:
            self.current_card_type_index = 1
        else:
            self.current_card_type_index = 0
        self.flip_button.config(image=self.flip_images[self.current_card_type_index])
        self.card.itemconfig(
            self.card_img, image=self.card_images[self.current_card_type_index]
        )
        self.card.itemconfig(
            self.word_text,
            text=self.word_list[self.current_item_index][self.current_card_type_index],
            fill=FONT_COLORS[self.current_card_type_index],
        )
        self.card.itemconfig(
            self.language_text,
            text=self.headers[self.current_card_type_index],
            fill=FONT_COLORS[self.current_card_type_index],
        )

    def show_buttons(self):

        self.after_cancel(self.flip_timer)
        self.flip_card()
        self.wrong_button.grid(column=0, row=2, sticky=E)
        self.correct_button.grid(column=3, row=2, sticky=W)
