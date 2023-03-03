

'''WHEN CONVERTING TO EXE HID IMPORT pkg_resources.py2_warn,pyttsx3.drivers,pyttsx3.drivers,pyttsx3.drivers.dummy,
pyttsx3.drivers.espeak,
pyttsx3.drivers.nsss,
pyttsx3.drivers.sapi5 !!!!!!!!!!!!!!!!!!!!!!!'''

#'pyttsx3.drivers.dummy',
#'pyttsx3.drivers.espeak',
#'pyttsx3.drivers.nsss',
#'pyttsx3.drivers.sapi5',

'''IMPORTS'''

from tkinter import *
from tkinter import filedialog as filedialog  # filedialog allows user to select where they want to save the file.
from tkinter import simpledialog as simpledialog
from tkinter import messagebox as messagebox
from PIL import Image, ImageTk
import os
import tkinter as tk
import AEScrypto as AES
import sentiment_analysis
import OpticalTextRecognition
import wikiCrawler
import syn_anto
from HTR.src import main as _htr


# creating the root of the window.
master = Tk()
master.iconbitmap("icons/window_icon.ico")
master.title("*Untitled - Smartext")
master.geometry("600x550")

# setting resizable window
master.resizable(True, True)
master.minsize(600, 550)  # minimimum size possible

# --------------- METHODS ---------------- #

# MAIN MENU METHODS
file_name = ""  # Current file name.
current_font_family = "Arial"
current_font_size = 12
fontColor = '#000000'
fontBackground = '#FFFFFF'

#create new file
def new(event=None):
    file_name = ""
    ans = messagebox.askquestion(title="Save File", message="Would you like to save this file?")
    if ans is True:
        save()
    delete_all()

#open existing file
def open_file(event=None):
    new()
    file = filedialog.askopenfile()
    global file_name
    file_name = file.name
    text.insert(INSERT, file.read())

#save current file
def save(event=None):
    global file_name
    if file_name == "":
        path = filedialog.asksaveasfilename()
        file_name = path
    master.title(file_name + " - Smartext")
    write = open(file_name, mode='w')
    write.write(text.get("1.0", END))

#save current file as
def save_as(event=None):
    if file_name == "":
        save()
        return "break"
    f = filedialog.asksaveasfile(mode='w+')
    if f is None:
        return
    text2save = str(text.get(1.0, END))
    f.write(text2save)
    f.close()

#open sentiment analysis window
def sent_analysis(event=None):
    sentiment_analysis.run_this()

#open optical character recognition window
def ocr_input(event=None):
    text.insert(END, OpticalTextRecognition.run_this())

#open handwritten text recognitio window
def htr_input(event=None):
    import numpy as np
    #import htr_main
    """process = subprocess.Popen(['cd', 'HTR'], stdin =subprocess.PIPE,stdout=subprocess.PIPE,shell=False)
    process.stdin.write("cd src")
    process.stdin.write("python main.py")
    process.stdin.close()"""
    _htr.main()
    #subprocess.call('cd HTR && cd src && python main.py')

#start dictating text
def text2speech(event=None):
    #import text2speech
    import NEWt2s
    some = text.get("1.0", END)
    thistext = some
    NEWt2s.text2speech(thistext)

#start microphone to transcribe text
def start_speech2text(event=None):
    import speech2text
    text.insert(END, speech2text.Start())

# AES encrypt a file with password
def encrypt(event=None):
    f = filedialog.askopenfile()
    base = os.path.basename(f.name)
    split = os.path.splitext(base)
    final = os.path.join(split[0] + '.txt.aes')
    encrypted = os.path.join('texts/' + final)
    password = simpledialog.askstring("AES", "Enter your password:")
    AES.AESsave(f.name, encrypted, password, 64*1024)

# AES decrypt a file with password
def decrypt(event=None):
    f = filedialog.askopenfile()
    base = os.path.basename(f.name)
    split = os.path.splitext(base)
    final = os.path.join(split[0])
    decrypted = os.path.join('texts/' + final)
    password = simpledialog.askstring("AES", "Enter your password:")
    AES.AESopen(f.name, decrypted, password, 60*1024)

