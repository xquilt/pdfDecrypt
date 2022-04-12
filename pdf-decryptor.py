from typing import ValuesView
import pikepdf

userPrompt = input('''
1-Try against a a file of words
2-Using brute Force
\t Which one do you wanna choose : 
''')


def pdfFileDecrypt(pdf_file_path, user_password):
    try :
        pdfObejct = pikepdf.Pdf.open(pdf_file_path , password=str(user_password))
        print(f"The password {user_password} worked !")
        return(True)
    except pikepdf._qpdf.PasswordError:
        print(f"The password {user_password} is wrong !")

if userPrompt == "1":
    wordListPath = input("Type the wordList absolute path : ")
    fileObject = open(wordListPath , "r")
    wordListWords = fileObject.readlines()
    fileObject.close()
    for word in wordListWords:
        word = word.replace("\n" , "")
        if pdfFileDecrypt(protectedFilePath , word) == True:
            break
        else :
            pdfFileDecrypt(protectedFilePath , word)
elif userPrompt == "2":
    print("\nAdd a range of numbers to search in !")
    startPoint = input("Starting from : ")
    endPoint = input("till : ")
    for passwordItem in range (int(startPoint) ,( int(endPoint)+1)):
        pdfFileDecrypt( protectedFilePath , passwordItem)
