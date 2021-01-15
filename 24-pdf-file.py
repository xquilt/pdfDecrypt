import pikepdf

userPrompt = input('''
1-Try against a a file of words
2-Using brute Force
\t Which one do you wanna choose : ''')


def pdfFileDecrypt(pdfFilePath,userPassword):
    try :
        pdfObejct = pikepdf.Pdf.open(pdfFilePath , password=str(userPassword))
        print(f"The password {userPassword} worked !")
        return(True)
    except pikepdf._qpdf.PasswordError:
        print(f"The password {userPassword} is wrong !")

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
