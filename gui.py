import tkinter as tk
import search as sr

class gui():
    def __init__(self, root):
        self.root = root
        self.root.title("MyFileSearch")
        root.geometry('900x750')
        self.file_search = sr.search()
        
        #-------Widgets---------------------
        self.SearchBar = tk.Entry(root)
        self.SearchButton = tk.Button(root, text="search", command=self.search_directory)
        self.Output = tk.Text(root)
        FrameD = tk.Frame(root)
        self.LabelD = tk.Label(FrameD, text="Current Directory")
        self.Directory = tk.Entry(FrameD)

        #-------Grids------------------------
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)

        #-------Widgets-Placements---------------------
        self.SearchBar.grid(row=0, column=1, sticky='ew')
        self.SearchButton.grid(row=0, column=2, sticky= 'w', padx=10)
        FrameD.grid(row=1, column=1, sticky="wen", columnspan=2) 
        self.LabelD.grid(row=0, column=1, sticky='nw')
        self.Directory.grid(row=1 , column=1)
        self.Output.grid(row=2, column=1, columnspan=1 ,sticky='new')

    def search_directory(self):
        user_directory = self.Directory.get()
        user_search = self.SearchBar.get()
        self.file_search.build_index(user_directory)
        self.file_search.search(user_search)
        results = "\n".join(self.file_search.result)
        self.Output.delete(1.0, tk.END)
        self.Output.insert(tk.END, results)
    
        
        
    
if __name__ == "__main__":
    root = tk.Tk()
    app = gui(root)
    root.mainloop()

    
    