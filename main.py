import pikepdf
from pyparsing import one_of

def prompt_user():
    userPrompt = input('''
    1-Try against a a file of words
    2-Using brute Force
    \t Which one do you wanna choose :
''')

some_number_one = 1
some_number_one_hundred = 100
verbosity_flag = True
locked_pdf_file = 'locked-file.pdf'
some_password = 99

def check_password(file_path, user_password):
    try:
        with pikepdf.open(file_path, password=(str(user_password))):
            return(True)
    except pikepdf.PasswordError:
        return(False)

#print(check_password(locked_pdf_file, some_password))
#print(check_password(locked_pdf_file, 20000))

# We have two functions { brute_crack_password, dict_crack_password}
#     -They both used to either crack the pdf's passwrd using sheer brute force or a a predefine dictionary lines

def return_password(file_path, number, verbosity_option):
    if (check_password(file_path, number)):
        print(f"The Pdf's password is {number}")
    else:
        print(f'Password {number} is wrong')

def brute_crack_password(first_number, end_number, file_path):
    for number in range(first_number, end_number):
        pass

# brute_crack_password(some_number_one, some_number_one_hundred, locked_pdf_file)

def dict_crack_password(dictionary, file_path):
    pass
#Reading the dictionary's content line by line
#    - First check that the file is textual one.
#    - Read the file content line by line.

def pdfFileDecrypt(file_path,user_password):
    try :
        pdfObejct = pikepdf.Pdf.open(file_path , password=str(user_password))
        print(f"The password {user_password} worked !")
        return(True)
    except pikepdf._qpdf.PasswordError:
        print(f"The password {user_password} is wrong !")

def check_value():
    if userPrompt == "1":
        wordListPath = input("Type the wordList absolute path : ")
        fileObject = open(wordListPath , "r")
        wordListWords = fileObject.readlines()
        fileObject.close()
        for word in wordListWords:
            word = word.replace("\n" , "")
            if pdfFileDecrypt(protectedFilePath , word) == True:
                break
            else:
                pdfFileDecrypt(protectedFilePath , word)
    elif userPrompt == "2":
        print("\nAdd a range of numbers to search in !")
        startPoint = input("Starting from : ")
        endPoint = input("till : ")
        for passwordItem in range (int(startPoint) ,( int(endPoint)+1)):
            pdfFileDecrypt( protectedFilePath , passwordItem)


# Todos
#     -The ability to view the file metadata
#     -The ability to check the file protection scheme
#     -the ability to crack the pdf password using either 
#         -sheer bruteforce.
#         -Dictionary based.

# - Handling linux signals
#     -Dedicate a separate module to exit the bruteforcing looping


shopping_list = {
    'bread': 1,
    'Milk': 2,
    'Butter': 3,
    'Coffee': 4
}

print(shopping_list.items())
print(type(shopping_list.items()))

def show_list():
    for item, quantity in shopping_list.items():
        print(f'The required item is {quantity}x and its name is {item}')

show_list()