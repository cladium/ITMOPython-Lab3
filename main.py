import tkinter as tk
import random
import os

FONT_PATH = "font/png/"
BACKGROUND_PATH = "bg_chloe.png"
LOGO_PATH = "lis_logo.png"
INPUT_BG_COLOR = "#e1c9d6"
BUTTON_BG_COLOR = "#e1c9d6"
BUTTON_FG_COLOR = "#4e3b3d"
TEXT_BG_COLOR = "#d99c92"
TEXT_FG_COLOR = "#4e3b3d"


def on_generate_png():
    if len(entry_str.get()) == 6:
        letters = list(set(entry_str.get().upper()))
        canvas.itemconfig(output_window, state="hidden")
        positions = list(set([(ord(i) - 96) % 10 for i in letters]))
        x_pos = 740
        y_pos = 290
        for i in range(3):
            l = random.choice(letters)
            canvas.itemconfig(key_png_list[i], image=font_dict[l])
            canvas.coords(key_png_list[i], x_pos, y_pos)
            x_pos += font_dict[l].width() + 2

        canvas.itemconfig(key_png_list[3], image=font_dict["hyphen"])
        canvas.coords(key_png_list[3], x_pos, y_pos)
        x_pos += font_dict["hyphen"].width() + 2

        for i in range(6):
            l = str(random.choice(positions))
            canvas.itemconfig(key_png_list[i + 4], image=font_dict[l])
            canvas.coords(key_png_list[i + 4], x_pos, y_pos)
            x_pos += font_dict[l].width() + 2

        canvas.itemconfig(key_png_list[10], image=font_dict["hyphen"])
        canvas.coords(key_png_list[10], x_pos, y_pos)
        x_pos += font_dict["hyphen"].width() + 2

        for i in range(3):
            l = random.choice(letters)
            canvas.itemconfig(key_png_list[i + 11], image=font_dict[l])
            canvas.coords(key_png_list[i + 11], x_pos, y_pos)
            x_pos += font_dict[l].width() + 2
    else:
        canvas.itemconfig(output_window, state="normal")


root = tk.Tk()
root.title("LiS Keygen")

canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack()

# load & set background & logo
background_image = tk.PhotoImage(file=BACKGROUND_PATH)
overlay_image = tk.PhotoImage(file=LOGO_PATH)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
img_id = canvas.create_image(570, 35, anchor=tk.NW, image=overlay_image)

# load all font .png files into dict
font_dict = {}
for filename in os.listdir(FONT_PATH):
    file_path = os.path.join(FONT_PATH, filename)
    if os.path.isfile(file_path):
        font_dict[os.path.splitext(os.path.basename(file_path))[0]] = tk.PhotoImage(
            file=file_path
        )


# create list for all key .png's
key_png_list = []
x_pos = 740
y_pos = 290
for i in range(14):
    if i in (3, 10):
        key_png_list.append(
            canvas.create_image(x_pos, y_pos, anchor=tk.NW, image=font_dict["hyphen"])
        )
        x_pos += font_dict["hyphen"].width() + 2
    else:
        key_png_list.append(
            canvas.create_image(x_pos, y_pos, anchor=tk.NW, image=font_dict["X"])
        )
        x_pos += font_dict["X"].width() + 2

entry_str = tk.StringVar()
entry_field = tk.Entry(
    root, bg=INPUT_BG_COLOR, font=("Calibri", 22), textvariable=entry_str
)
entry_window = canvas.create_window(
    840, 400, anchor="nw", window=entry_field, width=120
)

generate_button = tk.Button(
    root,
    text="Generate",
    bg=BUTTON_BG_COLOR,
    fg=BUTTON_FG_COLOR,
    font=("Calibri", 22),
    command=on_generate_png,
)
button_window = canvas.create_window(
    970, 400, anchor="nw", window=generate_button, height=40
)

output_label = tk.Label(
    root,
    bg=TEXT_BG_COLOR,
    fg=TEXT_FG_COLOR,
    font=("Calibri", 20),
    text="The input field must contain 6 letters",
)
output_window = canvas.create_window(
    780, 480, anchor="nw", window=output_label, height=50, state="hidden"
)

root.mainloop()