# Set UI to dark theme
def dark_mode(event=None):
    textarea_dark()
    toolbar.configure(background='#ffff80')
    formattingbar.configure(background='#ffff4d')
    new_button.configure(background = "#ffc14d")
    file_menu.configure(background='#cccccc')
    edit_menu.configure(background='#cccccc')
    tool_menu.configure(background='#cccccc')
    lexer_menu.configure(background='#cccccc')
    dark_light.configure(background='#cccccc')
    help_menu.configure(background='#cccccc')
    new_button.configure(background = "#ffc14d")
    save_button.configure(background = "#ffc14d")
    undo_button.configure(background = "#ffc14d")
    redo_button.configure(background = "#ffc14d")
    open_button.configure(background = "#ffc14d")
    cut_button.configure(background = "#ffc14d")
    copy_button.configure(background = "#ffc14d")
    find_button.configure(background = "#ffc14d")
    paste_button.configure(background = "#ffc14d")
    align_justify_button.configure(background = "#ffc14d")
    align_center_button.configure(background = "#ffc14d")
    align_left_button.configure(background = "#ffc14d")
    align_right_button.configure(background = "#ffc14d")
    wiki_search.configure(background = "#ffc14d")
    text2speech.configure(background = "#ffc14d")
    speech2text.configure(background = "#ffc14d")
    ocr.configure(background = "#ffc14d")
    htr.configure(background = "#ffc14d")
    sentiment_analysis.configure(background = "#ffc14d")
    status.configure(background = '#ffff4d')

# Set UI to light theme
def light_mode(event=None):
    textarea_light()
    toolbar.configure(background='#f0f0f0')
    formattingbar.configure(background='#f0f0f0')
    new_button.configure(background = "#f0f0f0")
    file_menu.configure(background='#f0f0f0')
    edit_menu.configure(background='#f0f0f0')
    tool_menu.configure(background='#f0f0f0')
    lexer_menu.configure(background='#f0f0f0')
    dark_light.configure(background='#f0f0f0')
    help_menu.configure(background='#f0f0f0')
    new_button.configure(background = "#f0f0f0")
    save_button.configure(background = "#f0f0f0")
    undo_button.configure(background = "#f0f0f0")
    redo_button.configure(background = "#f0f0f0")
    open_button.configure(background = "#f0f0f0")
    cut_button.configure(background = "#f0f0f0")
    copy_button.configure(background = "#f0f0f0")
    find_button.configure(background = "#f0f0f0")
    paste_button.configure(background = "#f0f0f0")
    align_justify_button.configure(background = "#f0f0f0")
    align_center_button.configure(background = "#f0f0f0")
    align_left_button.configure(background = "#f0f0f0")
    align_right_button.configure(background = "#f0f0f0")
    wiki_search.configure(background = "#f0f0f0")
    text2speech.configure(background = "#f0f0f0")
    speech2text.configure(background = "#f0f0f0")
    ocr.configure(background = "#f0f0f0")
    htr.configure(background = "#f0f0f0")
    sentiment_analysis.configure(background = "#f0f0f0")
    status.configure(background = "#f0f0f0")

#Set textbox to light theme
def textarea_light(event=None):
    text.configure(background = "white",fg = "black",insertbackground = "black")

# Set textbox to dark theme
def textarea_dark(event=None):
    text.configure(background = "black",fg = "white",insertbackground = "white")

      
new_name = ""  # Used for renaming the file
# rename a file
def rename(event=None):
    global file_name
    if file_name == "":
        open_file()

    arr = file_name.split('/')
    path = ""
    for i in range(0, len(arr) - 1):
        path = path + arr[i] + '/'

    new_name = simpledialog.askstring("Rename", "Enter new name:")
    os.rename(file_name, str(path) + str(new_name))
    file_name = str(path) + str(new_name)
    master.title(file_name + " - Smartext")
# exit application
def close(event=None):
    save()
    master.quit()


# EDIT MENU METHODS

#cut text
def cut(event=None):
    # first clear the previous text on the clipboard.
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    # index of the first and yhe last letter of our selection.
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)

