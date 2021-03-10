import sys
import security
s = security.Security()

def main():
    txtFile = input("Please input your FileName.txt to transfer securely: ")
    try:
        f = open(txtFile, "r")
        txt = f.read()
    except:
        print("File not found. Please try again")
        sys.exit()

    print("You can either encrypt ir Decrypt your file")
    encryptChoice = input('Please enter "E" for encryption or "D" for Decryption: ')

    if not encryptChoice == "E" and not encryptChoice == "D":
        print("Invalid option. Please try again")
        sys.exit()   

    print("There are two encryption/decryption methods avaliable")
    encryptType = input('Please enter "C" for Caesar Cipher or "P" for Polyalphabetic Substitution: ')

    if not encryptType == "C" and not encryptType == "P":
        print("Invalid option. Please try again")
        sys.exit() 

    if encryptChoice == "E" and encryptType == "C":
        print("\n")
        CaesarEncrypttxt = s.CaesarEncryptor(txt)
        CaesarEncryptFile = open("caesar_encrypted.txt", "w+")
        CaesarEncryptFile.write(CaesarEncrypttxt)
        CaesarEncryptFile.close()
        print("***Caesar Cipher Encryption Done")
        print("Please refer to caesar_encrypted.txt file as your output")

    elif encryptChoice == "D" and encryptType == "C":
        print("\n")
        CaesarDecrypttxt = s.CaesarDecryptor(txt)
        CaesarDecryptFile = open("caesar_decrypted.txt", "w+")
        CaesarDecryptFile.write(CaesarDecrypttxt)
        CaesarDecryptFile.close()
        print("***Caesar Cipher Decryption Done")
        print("Please refer to caesar_decrypted.txt file as your output")

    elif encryptChoice == "E" and encryptType == "P":
        print("\n")
        PolySubEncrypttxt = s.PolySubEncryptor(txt)
        PolySubEncryptFile = open("polysub_encrypted.txt", "w+")
        PolySubEncryptFile.write(PolySubEncrypttxt)
        PolySubEncryptFile.close()
        print("***Polyalphabetic Encryption Done")
        print("Please refer to polysub_encrypted.txt file as your output")

    elif encryptChoice == "D" and encryptType == "P":
        print("\n")
        PolySubDecrypttxt = s.PolySubDecryptor(txt)
        PolySubDecryptFile = open("polysub_decrypted.txt", "w+")
        PolySubDecryptFile.write(PolySubDecrypttxt)
        PolySubDecryptFile.close()
        print("***Polyalphabetic Decryption Done")
        print("Please refer to polysub_decrypted.txt file as your output")

    print("Thank you!***")

if __name__ == "__main__":
    main()
