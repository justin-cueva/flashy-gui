from ui import AppUI
import pandas

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

flash_card_gui = AppUI(cards_to_learn=to_learn)