#copy text
def copy(event=None):
    # first clear the previous text on the clipboard.
    print
    text.index(SEL_FIRST)
    print
    text.index(SEL_LAST)
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())

#paste text
def paste(event=None):
    # get gives everything from the clipboard and paste it on the current cursor position
    # it does'nt removes it from the clipboard.
    text.insert(INSERT, master.clipboard_get())

#delete text
def delete(event=None):
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)

#undo most recent change
def undo(event=None):
    text.edit_undo()

#redo most recent change
def redo(event=None):
    text.edit_redo()

# highlight all text
def select_all(event=None):
    text.tag_add(SEL, "1.0", END)

#delete all text
def delete_all(event=None):
    text.delete(1.0, END)


# TOOLS MENU METHODS
# Adding Search Functionality

def check(value):
    text.tag_remove('found', '1.0', END)
    text.tag_config('found', foreground='red')
    list_of_words = value.split(' ')
    for word in list_of_words:
        idx = '1.0'
        while idx:
            idx = text.search(word, idx, nocase=1, stopindex=END)
            if idx:
                lastidx = '%s+%dc' % (idx, len(word))
                text.tag_add('found', idx, lastidx)
                print
                lastidx
                idx = lastidx


# implementation of search dialog box - calling the check method to search and find_text_cancel_button to close it
def find_text(event=None):
    search_toplevel = Toplevel(master)
    search_toplevel.title('Find Text')
    search_toplevel.transient(master)
    search_toplevel.resizable(False, False)
    Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
    search_entry_widget = Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    Button(search_toplevel, text="Ok", underline=0, command=lambda: check(search_entry_widget.get())).grid(row=0,
                                                                                                           column=2,
                                                                                                           sticky='e' + 'w',
                                                                                                           padx=2,
                                                                                                           pady=5)
    Button(search_toplevel, text="Cancel", underline=0, command=lambda: find_text_cancel_button(search_toplevel)).grid(
        row=0, column=4, sticky='e' + 'w', padx=2, pady=2)


# remove search tags and destroys the search box
def find_text_cancel_button(search_toplevel):
    text.tag_remove('found', '1.0', END)
    search_toplevel.destroy()
    return "break"


# FORMAT BAR METHODS


# To make align functions work properly
def remove_align_tags(event=None):
    all_tags = text.tag_names(index=None)
    if "center" in all_tags:
        text.tag_remove("center", "1.0", END)
    if "left" in all_tags:
        text.tag_remove("left", "1.0", END)
    if "right" in all_tags:
        text.tag_remove("right", "1.0", END)


# align_center
def align_center(event=None):
    remove_align_tags()
    text.tag_configure("center", justify='center')
    text.tag_add("center", 1.0, "end")


# align_justify
def align_justify(event=None):
    remove_align_tags()


# align_left
def align_left(event=None):
    remove_align_tags()
    text.tag_configure("left", justify='left')
    text.tag_add("left", 1.0, "end")


# align_right
def align_right(event=None):
    remove_align_tags()
    text.tag_configure("right", justify='right')
    text.tag_add("right", 1.0, "end")


def wiki(event=None):
    searchtoken = simpledialog.askstring("Wikipedia search", "Enter your term:")
    search_result = wikiCrawler.wiki_run(searchtoken)
    result=Toplevel(master)
    result.title("Wikipedia Search Result")
    result.transient(master)
    result.resizable(TRUE, TRUE)
    final = tk.Text(result, wrap=WORD)
    final.insert('1.0', search_result)
    final.pack()


def lexdef(event=None):
    word = simpledialog.askstring("Definition", "Enter word:")
    def_result=syn_anto.definition(word)
    result = Toplevel(master)
    result.title("Definition")
    result.transient(master)
    result.resizable(TRUE, TRUE)
    final = tk.Text(result, wrap=WORD)
    final.insert('1.0', def_result)
    final.pack()


def lexsyn(event=None):
    word = simpledialog.askstring("Synonyms", "Enter word:")
    syn_result = syn_anto.synonym(word)
    result = Toplevel(master)
    result.title("Synonyms List")
    result.transient(master)
    result.resizable(TRUE, TRUE)
    final = tk.Text(result, wrap=WORD)
    final.insert('1.0', syn_result)
    final.pack()


