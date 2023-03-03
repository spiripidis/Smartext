import cv2
import pytesseract
try:
    import tkinter as tk
    import tkinter.filedialog as tkfd
except ImportError:
    import Tkinter as tk
    import tkFileDialog as tkfd


pytesseract.pytesseract.tesseract_cmd = 'Tesseract\\tesseract.exe'


def run_this():
    t2s = tk.Toplevel()
    t2s.title("Optical Character Recognition")
    canvas1 = tk.Canvas(t2s, width=420, height=350, relief='raised')
    canvas1.pack()
    label1 = tk.Label(t2s, text='Optical Character Recognition')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)
    entry = tk.Entry(t2s)
    entry.pack()
    path = tkfd.askopenfilename(initialdir="/Desktop", title="Select file",
                                filetypes=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg")))
    entry.insert('0', path)
    img = cv2.imread(entry.get())
    ocrText = pytesseract.image_to_string(img)
    return ocrText

    #t2s.mainloop()
