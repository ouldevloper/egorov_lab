#!/usr/bin/env python3

import sys,os,requests,time
import subprocess,socket
class Fuzzer:
    def __init__(self):
        self.pad = ''
        self.host = '127.0.0.1'
        self.port = 80
    def print(self,msg):
        sys.stdout.flush()
        sys.stdout.write(f'\r\r{msg}')
        sys.stdout.flush()
        time.sleep(0.1)
    def send(self,msg:str):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect((self.host,self.port))
                    sock.sendall(msg.encode())
            return True;
        except:
            return False
    def run(self):
        for padCounter in range(1000,10000):
            pattern = "\x41"*padCounter
            payload = f'GET {pattern}\n'
            res = self.send(payload)
            self.print(f"\r\rTrying [{padCounter}] | {pattern[:10]}")
            if not res:
                self.print(f'\n\nOffset Found {padCounter-1}')
                exit(0)
Fuzzer().run()
