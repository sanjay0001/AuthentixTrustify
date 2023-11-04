import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compare_images(image1, image2):
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))

    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    ssi_index = ssim(gray_img1, gray_img2)

    err = np.sum((gray_img1.astype("float") - gray_img2.astype("float")) ** 2)
    err /= float(gray_img1.shape[0] * gray_img2.shape[1])

    return ssi_index, err

def select_image(index):
    path = filedialog.askopenfilename()
    if index == 1:
        global image_path1
        image_path1 = path
        load_image(image_path1, 1)
    else:
        global image_path2
        image_path2 = path
        load_image(image_path2, 2)

def load_image(path, index):
    img = Image.open(path)
    img = img.resize((250, 250), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img)
    if index == 1:
        panel1.config(image=img)
        panel1.image = img
    else:
        panel2.config(image=img)
        panel2.image = img

def compare_signatures():
    ssi_index, mse = compare_images(image_path1, image_path2)
    ssi_threshold = 0.7  
    mse_threshold = 1000 

    if ssi_index > ssi_threshold and mse < mse_threshold:
        result_label.config(text="The signatures match.")
    else:
        result_label.config(text="The signatures do not match.")

root = tk.Tk()
root.title("Signature Comparison Module")

select_button1 = tk.Button(root, text="Select Image 1", command=lambda: select_image(1))
select_button1.pack()
select_button2 = tk.Button(root, text="Select Image 2", command=lambda: select_image(2))
select_button2.pack()

panel1 = tk.Label(root)
panel1.pack()
panel2 = tk.Label(root)
panel2.pack()

compare_button = tk.Button(root, text="Compare Signatures", command=compare_signatures)
compare_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
