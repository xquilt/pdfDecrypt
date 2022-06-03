#from pyparsing import one_of
from colorama import Fore, init
import pikepdf

# To avoid typing reset ANSI sequences repeatedly
init(autoreset=True)

def prompt_user():
    userPrompt = input('''
        1-Try against a a file of words
        2-Using brute Force
        Which one do you wanna choose :
    ''')

# A set of global variables (A temporary subtitute to command line argument/flags)
some_number_one = 1
some_number_one_hundred = 100
verbosity_option = True
locked_pdf_file = 'locked-file.pdf'
file_password = 99

'''
- Creating a function that returns data about the PDF file itself.
    - PDF file name
    - Other manageable pdf metadata that can be possible extracted using the library itself
'''

'''
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP toolkit 2.9.1-13, framework 1.6">
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:iX="http://ns.adobe.com/iX/1.0/">
<rdf:Description xmlns:pdf="http://ns.adobe.com/pdf/1.3/" />
<rdf:Description xmlns:xmp="http://ns.adobe.com/xap/1.0/" >
<xmp:CreatorTool>UnknownApplication</xmp:CreatorTool></rdf:Description>
<rdf:Description xmlns:xapMM="http://ns.adobe.com/xap/1.0/mm/" rdf:about="" 
<rdf:Description xmlns:dc="http://purl.org/dc/elements/1.1/" rdf:about="" 

dc:title><rdf:Alt><rdf:li xml:lang="x-default">Untitled</rdf:li></rdf:Alt></dc:title></rdf:Description>

="application/pdf"><
'''

def pdf_data_info():
    pdf_file_object = return_pdf_file_object(locked_pdf_file, file_password)
    file_properties_keys = ["pdf:Producer", "dc:format", "rdf:about", "xmp:ModifyDate", "xmp:CreateDate"]
    file_properties_list = []
    index = 0
    while index < len(file_properties_keys):
        try:
            file_property_value = pdf_file_object.open_metadata()[file_properties_keys[index]]
            file_properties_list.append(file_property_value)
        except:
            file_properties_list.append("Unknown")
        index += 1
    #document_id = pdf_file_object.open_metadata()["xapMM:DocumentID"]
    file_data = {
        "file_modification_data": file_properties_list[3],
        "file_creation_data": file_properties_list[4],
        "file_format": file_properties_list[1],
        "pdf_producer": file_properties_list[0],
        "file_about": file_properties_list[2]
    }
    print(file_data)
    return file_data

'''
This very function is just for test purposes.
    - I was testing the difference between the 'with' statement in contrasts to typical open function.
'''

def return_pdf_file_object(filepath, file_password):
    try:
        pdf_file_object = pikepdf.Pdf.open(filepath, password=str(file_password))
        return pdf_file_object
    except:
        print("The file couldn't be opened")
        return false

def pdf_file_decrypt(file_path,user_password):
    try:
        pdf_object = pikepdf.Pdf.open(file_path , password=str(user_password))
        print(f"The password {user_password} worked !")
        return True
    except pikepdf.qpdf.PasswordError:
        print(Fore.RED + f'Password {user_password} is wrong!')
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

#print(check_password(locked_pdf_file, file_password))
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
            print(Fore.RED + f'Password {number} is wrong')
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

    # A hypothetical string (this string should be the returned value of the included dictionary )
    just_multiline = '''
    pass_one
    pass_two
    pass_three
    pass_four
    pass_five
    password six
    '''
    print(just_multiline)
    passwords_list = just_multiline.splitlines()
    # I guess this returned list of hypothetical passwords should be further refined to exclude redundancy (this would cut down possible computational overload, as opening, testing password and print trial error is too much)

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

pdf_data_info()
#brute_crack_password(1,100,locked_pdf_file)
