from tkinter import * 
from tkinter import ttk
from insta import insta_srcapping
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox

def destroy_window():
    browse.place_forget()
    
def read_data():
    
    global username, password, target_username, file_name, location, insta_list

    username_data   = username.get()
    password_data   = password.get()
    target_username_data = target_username.get()
    file_name_data  = file_name.get()
    location_data   = location.get()
    insta_list_data = insta_list.get()

    if(insta_list_data == "Followers"):
        insta_list_data = 0
    elif(insta_list_data == "Following"):
        insta_list_data = 1
    else:
        insta_list_data = 2
        
    message = insta_srcapping(username_data, password_data, target_username_data, insta_list_data, file_name_data, location_data)
    messagebox.showinfo("Information", message)


def file_location():
    
    global folder_path, location , canvas1
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    location.delete(0,END)
    location.insert(0, filename)


if __name__ == "__main__":
    window = Tk()

    window.title("Instagram lists Scrapper")
    window.configure(width=800, height=500)
    window.configure(bg='lightgray')
    window.eval('tk::PlaceWindow . center')
    window.resizable(False, False)

    canvas1 = Canvas(window, width=800, height=420, bg='white')
    canvas1.pack(fill = "both", expand = True)
    img = ImageTk.PhotoImage(Image.open("background.jpg")) 
    canvas1.create_image( 0, 0, image = img, anchor = "nw")

    canvas1.create_text(90, 50, text="Username:", fill="white", font=('Helvetica 16 bold'))
    username = Entry(canvas1, width=20, font=("Helvetica", 14))
    username.place(x=150,y=38)

    canvas1.create_text(460, 50, text="Password:", fill="white", font=('Helvetica 16 bold'))
    password = Entry(canvas1, width=20, font=("Helvetica", 14))
    password.place(x=520,y=38)

    canvas1.create_text(126, 118, text="Target username:", fill="white", font=('Helvetica 16 bold'))
    target_username = Entry(canvas1, width=20, font=("Helvetica", 14))
    target_username.place(x=230,y=107)

    canvas1.create_text(550, 120, text="List to scrape: ", fill="white", font=('Helvetica 16 bold'))
    insta_list = ttk.Combobox(canvas1, 
                        values=["Followers", "Following", "Both"], font=('Helvetica 14 bold'), width=9)
    insta_list.current(0)
    insta_list.config(state = "readonly")
    insta_list.place(x=625,y=107)

    canvas1.create_text(212, 180, text="Excel file name (with .xlsx or .csv): ", fill="white", font=('Helvetica 16 bold'))
    file_name = Entry(canvas1, width=20, font=("Helvetica", 14))
    file_name.place(x=400,y=170)
    
    canvas1.create_text(200, 240, text="Choose where to save your file: ", fill="white", font=('Helvetica 16 bold'))
    location = Entry(canvas1, width=40, font=("Helvetica", 14))
    location.place(x=40,y=280)

    folder_path = StringVar()
    browse = Button(canvas1, text="Browse", width=7, font=("Helvetica", 10), command=file_location)
    browse.place(x=500,y=280)

    scrapeb = Button(canvas1, text="Scrape", width=15, font=("Helvetica", 10), bg="Green", fg="white", command=read_data)
    scrapeb.place(x=320,y=370)
    """
    browse = Button(canvas1, text="Browse", width=7, font=("Helvetica", 10), command=destroy_window)
    browse.place(x=550,y=250)"""
    window.mainloop()