class Security:
    def __init__(self):
        #Lists for letters, numbers, special characters and a list containing all characters
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.specialchar = ["\n", " ", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "<", ">", ",", ".", "?", "/", "\"", "|", "[", "]", "{", "}", ";", ":"]
        self.fullList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] + self.letters + self.numbers + self.specialchar

    def CaesarEncryptor(self, text):
        #Variables used in program
        txtList = []

        #Welcomes user to Caesar Encryption and asks for an encryption key
        print("***Welcome to Caesar Cipher Encryption Function***")
        keyshift = int(input("Please enter an integer number as an encryption key: "))

        #Runs the loop for each character in the text
        for i in range(len(text)):
            #Variables used in program
            char = text[i]
            uppercaseChar = char.upper()

            #Checks to see if the character is uppercase
            if char in self.letters:
                #Checks to see what index it is in letter list
                for j in range(len(self.letters)):
                    if self.letters[j] == char:
                        #Shifts the index of the number list by key index then appends the new letter
                        txtList.append(self.letters[j - keyshift])

            #Check to see if the character is a number
            elif char in self.numbers:
                #Checks to see what index it is in number list
                for k in range(len(self.numbers)):
                    if self.numbers[k] == char:
                        #Shifts the index of the number list by key index then appends the new number
                        txtList.append(self.numbers[k - keyshift])

            #Checks to see if the character is a special character
            elif char in self.specialchar:
                #Checks to see what index it is in special character list
                for l in range(len(self.specialchar)):
                    if self.specialchar[l] == char:
                        #Shifts the index of the special char list by key index then appends the new special character
                        txtList.append(self.specialchar[l - keyshift])

            #Converts lowercase letters to uppercase then checks to see if they appear in letter list
            elif uppercaseChar in self.letters:
                #Checks to see what index it is in letter list
                for m in range(len(self.letters)):
                    if self.letters[m] == uppercaseChar:
                        #Shifts the index of the letter list by key index then appends the new letter as lowercase
                        lowercase = self.letters[m  - keyshift]
                        txtList.append(lowercase.lower())
           
        #Joins the shifted list into a string then returns it to the main program
        txtString = ''.join(txtList)
        return txtString


    def CaesarDecryptor(self, text):
        #Variables used in program
        txtList = []
        reversedLetterList = []
        reversedNumberList = []
        reversedSpecialCharList = []

        #Welcomes user to Caesar Decryption and asks for an encryption key
        print("***Welcome to Caesar Cipher Decryption Function***")
        keyshift = int(input("Please enter an integer number as an encryption key: "))

        #ReversingLists
        for i in reversed(self.letters):
            reversedLetterList.append(i)
        for i in reversed(self.numbers):
            reversedNumberList.append(i)
        for i in reversed(self.specialchar):
            reversedSpecialCharList.append(i)

        #Runs loop for each character in the text
        for i in range(len(text)):
            #Variables used in program
            char = text[i]
            uppercaseChar = char.upper()

            #Check Uppercase Letters
            if char in self.letters:
                for j in range(len(reversedLetterList)):
                    if reversedLetterList[j] == char:
                        txtList.append(reversedLetterList[j - keyshift])

            #Checks Numbers
            elif char in reversedNumberList:
                for k in range(len(reversedNumberList)):
                    if reversedNumberList[k] == char:
                        txtList.append(reversedNumberList[k - keyshift])

            #Checks Special Characters
            elif char in reversedSpecialCharList:
                for l in range(len(reversedSpecialCharList)):
                    if reversedSpecialCharList[l] == char:
                        txtList.append(reversedSpecialCharList[l - keyshift])

            #Converts Lowercase to Uppercase then checks 
            elif uppercaseChar in reversedLetterList:
                for m in range(len(reversedLetterList)):
                    if reversedLetterList[m] == uppercaseChar:
                        lowercase = reversedLetterList[m  - keyshift]
                        txtList.append(lowercase.lower())
           
        #Joins the shifted list into a string then returns it to the main program
        txtString = ''.join(txtList)
        return txtString

        
    def PolySubEncryptor(self, text):
        #Variables used in program
        nonDuplicateKey = []
        repeatedKey = []
        indexKeyList = []
        polyList = []
        keycount = 0 
        indexCount = 0 

        #Welcomes user to PolySub Encryption and asks for an encryption keyword
        print("***Welcome to Polyalphabetic Substitution Encryption Function***")
        key = str(input("Please enter a string as an encryption keyword: "))

        #Removes duplicate characters from encryption key 
        keyList = list(key)
        for i in range (len(keyList)):
            if keyList[i] not in nonDuplicateKey:
                nonDuplicateKey.append(key[i])

        #Creates a list of the keyword repeated until it reaches the same length as the text
        while len(repeatedKey) < len(text):
           repeatedKey.append(nonDuplicateKey[keycount])
           keycount += 1
           if keycount == len(nonDuplicateKey):
                keycount = 0

        #Runs through the repeated list and collects the index 
        for i in range(len(repeatedKey)):
            subkey = repeatedKey[i]
            if subkey in self.fullList:
                for j in range(len(self.fullList)):
                    if self.fullList[j] == subkey:
                        indexKeyList.append(j)

        #Runs the loop for each character in the text
        for i in range(len(text)):
            char = text[i]

            #Checks for Letters Numbers and Special Characters then appends them to list
            if char in self.fullList:
                for j in range(len(self.fullList)):
                    if self.fullList[j] == char:
                        polyKey = j + indexKeyList[indexCount]
                        if polyKey > 93:
                            polyKey = polyKey - 94
                        polyList.append(self.fullList[polyKey])
                        indexCount += 1

        #Joins the shifted list into a string then returns it to the main program
        txtString = ''.join(polyList)
        return txtString


    def PolySubDecryptor(self, text):
        #Variables used in program
        nonDuplicateKey = []
        repeatedKey = []
        indexKeyList = []
        polyList = []
        keycount = 0 
        indexCount = 0 

        #Welcomes user to PolySub Decryption and asks for an encryption keyword
        print("***Welcome to Polyalphabetic Substitution Decryption Function***")
        key = str(input("Please enter a string as an encryption keyword: "))

        #Removes duplicate characters from encryption key 
        keyList = list(key)
        for i in range (len(keyList)):
            if keyList[i] not in nonDuplicateKey:
                nonDuplicateKey.append(key[i])

        #Creates a list of the keyword repeated until it reaches the same length as the text
        while len(repeatedKey) < len(text):
           repeatedKey.append(nonDuplicateKey[keycount])
           keycount += 1
           if keycount == len(nonDuplicateKey):
                keycount = 0

        #Runs through the repeated list and adds the index 
        for i in range(len(repeatedKey)):
            subkey = repeatedKey[i] 
            if subkey in self.fullList:
                for j in range(len(self.fullList)):
                    if self.fullList[j] == subkey:
                        indexKeyList.append(j)

        #Runs the loop for each character in the text
        for i in range(len(text)):
            char = text[i]

            #Uppercase Letters, Numbers
            if char in self.fullList:
                for j in range(len(self.fullList)):
                    if self.fullList[j] == char:
                        polyKey = j - indexKeyList[indexCount]
                        polyList.append(self.fullList[polyKey])
                        indexCount += 1

        #Joins the shifted list into a string then returns it to the main program
        txtString = ''.join(polyList)
        return txtString