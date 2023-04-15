import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Menu, Menubutton, messagebox
from c1pher import Param
import threading
import time

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)

    def enter(self, event):
        self.widget.config(cursor="arrow")
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+{}+{}".format(event.x_root+10, event.y_root+10))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffff", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def leave(self, event):
        self.widget.config(cursor="")
        if self.tipwindow:
            self.tipwindow.destroy()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.file_path = ""
        self.create_widgets()

    def create_widgets(self):
        # Create the Sign button
        # self.cp_button = tk.Button(self.master, text="Create Parameters", command=self.cp)
        # self.cp_button.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)
        self.menuBar = Menu(self.master)
        self.master.config(menu=self.menuBar)
        self.menuMisc = Menu(self.menuBar, tearoff=0)
        self.menuMisc.add_command(label="Parameters", command="#")
        self.menuMisc.add_command(label="in4", command="#")
        self.menuMisc.add_command(label="Help!", command="#")
        self.menuBar.add_cascade(label="Misc", menu=self.menuMisc)
        # self.menuMisc.add_separator()
        
        

        # Create the Unsign button
        self.sign_button = tk.Button(self.master, text="Sign", command=self.sign)
        self.sign_button.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)

        # Create the Unsign file path input and file chooser button
        self.sign_entry = tk.Entry(self.master, width=50)
        self.sign_entry.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)
        self.sign_file_button = tk.Button(self.master, text="...", command=self.open_sign_file)
        self.sign_file_button.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)

        # Create the Create Param button
        self.unsign_button = tk.Button(self.master, text="unSign", command=self.unsign)
        self.unsign_button.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)

        # Create the progress bar
        self.progress_bar = tk.ttk.Progressbar(self.master, orient="horizontal", length=100, mode="indeterminate")
        self.progress_bar.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)
        
        ToolTip(self.sign_button, "Start Signcryption!")
        ToolTip(self.unsign_button, "Start unSigncryption!")

        # Create the status bar
        self.status_bar = tk.Label(self.master, text="Ready")
        self.status_bar.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)
        
        self.time_label = tk.Label(root, font=("Helvetica", 10))
        self.time_label.pack(padx=10, pady=10)
        
        

      

    def sign(self):
        self.master.after(0, self.time_label.config, {"text": ""})
        self.sign_button.config(state="disabled")
        self.progress_bar.start(50)
        t = threading.Thread(target=self.sign_long)
        t.start()
        
    def sign_long(self):
        p = Param.Sparam()
        if self.file_path:
            self.start_time = time.time()
            print("File for SignCryption is: ", self.file_path)
            p.run(self.file_path)
            self.master.after(0, self.status_bar.config, {"text": "Signed!"})
            self.master.after(0, self.time_label.config, {"text": f"{time.time() - self.start_time:.2f} seconds"})
        else:
            messagebox.showinfo("Error", "No file selected!")
            self.master.after(0, self.status_bar.config, {"text": "can't sign, No file selected!"})

        
        self.master.after(0, self.progress_bar.stop)
        self.master.after(0, self.sign_button.config, {"state": "normal"})
      


    def unsign(self):
        self.master.after(0, self.time_label.config, {"text": ""})
        self.unsign_button.config(state="disabled")
        self.progress_bar.start(50)
        t = threading.Thread(target=self.unsign_long)
        t.start()
    def unsign_long(self):
        p = Param.Uparam()
        self.start_time = time.time()
        p.run()
        self.master.after(0, self.unsign_button.config, {"state": "normal"})
        self.master.after(0, self.status_bar.config, {"text": "Un-Signed!"})    
        self.master.after(0, self.time_label.config, {"text": f"{time.time() - self.start_time:.2f} seconds"})
      

    def open_sign_file(self):
        filename = filedialog.askopenfilename(initialdir=".", title="Select file", filetypes=(("Text files", "*.txt"),))
        self.sign_entry.delete(0, tk.END)
        self.sign_entry.insert(0, filename)
        self.file_path = filename if filename else ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.pack(fill=tk.BOTH, expand=True)
    app.mainloop()
