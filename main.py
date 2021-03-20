import requests
import tkinter
import tkinter.font
import  tkinter.filedialog

if __name__ == '__main__':
    tk = tkinter.Tk()

    tk.title("SGD")
    tk.geometry("640x400+200+100")
    tk.resizable(False, False)
    tk.config(bg="black")

    font = tkinter.font.Font(size=32)
    labal = tkinter.Label(tk, text="SPIGOT_DOWNLOAD", width=20, height=5, fg="red", bg="black", font=font)
    labal.pack()
    version = tkinter.Entry(tk)
    version.pack()

    def selPath():
        path = tkinter.filedialog.askdirectory()
        print(path)
        return path

    def downSpigot():
        url = 'https://cdn.getbukkit.org/spigot/spigot-' + version.get() + '.jar'
        print(url)
        r = requests.get(url, allow_redirects=True)
        open(selPath() + '/spigot-' + version.get() + '.jar', 'wb').write(r.content)

    button = tkinter.Button(tk, text="DOWNLOAD", command=downSpigot)
    button.pack()

    tk.mainloop()