#Python Script to encode a string to be compatible in a URL
#Github: https://github.com/mbrenton/URL-Encoder

#import pyperclip

def main():
    str = input("String: ")

    #Replacing " " to "%20"
    encoded_str = str.replace(" ", "%20")

    #This is for curl command, does not replace first space in command, if wanna paste in full command.
    if encoded_str.startswith("curl"):
        encoded_str = encoded_str.replace("%20", " ", 1)

    print("Encoded String:", encoded_str)

    #Copy to clipboard

    #pyperclip.copy(encoded_str)
    #print("URL Encoded String has been copied to clipboard...")
    #spam = pyperclip.paste()

if __name__ == "__main__":
    main()