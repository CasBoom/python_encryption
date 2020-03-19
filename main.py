import sys
import encryptron as cr
encryptron = cr.Encryptron()
intention = ""
running = True

#main loop
while(running):
    #check user intention
    if(intention == ""):
        print("_____Encryptron___")
        print("Enter 'c' to close")
        intention = input("Would you like to encrypt or decrypt a file? (e/d): ").lower()

    #encrpyting options
    if(intention == "e"):
        file_to_encrypt = input("Which file would you like to encrypt? ('C' to cancel): ").lower()
        if(file_to_encrypt=='c'):
            print("Canceling...")
            intention = ""
        else:
            #if file exists
            try:
                encryptron.open_file(file_to_encrypt)
                file_exists = True
            except:
                file_exists = False
                print("Theres no file named: " + file_to_encrypt + " in this directory.")
            if(file_exists):
                auth = input("Are you sure you want to encrypt: " + file_to_encrypt + "? (y/n) ").lower()
                if(auth=='y'):
                    password=input("Choose a password to lock your files with: ")
                    print("encrypting...")
                    encryptron.encrypt(password)
                    print("Your file has been encrypted")
            
    #decrypting options
    elif(intention=="d"):
        file_to_decrypt = input("Which file would you like to decrypt ('C' to cancel): ").lower()
        if(file_to_decrypt == 'c'):
            print("Canceling...")
            intention = ""
        else:
            #if file exists
            try:
                encryptron.open_file(file_to_decrypt)
                file_exists=True

            except:
                file_exists=False
                print("Theres no file named: " + file_to_decrypt + " in this directory.")

            if(file_exists):
                auth = input("Are you sure you want to decrypt: " + file_to_decrypt + "? (y/n) ").lower()
                if(auth=='y'):
                    action = input("Would you like to permanently undo the encryption (y/n/help) ").lower()
                    password=input("Password: ")
                    if(auth != ""):
                        if(action == 'y'):                   
                            print("decrypting...")
                            encryptron.decrypt(password, False)
                            print("Your file has been decrypted")
                        elif(action == 'n'):
                            print("decrypting...")
                            encryptron.decrypt(password)
                            print("Your file has been decrypted")
                        elif(action == "help"):
                            print("""If you permanently decrypt a file, it will be saved in a text file.
                                Trying to decrypt a file with a wrong password may make the file irrecoverable.
                                
                                Simply reading the file will print the file out into the terminal with no risk of damaging the file""")
                        elif(action == "c"):
                            print("Canceling...")
                            intention = ""
                        else:
                            print("Invalid command")
                            auth = ""
                elif(auth=='n'):
                    print("Canceling...")
                    intention = ""

    #closing
    elif(intention == "c"):
        print("Closing...")
        running = False

    else:
        print("unknown command")
