#!/usr/bin/python3
badchars = ''
for char in range(0x01,0xff+1):
	if(char <= 0x0f):
		badchars += "\\x0%s"%hex(char)[2:]
	else:
		badchars += "\\x%s"%hex(char)[2:]
print(badchars)
