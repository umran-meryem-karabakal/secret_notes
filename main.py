from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from cryptography.fernet import Fernet

def create_file():
    file_name = "my_secret"
    if file_name.strip() == "":
        messagebox.showerror("Hata", "Bilgiler eksik")
    else:
        try:
            with open(file_name, "w") as file:
                file.write("")
            messagebox.showinfo("Başarılı", f"{file_name} dosyası oluşturuldu.")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya oluşturma sırasında bir hata oluştu: {str(e)}")
    with open(file_name, mode="w") as myNewFile:
        myNewFile.write(sn_entry_1.get())  # Parantez ekleyerek sn_entry_1.get() fonksiyonunu çağırın
        myNewFile.write("\n")
        myNewFile.write(sn_text.get("1.0", "end-1c"))  # Aynı şekilde sn_text.get() fonksiyonunu çağırın
    sn_entry_1.delete(0, END)
    sn_entry_2.delete(0,END)
    sn_text.delete(1.0, END)
    key = sn_entry_2.get()  # Kullanıcının girdiği anahtar
    if not key:
        messagebox.showerror("Hata", "Anahtar boş olamaz!")
        return
    cipher_suite = Fernet(key)
    plain_text = sn_text.get("1.0", "end-1c")
    encrypted_text = cipher_suite.encrypt(plain_text.encode())


def write_file():
    pass

def generate_key():
    key = Fernet.generate_key()
    return key


sn_window = Tk()
sn_window.title("screen notes with python")
sn_window.config(padx=20, pady=20)
#sn_window.minsize(width=150, height = 200)

path = "img.png"
original_img = Image.open(path)
resized_img = original_img.resize((100,100))  # Yeni genişlik ve yükseklik değerlerini burada ayarlayabilirsiniz
img = ImageTk.PhotoImage(resized_img)
img_label = Label(image = img)
img_label.pack(fill = "both", expand = "yes")
img_label.config(padx=50, pady=50)

sn_label_1 = Label(text ="enter your title")
sn_label_1.pack()

sn_entry_1 = Entry(width=25)
sn_entry_1.focus()
sn_entry_1.pack()

sn_label_2 = Label(text="enter your secret")
sn_label_2.pack()

sn_text = Text(width=25, height= 10)
sn_text.pack()

sn_label_3 = Label(text= "enter master key")
sn_label_3.pack()

sn_entry_2 = Entry(width=25)
sn_entry_2.pack()

spacer1 = Label(text="")
spacer1.pack()

sn_button_1 = Button(text ="save & encrypt", command=create_file)
sn_button_1.config(width=15,height=1)
sn_button_1.pack()

spacer2 = Label(text="")
spacer2.config(padx=3,pady=0.5)
spacer2.pack()

sn_button_2 = Button(text ="decrypt")
sn_button_2.config(width=15,height=1)
sn_button_2.pack()

sn_window.mainloop()

"""
sorunlar
> text dosyası oluşturma
> text dosyasını şifreleme
"""