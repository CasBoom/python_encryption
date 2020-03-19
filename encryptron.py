class Encryptron:
    def __init__(self):
        self.file=""

    def open_file(self, file):
        self.file = file
        new_file = open(self.file, encoding='utf-8')
        self.data = new_file.read()
        new_file.close()

    def encrypt(self, password):
        new_file = ""
        for n in range(0, len(self.data)):
            new_file += chr(ord(self.data[n])+ord(password[n%len(password)])+n%100)
        self.__save_file(new_file)

    def decrypt(self, password, view_only=True):
        new_file = ""
        for n in range(0, len(self.data)):
            new_file += chr(ord(self.data[n])-ord(password[n%len(password)])-n%100)
        
        if(view_only):
            print(new_file)
        else:
            self.__save_file(new_file)
    
    def __save_file(self, new_data):
        file_w = open(self.file, "w", encoding='utf-8')
        file_w.write(new_data)
        file_w.close()