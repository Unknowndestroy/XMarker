import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk
import os

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not file_path:
        return

    original = Image.open(file_path).convert("RGBA")
    original.save("original_image.png")

    edited = original.copy()
    draw = ImageDraw.Draw(edited)
    width, height = edited.size
    draw.line((0, 0, width, height), fill="red", width=5)
    draw.line((0, height, width, 0), fill="red", width=5)
    edited.save("image.png")

    tk_img = ImageTk.PhotoImage(edited.resize((400, 400)))
    label.config(image=tk_img)
    label.image = tk_img

root = tk.Tk()
root.title("Image X Marker")
root.geometry("450x500")

upload_btn = tk.Button(root, text="Upload Image", command=upload_image, font=("Arial", 14))
upload_btn.pack(pady=20)

label = tk.Label(root)
label.pack()

root.mainloop()