def lexant(event=None):
    word = simpledialog.askstring("Antonyms", "Enter word:")
    ant_result = syn_anto.antonym(word)
    result = Toplevel(master)
    result.title("Antonyms List")
    result.transient(master)
    result.resizable(TRUE, TRUE)
    final = tk.Text(result, wrap=WORD)
    final.insert('1.0', ant_result)
    final.pack()



# called when <<combobox>> event is called
# ------------- CREATING - MENUBAR AND ITS MENUS, TOOLS BAR, FORMAT BAR, STATUS BAR AND TEXT AREA -----------#


# TOOLBAR
toolbar = Frame(master, pady=2)

# TOOLBAR BUTTONS
# new
new_button = Button(name="toolbar_b2", borderwidth=1, command=new, width=20, height=20)
photo_new = Image.open("icons/new.png")
photo_new = photo_new.resize((18, 18), Image.ANTIALIAS)
image_new = ImageTk.PhotoImage(photo_new)
new_button.config(image=image_new)
new_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# save
save_button = Button(name="toolbar_b1", borderwidth=1, command=save, width=20, height=20)
photo_save = Image.open("icons/save.png")
photo_save = photo_save.resize((18, 18), Image.ANTIALIAS)
image_save = ImageTk.PhotoImage(photo_save)
save_button.config(image=image_save)
save_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# open
open_button = Button(name="toolbar_b3", borderwidth=1, command=open_file, width=20, height=20)
photo_open = Image.open("icons/open.png")
photo_open = photo_open.resize((18, 18), Image.ANTIALIAS)
image_open = ImageTk.PhotoImage(photo_open)
open_button.config(image=image_open)
open_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# copy
copy_button = Button(name="toolbar_b4", borderwidth=1, command=copy, width=20, height=20)
photo_copy = Image.open("icons/copy.png")
photo_copy = photo_copy.resize((18, 18), Image.ANTIALIAS)
image_copy = ImageTk.PhotoImage(photo_copy)
copy_button.config(image=image_copy)
copy_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# cut
cut_button = Button(name="toolbar_b5", borderwidth=1, command=cut, width=20, height=20)
photo_cut = Image.open("icons/cut.png")
photo_cut = photo_cut.resize((18, 18), Image.ANTIALIAS)
image_cut = ImageTk.PhotoImage(photo_cut)
cut_button.config(image=image_cut)
cut_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# paste
paste_button = Button(name="toolbar_b6", borderwidth=1, command=paste, width=20, height=20)
photo_paste = Image.open("icons/paste.png")
photo_paste = photo_paste.resize((18, 18), Image.ANTIALIAS)
image_paste = ImageTk.PhotoImage(photo_paste)
paste_button.config(image=image_paste)
paste_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# redo
redo_button = Button(name="toolbar_b7", borderwidth=1, command=redo, width=20, height=20)
photo_redo = Image.open("icons/redo.png")
photo_redo = photo_redo.resize((18, 18), Image.ANTIALIAS)
image_redo = ImageTk.PhotoImage(photo_redo)
redo_button.config(image=image_redo)
redo_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# undo
undo_button = Button(name="toolbar_b8", borderwidth=1, command=undo, width=20, height=20)
photo_undo = Image.open("icons/undo.png")
photo_undo = photo_undo.resize((18, 18), Image.ANTIALIAS)
image_undo = ImageTk.PhotoImage(photo_undo)
undo_button.config(image=image_undo)
undo_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# find
find_button = Button(name="toolbar_b9", borderwidth=1, command=find_text, width=20, height=20)
photo_find = Image.open("icons/find.png")
photo_find = photo_find.resize((18, 18), Image.ANTIALIAS)
image_find = ImageTk.PhotoImage(photo_find)
find_button.config(image=image_find)
find_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# align_justify
align_justify_button = Button(name="formatbar_b8", borderwidth=1, command=align_justify, width=20, height=20)
photo_align_justify = Image.open("icons/align-justify.png")
photo_align_justify = photo_align_justify.resize((18, 18), Image.ANTIALIAS)
image_align_justify = ImageTk.PhotoImage(photo_align_justify)
align_justify_button.config(image=image_align_justify)
align_justify_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# align_left
align_left_button = Button(name="formatbar_b9", borderwidth=1, command=align_left, width=20, height=20)
photo_align_left = Image.open("icons/align-left.png")
photo_align_left = photo_align_left.resize((18, 18), Image.ANTIALIAS)
image_align_left = ImageTk.PhotoImage(photo_align_left)
align_left_button.config(image=image_align_left)
align_left_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# align_center
align_center_button = Button(name="formatbar_b7", borderwidth=1, command=align_center, width=20, height=20)
photo_align_center = Image.open("icons/align-center.png")
photo_align_center = photo_align_center.resize((18, 18), Image.ANTIALIAS)
image_align_center = ImageTk.PhotoImage(photo_align_center)
align_center_button.config(image=image_align_center)
align_center_button.pack(in_=toolbar, side="left", padx=4, pady=4)

