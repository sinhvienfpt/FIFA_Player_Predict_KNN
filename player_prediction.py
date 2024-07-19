import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import numpy as np
import pandas as pd
from knn import KNNRecognizer
import os
import webbrowser
# Function to overlay one image onto another
def overlay_images(background_image, overlay_image):
    overlay = Image.open(overlay_image)
    overlay = overlay.resize((322, 450), Image.LANCZOS)
    if overlay.mode != 'RGBA':
            overlay = overlay.convert("RGBA")
    background_image.paste(overlay, (0, 0), overlay)
    return background_image

# Function to add text to an image
def add_text_to_image(image, text_values):
    draw = ImageDraw.Draw(image)
    font_path = "arial.ttf"
    font_size = 17
    font = ImageFont.truetype(font_path, font_size)
    fontvalue = ImageFont.truetype(font_path, font_size+4)

    # Center the name text
    name_width, name_height = draw.textsize(text_values[0], font=fontvalue)    
    image_width, image_height = image.size    
    x_offset = (image_width - name_width) // 2    
    draw.text((x_offset, 365), text_values[0], font=fontvalue, fill="white")

    # Add numerical values
    x_start = 40
    y_start = 300   
    x_offset = x_start 
    y_offset = y_start -195 
    for text in text_values[-2:]:
        draw.text((x_offset +2, y_offset), str(text), font=fontvalue, fill="white")
        y_offset += font_size + 5
        x_offset -= 3
    
    # Add labels and values
    x_offset = x_start +2
    y_offset = y_start + 25    
    for text in text_values[1:-2]:
        draw.text((x_offset , y_offset), str(text), font=fontvalue, fill="white")
        x_offset += font_size + 25

    # Add attribute labels
    x_offset = x_start
    y_offset = y_start
    for text in ['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']:
        draw.text((x_offset, y_start), text, font=font, fill="black")
        x_offset += font_size + 25
    return image


# Function to search and display player predictions
def search_player():
    global image_paths, values_to_display, image_backgr_paths, links
    test = [] 
    try:
        for label in numerical_labels:
            test.append(int(entries[label].get()))
    except:
        messagebox.showerror("Input Error", "Please enter valid numerical values between 1 and 99.")
        return
    
    FIFA_player_predict =  knn.predict(test)
    values_to_display, image_backgr_paths, image_paths, links = [], [], [], []
  
    for result in FIFA_player_predict:
        infor_predict= df[(df['id'] == result[0]) & (df['Version'] == result[1])].values.tolist()
        image_paths.append("img/"+infor_predict[0].pop(0)+'.png')
        image_backgr_paths.append('Version/'+infor_predict[0].pop(1)[:-1]+'.png')
        links.append(infor_predict[0].pop())
        values_to_display.append(infor_predict[0])

    update_image(0)

# Function to update the displayed image
def update_image(index):
    if not os.path.exists(image_backgr_paths[index]):        
        background_image = Image.open('Version\All.png')
    else:
        background_image = Image.open(image_backgr_paths[index])
    if len(image_paths) < 5:
        return

    background_image = background_image.resize((322, 450), Image.LANCZOS)
    result_image = overlay_images(background_image,image_paths[index] )
    result_image = add_text_to_image(result_image, values_to_display[index])

    photo = ImageTk.PhotoImage(result_image)
    image_label.config(image=photo)
    image_label.image = photo     

    result_label.config(text=f"Predicted player: {index +1} - {values_to_display[index][0]} - {image_backgr_paths[index][8:-4]} ")

# Function to go to the next image
def next_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(image_paths)
    update_image(current_image_index)

# Function to go to the previous image
def previous_image():
    global current_image_index
    current_image_index = (current_image_index - 1) % len(image_paths)
    update_image(current_image_index)

# Function to open a link on double click
def on_image_double_click(event):
    link = links[current_image_index]
    if link:
        webbrowser.open(link)

# Load data and train the model
df = pd.read_csv('data.csv')
knn = KNNRecognizer()
y = df[['id','Version']]
x = df[['PAC','SHO',	'PAS','DRI',"DEF"	,'BHY']]
knn.train(x,y)

# Initialize the Tkinter application
app = tk.Tk()
app.title('Prediction Player')

# Frame for player data input
frame = ttk.LabelFrame(app, text="Patient Data", padding=(20, 10))
frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Entry fields for numerical data
numerical_labels = ['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']
row = 2
entries = {}
for n_label in numerical_labels:
    label = ttk.Label(frame, text=f"{n_label}:")
    label.grid(row=row, column=0, sticky="e", pady=5)
    entry = ttk.Combobox(frame, values=list(range(99,0,-1)))
    entry.grid(row=row, column=1, sticky="ew", pady=5)
    entries[n_label] = entry
    row += 1

# Submit button
submit_button = ttk.Button(frame, text="Submit", command=search_player)
submit_button.grid(row=row, column=0, columnspan=2, pady=10)

# Frame for notes
notes_frame = ttk.LabelFrame(app, text="Notes", padding=(20, 10))
notes_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

notes = [
    "PAC: Pace, measuring the player's speed and acceleration",
    "SHO: Shooting, measuring the player's shooting ability",
    "PAS: Passing, measuring the player's passing ability",
    "DRI: Dribbling, measuring the player's dribbling skills",
    "DEF: Defense, measuring the player's defensive abilities",
    "PHY: Physical, measuring the player's physical strength and stamina"
]

for i, note in enumerate(notes):
    ttk.Label(notes_frame, text=note, wraplength=250).grid(row=i, column=0, sticky="w", padx=5, pady=2)



# Frame for image and controls
info_frame = ttk.LabelFrame(app, text="Image", padding=(20, 10))
info_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

# Navigation buttons
backIcon = Image.open(r"back_icon.png")
backImg = ImageTk.PhotoImage(backIcon)
backFrameButton = tk.Button(info_frame, image=backImg, command=previous_image)
backFrameButton.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky="nsew")

nextIcon = Image.open(r"next_icon.png")
nextImg = ImageTk.PhotoImage(nextIcon)
nextFrameButton = tk.Button(info_frame, image=nextImg, command=next_image)
nextFrameButton.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")

# Image display frame
image_frame = tk.Frame(info_frame, width=350, height=480)
image_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

# Initialize the first image
current_image_index = 0
image_paths = ["Version/Copa America TOTT.png"]
image_backgr_paths = ["img\\167930183.png"]
links =["https://www.futwiz.com/en/fc24/player/lionel-messi/22632"]
# Initial values to display on the image
values_to_display = [[
    "Messi",
    "93",
    "98",
    "99",
    "99",
    "46",
    "82",
    "99",
    "ST"
]]



background_image = Image.open(image_paths[current_image_index])
background_image = background_image.resize((322, 450), Image.LANCZOS)
result_image = overlay_images(background_image, image_backgr_paths[current_image_index])
result_image = add_text_to_image(result_image, values_to_display[0])

photo = ImageTk.PhotoImage(result_image)
image_label = ttk.Label(image_frame, image=photo)
image_label.pack()
image_label.bind("<Double-1>", on_image_double_click)

# Label to display the result
result_label = tk.Label(app, text="Your result will appear here.")
result_label.grid(row=3, column=0, columnspan=2)

app.mainloop()
