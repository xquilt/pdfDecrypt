#from pyparsing import one_of
import sys
from colorama import Fore, init
import pikepdf

# To avoid typing reset ANSI sequences repeatedly
init(autoreset=True)

def prompt_user():
    userPrompt = input('''
    1-Try against a a file of words
    2-Using brute Force
    \t Which one do you wanna choose :
''')

# A set of global variables (A temporary subtitute to command line argument/flags)
some_number_one = 1
some_number_one_hundred = 100
verbosity_option = True
locked_pdf_file = 'locked-file.pdf'
some_password = 99

'''
This very function is just for test purposes.
    - I was testing the difference between the 'with' statement in contrasts to typical
    open function.
'''
def pdf_file_decrypt(file_path,user_password):
    try:
        pdf_object = pikepdf.Pdf.open(file_path , password=str(user_password))
        print(f"The password {user_password} worked !")
        return True
    except pikepdf.qpdf.PasswordError:
        print(Fore.RED + f'The password {user_password} is wrong!')
        return False

def check_password(file_path, user_password):
    '''
    Test if the passed pdf file & password work together
    :param Pdf file path:
    :param Specific pdf file's password:
    :return Boolean value:
    '''
    try:
        with pikepdf.open(file_path, password=(str(user_password))):
            return True
    except pikepdf.PasswordError:
        return False
#print(check_password(locked_pdf_file, some_password))
#print(check_password(locked_pdf_file, 20000))
def return_password(file_path, number, verbosity_option=True):
    '''
    A wrapper around the check_password() function.
    it supports the addition of an optional verbosity logging at the standard output.
    The logging is further enhanced with visual indicators.
    :param The path to the pdf file:
    :param number:
    :param verbosity_option:
    :return:
    '''
    # Wouldn't it be cool if you've made use of a another tui library to draw a new screen of trial attempts, if verbosity option is true
    if (verbosity_option):
        if (check_password(file_path, number)):
            print(Fore.GREEN + f"The Pdf's password is {number}")
        else:
            print(Fore.RED + f'The Password {number} is wrong')
    else:
        if (check_password(file_path, number)):
            print(f"The pdf's password is {number}")

# We have two functions { brute_crack_password, dict_crack_password}
#     -They both used to either crack the pdf's password using sheer brute force or a predefine dictionary lines

# Password cracking functions
def brute_crack_password(first_number, end_number, file_path):
    '''
    Cracking the password using sheer brute force.
        -it should support
            -numeric
            -alphanumeric
            -symbolic
    :param The initial number in the ragne:
    :param The second number in the range:
    :param The path of the pdf file:
    :return:
    '''
    for current_number in range(first_number, end_number):
        return_password(file_path, current_number)
def dict_crack_password(dictionary, file_path):
    '''
    Reading the dictionary's content line by line
        - First check that the file is textual one.
        - Read the file content line by line.
    :param dictionary:
    :param file_path:
    :return:
    '''
    pass
brute_crack_password(1,100,locked_pdf_file)

def check_value():
    if userPrompt == "1":
        wordListPath = input("Type the wordList absolute path : ")
        fileObject = open(wordListPath , "r")
        wordListWords = fileObject.readlines()
        fileObject.close()
        for word in wordListWords:
            word = word.replace("\n" , "")
            if (pdf_file_decrypt(protectedFilePath , word) == True):
                break
            else:
                pdf_file-decrypt(protectedFilePath , word)
    elif userPrompt == "2":
        print("\nAdd a range of numbers to search in !")
        startPoint = input("Starting from : ")
        endPoint = input("till : ")
        for passwordItem in range (int(startPoint) ,( int(endPoint)+1)):
            pdf_file_decrypt( protectedFilePath , passwordItem)


'''
-Todos
    -The ability to view the file metadata
    -The ability to check the file protection scheme
    -the ability to crack the pdf password using either 
        -sheer bruteforce.
        -Dictionary based.
            -This approach is file based
                -Therefore should be a function that checks & read a dictionary file
'''

# - Handling linux signals
#     -Dedicate a separate module to exit the bruteforcing looping
#
# Won't it be cool to encapsulate crack{brute_force, dictionary} under one class nmaed 'pdf_crack' or something similar to that  


'''
This function should 
    -have multiple variables entailing data about the pdf file
        -data
            -name
            -pages count
            -encryption state (encrypted or not)
            -encryption type
            -encryption password (if found)
    -The printing should be directed at either 
        -the standard output
        -a file-like object (named after the original pdf file
'''
def print_data():
    file_name = 'name'
    file_count = 'file_count'
    encrypted_status = True
    encryption_type = 'somfe_type'
    info_list = [file_name, file_count, encrypted_status, encryption_type]
    with open(file_name, 'a+') as pdf_file:
        for property_item in info_list:
            print(property_item, file=file_name)
    pass