import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
from time import sleep
import os

video_name = "Videos/Intro.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label,root):
    try:
        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image
    except:
        root.quit()
        os.system("python3 game.py")
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("3CP Studios")
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,root,))
    thread.daemon = 1
    thread.start()
    root.mainloop()
    
