def main():
    def encrypt(plaintext, shift):
        ciphertext = ""
        # using for loop to seperate all characters (slicing the string)
        for char in plaintext:
            if char.isalpha():
                '''Prints in respective format. If the user input Capital letter it encrypts and prints the capital letter
                if the user input small letter it encrypts small letter. The Input provided by the user is converted into
                ASCII Value and Adds with the shift value and prints the final value'''
                if char.isupper():
                    ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                ciphertext += char
        return ciphertext


    # Defining Function for Decrypting
    def decrypt(ciphertext, shift):
        plaintext = ""
        # using for loop to seperate all characters (slicing the string)
        for char in ciphertext:
            if char.isalpha():
                '''Prints in respective format. If the user input Capital letter it decrypts and prints the capital letter
                if the user input small letter it decrypts small letter. The Input provided by the user is converted into
                ASCII Value and Adds with the shift value and prints the final value'''
                if char.isupper():
                    plaintext += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    plaintext += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                plaintext += char
        return plaintext

    #this function will be called to welcome the new user
    def welcome():
        print("Welcome to Caesar Cipher")
        print("This Program can encrypt and decrypt the words and files you provide")

    #this function prompts the user to enter between 3 choices and returns the choice.
    def enter_message():
        # prompt user for input and use if else to encrypt , decrypt or quit the program.
        msg = input("Write 1 to encrypt, 2 to decrypt and 3 to quit the program: ")
        return msg

    #this function reads the input file and returns the content
    def read_file(filename):
        with open(filename, "r") as file:
            content = file.read()
        return content

    # The code for Running the program starts here.
    # 'valid' is given True boolen type soo the while loop executes
    valid = True
    # 'Run' is given True boolen Value soo the nested while loop(to rerun the program) executes
    run = True
    # the while loop executes when the value is true.
    welcome()

    while valid:
        u = int(input("Enter 1 to Encrypt/Decrypt a word or 2 to Encrypt/Decrypt a file and 3 to Quit the program: "))
        if u == 1:
            n = enter_message()
            if n == "1":
                # ask for input and shift value and call the Function 'Encrypt'
                plaintext = input("Enter a String: ")
                shift = int(input("Enter how much you want to shift your Word: "))
                ciphertext = encrypt(plaintext, shift)
                print(ciphertext)
                # Prompts the user to input a value and check if they want to rerun the program.
                while run:
                    j = input("Do you want to rerun the program? y/n: ")
                    # using if else and changing the boolean value of 'Value' and 'run'
                    if j == "y":
                        valid = True
                        run = False
                    elif j == "n":
                        valid = False
                        run = False
                    else:
                        valid = True
                        print("Not sure what you meant by", j, "Please enter either y or n")
                        run = True
            elif n == "2":
                # ask for input and shift value and call the Function 'Decrypt'
                ciphertext = input("Enter a String: ")
                shift = int(input("Enter how much you want to shift your Word: "))
                decrypted_plaintext = decrypt(ciphertext, shift)
                print(decrypted_plaintext)
                # Prompts the user to input a value and check if they want to rerun the program.
                while run:
                    k = input("Do you want to rerun the program? y/n: ")
                    # using if else and changing the boolean value of 'Value' and 'run'
                    if k == "y":
                        valid = True
                        run = False
                        k = " "
                    # if the user inputs n the valid and run are changed into false hence we escape both the loops
                    elif k == "n":
                        valid = False
                        run = False
                        k = " "
                    # if the user inputs something else than y and n then the code reruns the nested loop(from line 70)
                    else:
                        valid = True
                        print("Not sure what you meant by", k, "Please enter either y or n")
                        run = True

            elif n == "3":
                print("Quitting the program")
                valid = False
        elif u == 2:
            n = enter_message()
            if n == "1":
                # ask for file input and shift value and call the Function 'Encrypt'
                '''Here user will have to input the full location of the txt file they want to read along with the extension
                .txt. For example i have a txt file named "hck.txt" in desktop. if i want to encrypt or decrypt the file
                then ill have to enter the full path in following manner. c:/Users/suyog/OneDrive/Desktop/hck.txt and it 
                will run the entire document in the contained file.'''
                p = input("Enter filename with extension and location following with a / : ")
                plaintext =  read_file(filename = p)
                shift = int(input("Enter how much you want to shift your file: "))
                ciphertext = encrypt(plaintext, shift)
                print(ciphertext)
                # Prompts the user to input a value and check if they want to rerun the program.
                while run:
                    j = input("Do you want to rerun the program? y/n: ")
                    # using if else and changing the boolean value of 'Value' and 'run'
                    if j == "y":
                        valid = True
                        run = False
                    elif j == "n":
                        valid = False
                        run = False
                    else:
                        valid = True
                        print("Not sure what you meant by", j, "Please enter either y or n")
                        run = True
            elif n == "2":
                '''Here user will have to input the full location of the txt file they want to read along with the extension
                .txt. For example i have a txt file named "hck.txt" in desktop. if i want to encrypt or decrypt the file
                then ill have to enter the full path in following manner. c:/Users/suyog/OneDrive/Desktop/hck.txt and it 
                will run the entire document in the contained file.'''
                # ask for input and shift value and call the Function 'Decrypt'
                p = input("Enter filename with extension: ")
                ciphertext = read_file(filename = p)
                shift = int(input("Enter how much you want to shift your file: "))
                decrypted_plaintext = decrypt(ciphertext, shift)
                print(decrypted_plaintext)
                # Prompts the user to input a value and check if they want to rerun the program.
                while run:
                    k = input("Do you want to rerun the program? y/n: ")
                    # using if else and changing the boolean value of 'Value' and 'run'
                    if k == "y":
                        valid = True
                        run = False
                    # if the user inputs n the valid and run are changed into false hence we escape both the loops
                    elif k == "n":
                        valid = False
                        run = False
                    # if the user inputs something else than y and n then the code reruns the nested loop(from line 70)
                    else:
                        valid = True
                        print("Not sure what you meant by", k, "Please enter either y or n")
                        run = True
        elif u == 3:
            valid = False
            print("Quitting the program")
        else:
            print("Not sure what you meant by",u,"please enter either 1 or 2")
            valid = True


    print("Thank you for using the program")
main()
