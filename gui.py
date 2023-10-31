import tkinter as tk
from tkinter import filedialog
import search as sr
import threading

class gui():
    def __init__(self, root):
        self.root = root
        self.root.title("MyFileSearch")
        root.geometry('900x750')
        self.file_search = sr.search()
        self.var1 = tk.StringVar(value='contain')
        self.var2 = tk.StringVar(value='startwith')
        self.var3 = tk.StringVar(value='endwith')
        self.folder_path = tk.StringVar()
        
        #-------Widgets---------------------
        FrameS = tk.Frame(root)
        self.SearchBar = tk.Entry(FrameS)
        self.SearchButton = tk.Button(FrameS, text="search", command=self.search_directory)
        self.CancelButton = tk.Button(FrameS, text="cancel", command=self.stop_search)
        self.Output = tk.Text(root)
        FrameD = tk.Frame(root)
        self.LabelD = tk.Label(FrameD, text="Current Directory")
        self.Directory = tk.Entry(FrameD)
        self.Directory.insert(tk.END, '/mnt/c')
        self.selected_directory = '/mnt/c'
        self.BrowseButton = tk.Button(FrameD, text="browse", command=self.browse)
        FrameB = tk.Frame(FrameS)
        self.CBox = tk.Checkbutton(FrameB, text='Contains',onvalue='contain', variable=self.var1)
        self.SBox = tk.Checkbutton(FrameB, text='StartsWith',onvalue='startwith', variable=self.var2, offvalue='')
        self.EBox = tk.Checkbutton(FrameB, text='EndsWith',onvalue='endwith', variable=self.var3, offvalue='')

        #-------Grids------------------------
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        FrameS.columnconfigure(0, weight=10)
        FrameS.columnconfigure(1, weight=1)
        FrameS.rowconfigure(0, weight=1)
        FrameS.rowconfigure(1, weight=10)

        #-------Widgets-Placements---------------------
        FrameS.grid(row=0, column=1, sticky="we")
        self.SearchBar.grid(row=0, column=0, sticky='ew')
        self.SearchButton.grid(row=0, column=1, sticky= 'w', padx=10)
        self.CancelButton.grid(row=1, column=1, sticky='w', padx=10)
        FrameB.grid(row=1, column=0, sticky='w')
        self.CBox.grid(row=1, column=0, sticky='w')
        self.SBox.grid(row=1, column=1, sticky='w')
        self.EBox.grid(row=1, column=2, sticky='w')
        FrameD.grid(row=1, column=1, sticky="wen", columnspan=2) 
        self.LabelD.grid(row=0, column=1, sticky='nw')
        self.Directory.grid(row=1 , column=1)
        self.BrowseButton.grid(row=1, column=2, padx=10)
        self.Output.grid(row=2, column=1, columnspan=1 ,sticky='new')

    def start_search(self):
        pass
    
    def search_directory(self):
        user_directory = self.Directory.get()
        user_search = self.SearchBar.get()
        
        if self.var1.get() == 'contain':
            search_type = 'contain'
        elif self.var2.get() == 'startwith':
            search_type = 'startwith'
        elif self.var3.get() == 'endwith':
            search_type = 'endwith'
        else:
            search_type = 'contain'
        
        self.file_search.build_index(user_directory)
        self.file_search.search(user_search, search_type)
        results = "\n".join(self.file_search.result)
        message = f"{self.file_search.match} Matches out of {self.file_search.records} Records\n"
        self.Output.delete(1.0, tk.END)
        self.Output.insert(tk.END, message)
        results = "\n".join(self.file_search.result)
        self.Output.insert(tk.END, results)
    
    def browse(self):
        filedirectory = filedialog.askdirectory(initialdir='/mnt/c')
        if filedirectory:
            self.selected_directory = filedirectory
            self.Directory.delete(0, tk.END)
            self.folder_path.set(filedirectory)
            self.Directory.insert(0, self.selected_directory)
            
    
    def stop_search(self):
        pass  
        
    
if __name__ == "__main__":
    root = tk.Tk()
    app = gui(root)
    root.mainloop()

    
    