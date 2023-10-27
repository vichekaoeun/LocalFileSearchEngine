import os

class search:
    def __init__(self):
        self.file_index = {} #store our file indexes
        self.result = [] #store our list of results
        self.match = 0 #counter for the number of matches
        self.records = 0 #counter for record search
    
    def build_index(self, directory): #Building our file indexes
        for roots, dirs, files in os.walk(directory): #this loops tranverses through 'directory' as provided by os.walk
            for file in files: #loops through list of file names in current directory
                file_path = os.path.join(roots, file) #combine file path with root path
                self.file_index[file] = file_path #append this path to 'file_index'
    
    def search(self, query, type='contain'): #Performs the actual search, Query is user-input
        self.result = [] #clear previous result
        self.match = 0 #resets match
        self.records = 0 #resets records
        
        for files, path in self.file_index.items():
            self.records += 1
            if (type == 'contain' and query.lower() in files.lower() or
                type == 'startwith' and files.lower().startswith(query.lower()) or
                type == 'endwith' and files.lower().endswith(query.lower())):
                    result = path.replace('\\', '/') + '/' + files
                    self.result.append(result)
                    self.match += 1 #increment match for every match found

