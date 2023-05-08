from tkinter import *
from tkinter import ttk, Menu
from tkinter.messagebox import showinfo, showerror, askokcancel
from github import Github


def close_window():
    # if askokcancel is True, close the window
    if askokcancel(title='Close', message='Do you want to close Git Helper?'):
        # this distroys the window
        window.destroy()
# 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


def gitCheck():
    token = git_token_entry.get()
    g = Github(token)
    try:
        logo_text.config(text=g.get_user().name)
        git_token.config(text='Repo :')
        canvas.create_window(50, 250, window=git_token)

        git_token_entry.destroy()
        repo_url = ttk.Entry(window, width=20, style='TEntry')
        canvas.create_window(150, 245, window=repo_url)
        # menu = Menu(window)
        # new_item = Menu(menu, tearoff=0)
        # new_item.add_command(label='Create')
        # new_item.add_separator()
        # new_item.add_command(label='Commit')
        # menu.add_cascade(label='File', menu=new_item)
        # window.config(menu=menu)
    except:
        showerror('Error', 'Check git token')


window = Tk()
window.geometry("400x400")
window.title('Git Helper')

canvas = Canvas(window, width=400, height=400)
canvas.pack()

logo = PhotoImage(file='logo.png')
logo = logo.subsample(5, 5)
canvas.create_image(200, 100, image=logo)

window.iconbitmap(window, 'logo.png')

label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000',
                      font=('Javanese Text', 16))

entry_style = ttk.Style()
entry_style.configure('TEntry', foreground='#000000',
                      font=('Book Antiqua', 22))

button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font='DotumChe')

logo_text = ttk.Label(
    window, text='Git Helper', font=('Edwardian Script ITC', 52))
canvas.create_window(200, 200, window=logo_text)

git_token = ttk.Label(window, text='Git Token :', style='TLabel')
canvas.create_window(100, 300, window=git_token)

git_token_entry = ttk.Entry(window, width=30, style='TEntry')
canvas.create_window(260, 295, window=git_token_entry)

git_check_button = ttk.Button(
    window, text='Check', style='TButton', command=gitCheck)
canvas.create_window(200, 350, window=git_check_button)

window.protocol('WM_DELETE_WINDOW', close_window)

window.mainloop()