# align_right
align_right_button = Button(name="formatbar_b10", borderwidth=1, command=align_right, width=20, height=20)
photo_align_right = Image.open("icons/align-right.png")
photo_align_right = photo_align_right.resize((18, 18), Image.ANTIALIAS)
image_align_right = ImageTk.PhotoImage(photo_align_right)
align_right_button.config(image=image_align_right)
align_right_button.pack(in_=toolbar, side="left", padx=4, pady=4)


# FORMATTING BAR
formattingbar = Frame(master, padx=2, pady=2)

# FORMATBAR BUTTONS

#Wikipedia
wiki_search = Button(name="toolbar_b10", borderwidth=1, command=wiki, width=20, height=20)
photo_wiki = Image.open("icons/wiki_logo.png")
photo_wiki = photo_wiki.resize((18, 18), Image.ANTIALIAS)
image_wiki = ImageTk.PhotoImage(photo_wiki)
wiki_search.config(image=image_wiki)
wiki_search.pack(in_=formattingbar, side="left", padx=4, pady=4)

#Sentiment Analisys
sentiment_analysis = Button(name="toolbar_b11", borderwidth=1, command=sentiment_analysis.run_this, width=20, height=20)
photo_sentiment = Image.open("icons/sentiment.png")
photo_sentiment = photo_sentiment.resize((18, 18), Image.ANTIALIAS)
image_sentiment = ImageTk.PhotoImage(photo_sentiment)
sentiment_analysis.config(image=image_sentiment)
sentiment_analysis.pack(in_=formattingbar, side="left", padx=4, pady=4)

#SpeechToText
speech2text = Button(name="toolbar_b12", borderwidth=1, command=start_speech2text, width=20, height=20)
photo_speech2text = Image.open("icons/speech2text.png")
photo_speech2text = photo_speech2text.resize((18, 18), Image.ANTIALIAS)
image_speech2text = ImageTk.PhotoImage(photo_speech2text)
speech2text.config(image=image_speech2text)
speech2text.pack(in_=formattingbar, side="left", padx=4, pady=4)

#TextToSpeech
text2speech = Button(name="toolbar_b13", borderwidth=1, command=text2speech, width=20, height=20)
photo_text2speech = Image.open("icons/text2speech.png")
photo_text2speech = photo_text2speech.resize((18, 18), Image.ANTIALIAS)
image_text2speech = ImageTk.PhotoImage(photo_text2speech)
text2speech.config(image=image_text2speech)
text2speech.pack(in_=formattingbar, side="left", padx=4, pady=4)

#OpticalCharacterRecognition
ocr = Button(name="toolbar_b14", borderwidth=1, command=ocr_input, width=20, height=20)
photo_ocr = Image.open("icons/ocr.png")
photo_ocr = photo_ocr.resize((18, 18), Image.ANTIALIAS)
image_ocr = ImageTk.PhotoImage(photo_ocr)
ocr.config(image=image_ocr)
ocr.pack(in_=formattingbar, side="left", padx=4, pady=4)

