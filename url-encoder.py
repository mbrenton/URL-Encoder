#!/usr/bin/env python3
# Python Script to encode a string to be compatible in a URL
# Github: https://github.com/mbrenton/URL-Encoder

# Imports
import urllib.parse
import sys

def main():

    # If argument is specified, use it, otherwise ask for input
    if len(sys.argv) > 1:
        str = sys.argv[1]
    else:
        str = input("Enter Command/Shell/URL: ")

    #This is for curl command, does not replace first space in command, if wanna paste in full command.
    if str.startswith("curl") or str.startswith("http"):
        code, command = str.split('=', 1)
        print("URL/curl: " + code + '=')
        print("Command:", command)
        str = urllib.parse.quote(command, safe='.')
        new_str = f"{code}={str}"
        print("Encoded Command/URL:", new_str)

    #Just Command
    else:
        new_str = urllib.parse.quote(str, safe='.')
        print("Encoded Command:", str)

if __name__ == "__main__":
    main()