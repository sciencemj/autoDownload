import os
import shutil
import time
import threading
import requests
import tkinter
import tkinter.font
import tkinter.filedialog
from zipfile import ZipFile
if __name__ == '__main__':
    # isRepeat = [False]
    tk = tkinter.Tk()

    tk.title("SGD")
    tk.geometry("640x400+200+100")
    tk.resizable(False, False)
    tk.config(bg="black")

    font = tkinter.font.Font(size=32)
    labal = tkinter.Label(tk, text="SPIGOT_DOWNLOAD", width=20, height=5, fg="red", bg="black", font=font)
    labal.pack()

    isrepeat = tkinter.Label(tk, text="REPEAT = FALSE", fg="red", bg="black")
    isrepeat.pack()
    
    def turnOn():
        isRepeat = False

        def turnOn_():
            nonlocal isRepeat
            if isRepeat:
                isRepeat = False
                isrepeat.config(text="REPEAT = FALSE")
            else:
                isRepeat = True
                isrepeat.config(text="REPEAT = TRUE")
                repeatDown()
        return turnOn_
    
            
    version = tkinter.Entry(tk)
    version.pack()

    def selPath():
        path = tkinter.filedialog.askdirectory()
        print(path)
        version.insert(0, path)

    selectPath = tkinter.Button(tk, text="PATH_SEL", command=selPath)
    selectPath.pack()
    # def downSpigot():
    #    url = 'https://cdn.getbukkit.org/spigot/spigot-' + version.get() + '.jar'
    #    print(url)
    #    r = requests.get(url, allow_redirects=True)
    #    open(selPath() + '/spigot-' + version.get() + '.jar', 'wb').write(r.content)

    def downGit():
        url = 'https://github.com/sciencemj/autoDownload_test/archive/refs/heads/main.zip'
        print(url)
        r = requests.get(url, allow_redirects=True)
        path = version.get()
        file = path + '/main.zip'
        open(file, 'wb').write(r.content)
        zf = ZipFile(file, 'r')
        print(zf.namelist())
        rmlist = []
        for x in zf.namelist():
            if len(x.split('.')) > 1:
                pop = x
                print(pop)
                zf.extract(pop, path)
                src = path + '/' + pop
                dir = path + '/' + pop.split('/')[len(pop.split('/')) - 1]
                print('dir: ' + dir)
                shutil.move(src, dir)
            else:
                rmlist.append(path + '/' + x)
        for x in rmlist:
            os.rmdir(x)
        zf.close()
        os.remove(file)


    button = tkinter.Button(tk, text="DOWNLOAD", command=downGit)
    button.pack()





    def repeatDown():
        downGit()
        threading.Timer(5, repeatDown).start()


    t = turnOn()
    toggle = tkinter.Button(tk, text="TOGGLE AUTO_DOWNLOAD", command=t)
    toggle.pack()
    #start = tkinter.Button(tk, text="START", command=repeatDown)
    #start.pack()

    tk.mainloop()