#HandwrittenTextRecognition
htr = Button(name="toolbar_b15", borderwidth=1, command=htr_input, width=20, height=20)
photo_htr = Image.open("icons/htr.png")
photo_htr = photo_htr.resize((18, 18), Image.ANTIALIAS)
image_htr = ImageTk.PhotoImage(photo_htr)
htr.config(image=image_htr)
htr.pack(in_=formattingbar, side="left", padx=4, pady=4)

# STATUS BAR
status = Label(master, text="", bd=1, relief=SUNKEN, anchor=W)

# CREATING TEXT AREA - FIRST CREATED A FRAME AND THEN APPLIED TEXT OBJECT TO IT.
text_frame = Frame(master, borderwidth=1, relief="sunken")

text = Text(wrap="word", font=("Arial", 12), borderwidth=0, highlightthickness=0, undo=True) ############### dark mode
text.pack(in_=text_frame, side="left", fill="both", expand=True)  # pack text object.

# PACK TOOLBAR, FORMATBAR, STATUSBAR AND TEXT FRAME.
toolbar.pack(side="top", fill="x")
formattingbar.pack(side="top", fill="x")
status.pack(side="bottom", fill="x")
text_frame.pack(side="bottom", fill="both", expand=True)
text.focus_set()

# MENUBAR CREATION

menu = Menu(master)
master.config(menu=menu)

# File menu.
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu, underline=0)

file_menu.add_command(label="New", command=new, compound='left', image=image_new, accelerator='Ctrl+N', underline=0)  # command passed is here the method defined above.
file_menu.add_command(label="Open", command=open_file, compound='left', image=image_open, accelerator='Ctrl+O', underline=0)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save, compound='left', image=image_save, accelerator='Ctrl+S', underline=0)
file_menu.add_command(label="Save As", command=save_as, compound='left', image=image_save, accelerator='Ctrl+Shift+S', underline=1)
renamee = PhotoImage(file = r"icons/rename.png")
file_menu.add_command(label="Rename", command=rename,compound='left', image=renamee, accelerator='Ctrl+Shift+R', underline=0)
encryptt = PhotoImage(file = r"icons/encrypt.png")
file_menu.add_command(label="Encrypt", command=encrypt, compound='left', image=encryptt, accelerator='Ctrl+Shift+E', underline=0)
decryptt = PhotoImage(file = r"icons/decrypt.png")
file_menu.add_command(label="Decrypt", command=decrypt, compound='left', image=decryptt, accelerator='Ctrl+Shift+D', underline=0)
file_menu.add_separator()
closee = PhotoImage(file = r"icons/close.png")
file_menu.add_command(label="Close", command=close, compound='left', image=closee, accelerator='Alt+F4', underline=0)

# Edit Menu.
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu, underline=0)

edit_menu.add_command(label="Undo", command=undo, compound='left', image=image_undo, accelerator='Ctrl+Z', underline=0)
edit_menu.add_command(label="Redo", command=redo, compound='left', image=image_redo, accelerator='Ctrl+Y', underline=0)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut, compound='left', image=image_cut, accelerator='Ctrl+X', underline=0)
edit_menu.add_command(label="Copy", command=copy, compound='left', image=image_copy, accelerator='Ctrl+C', underline=1)
edit_menu.add_command(label="Paste", command=paste, compound='left', image=image_paste, accelerator='Ctrl+P', underline=0)
deletee = PhotoImage(file = r"icons/delete.png")
edit_menu.add_command(label="Delete", command=delete, compound='left', image=deletee, accelerator='Ctrl+Shift+D', underline=0)
edit_menu.add_separator()
select = PhotoImage(file = r"icons/select_all.png")
edit_menu.add_command(label="Select All", command=select_all,  compound='left', image=select, accelerator='Ctrl+A', underline=0)
clear = PhotoImage(file = r"icons/clear_all.png")
edit_menu.add_command(label="Clear All", command=delete_all,  compound='left', image=clear, accelerator='Ctrl+D', underline=6)

# Tool Menu
tool_menu = Menu(menu)
menu.add_cascade(label="Tools", menu=tool_menu, underline=0)
tool_menu.add_command(label="Search", command=find_text, compound='left', image=image_find, accelerator='Ctrl+F')

#Dictionary
lexer_menu = Menu(menu)
menu.add_cascade(label="Dictionary", menu=lexer_menu, underline=0)
syn_ant = PhotoImage(file = r"icons/syn_ant.png")
lexer_menu.add_command(label="Synonyms", command=lexsyn, compound='left', image=syn_ant, accelerator='Ctrl+M') 
lexer_menu.add_command(label="Antonyms", command=lexant, compound='left', image=syn_ant, accelerator='Ctrl+J')
definition = PhotoImage(file = r"icons/definition.png")
lexer_menu.add_command(label="Definitions", command=lexdef, compound='left', image=definition, accelerator='Ctrl+K')

#Dark-Mode/Light-Mode
dark_light = Menu(menu)
menu.add_cascade(label="Vision Mode", menu=dark_light, underline=0)
dark = PhotoImage(file = r"icons/dark_mode.png")
dark_light.add_command(label="Dark Mode", command=dark_mode, compound='left', image=dark, accelerator='Ctrl+U')
light = PhotoImage(file = r"icons/light_mode.png")
dark_light.add_command(label="Light Mode", command=light_mode, compound='left', image=light, accelerator='Ctrl+L')

# Help Menu
def about(event=None):
    messagebox.showinfo("About", "Smartext\nCreated in Python using Tkinter\nContact Us at : \n t.michelioudakis@mc-class.gr \n l.lalagkos@mc-class.gr\na.basho@mc-class.gr")

help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu, underline=0)
aboutt = PhotoImage(file = r"icons/about.png")
help_menu.add_command(label="About", command=about, compound='left', image=aboutt, accelerator='Ctrl+B', underline=0)


# ----- BINDING ALL KEYBOARD SHORTCUTS ---------- #
text.bind('<Control-n>', new)
text.bind('<Control-N>', new)

text.bind('<Control-o>', open_file)
text.bind('<Control-O>', open_file)

text.bind('<Control-s>', save)
text.bind('<Control-S>', save)

text.bind('<Control-Shift-s>', save_as)
text.bind('<Control-Shift-S>', save_as)

text.bind('<Control-r>', rename)
text.bind('<Control-R>', rename)

text.bind('<Control-Shift-d>', delete)
text.bind('<Control-Shift-D>', delete)

text.bind('<Alt-F4>', close)
text.bind('<Alt-F4>', close)

text.bind('<Control-x>', cut)
text.bind('<Control-X>', cut)

text.bind('<Control-c>', copy)
text.bind('<Control-C>', copy)

text.bind('<Control-p>', paste)
text.bind('<Control-P>', paste)

text.bind('<Control-Shift-e>', encrypt)
text.bind('<Control-Shift-E>', encrypt)

text.bind('<Control-Shift-d>', decrypt)
text.bind('<Control-Shift-D>', decrypt)

text.bind('<Control-a>', select_all)
text.bind('<Control-A>', select_all)

text.bind('<Control-b>', about)
text.bind('<Control-B>', about)

text.bind('<Control-u>', dark_mode)
text.bind('<Control-U>', dark_mode)

text.bind('<Control-l>', light_mode)
text.bind('<Control-L>', light_mode)

text.bind('<Control-m>', lexsyn)
text.bind('<Control-M>', lexsyn)

text.bind('<Control-j>', lexant)
text.bind('<Control-J>', lexant)

text.bind('<Control-k>', lexdef)
text.bind('<Control-K>', lexdef)

text.bind('<Control-f>', find_text)
text.bind('<Control-F>', find_text)

text.bind('<Control-d>', clear)
text.bind('<Control-D>', clear)

text.bind('<Control-Shift-l>', align_left)
text.bind('<Control-Shift-L>', align_left)

text.bind('<Control-Shift-r>', align_right)
text.bind('<Control-Shift-R>', align_right)

text.bind('<Control-Shift-c>', align_center)
text.bind('<Control-Shift-C>', align_center)

text.bind('<Control-w>', wiki)
text.bind('<Control-W>', wiki)

text.bind('<Control-t>', text2speech)
text.bind('<Control-T>', text2speech)

text.bind('<Control-Shift-t>', start_speech2text)
text.bind('<Control-Shift-T>', start_speech2text)

text.bind('<Control-Shift-o>', ocr_input)
text.bind('<Control-Shift-O>', ocr_input)

text.bind('<Control-Shift-h>', htr_input)
text.bind('<Control-Shift-H>', htr_input)

'''text.bind('<Shift-s>', sent_analysis)
text.bind('<Shift-S>', sent_analysis)'''


# ---------- SETTING EVENTS FOR THE STATUS BAR -------------- #
def on_enter(event, str):
    status.configure(text=str)


def on_leave(event):
    status.configure(text="")


new_button.bind("<Enter>", lambda event, str="New, Command - Ctrl+N": on_enter(event, str))
new_button.bind("<Leave>", on_leave)

wiki_search.bind("<Enter>", lambda event, str="Wikipedia Search, Command - Ctrl+W": on_enter(event, str))
wiki_search.bind("<Leave>", on_leave)

text2speech.bind("<Enter>", lambda event, str="Text To Speech": on_enter(event, str))
text2speech.bind("<Leave>", on_leave)

speech2text.bind("<Enter>", lambda event, str="Speech To Text, Command - Control+Shift+T": on_enter(event, str))
speech2text.bind("<Leave>", on_leave)

ocr.bind("<Enter>", lambda event, str="Optical Character Recognition, Command - Ctrl+Shift+O": on_enter(event, str))
ocr.bind("<Leave>", on_leave)

htr.bind("<Enter>", lambda event, str="Handwritten Text Recognition, Command - Ctrl+Shift+H": on_enter(event, str))
htr.bind("<Leave>", on_leave)

sentiment_analysis.bind("<Enter>", lambda event, str="Sentiment Analysis": on_enter(event, str))
sentiment_analysis.bind("<Leave>", on_leave)

save_button.bind("<Enter>", lambda event, str="Save, Command - Ctrl+S": on_enter(event, str))
save_button.bind("<Leave>", on_leave)

open_button.bind("<Enter>", lambda event, str="Open, Command - Ctrl+O": on_enter(event, str))
open_button.bind("<Leave>", on_leave)

copy_button.bind("<Enter>", lambda event, str="Copy, Command - Ctrl+C": on_enter(event, str))
copy_button.bind("<Leave>", on_leave)

cut_button.bind("<Enter>", lambda event, str="Cut, Command - Ctrl+X": on_enter(event, str))
cut_button.bind("<Leave>", on_leave)

paste_button.bind("<Enter>", lambda event, str="Paste, Command - Ctrl+P": on_enter(event, str))
paste_button.bind("<Leave>", on_leave)

undo_button.bind("<Enter>", lambda event, str="Undo, Command - Ctrl+Z": on_enter(event, str))
undo_button.bind("<Leave>", on_leave)

redo_button.bind("<Enter>", lambda event, str="Redo, Command - Ctrl+Y": on_enter(event, str))
redo_button.bind("<Leave>", on_leave)

find_button.bind("<Enter>", lambda event, str="Find, Command - Ctrl+F": on_enter(event, str))
find_button.bind("<Leave>", on_leave)

align_justify_button.bind("<Enter>", lambda event, str="Justify": on_enter(event, str))
align_justify_button.bind("<Leave>", on_leave)

align_left_button.bind("<Enter>", lambda event, str="Align Left, Command - Control-Shift-L": on_enter(event, str))
align_left_button.bind("<Leave>", on_leave)

align_right_button.bind("<Enter>", lambda event, str="Align Right, Command - Control-Shift-R": on_enter(event, str))
align_right_button.bind("<Leave>", on_leave)

align_center_button.bind("<Enter>", lambda event, str="Align Center, Command - Control-Shift-C": on_enter(event, str))
align_center_button.bind("<Leave>", on_leave)


# MAINLOOP OF THE PROGRAM
master.mainloop()
