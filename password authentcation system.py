# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:39:10 2021

@author: Shivam Dandavate
"""

import pyaudio
import wave
from tkinter import *
import speech_recognition as sr

import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np


    
    
def register_user():
    username_info = username.get()
    fp = open("username.txt",'r')
    p =fp.read()
    
    if(p == username_info):
        Label(screen1,text ="Username not available",fg = "red",font = ("calibri" ,11),command = login()).pack()
    else:  
        
        file=open("username.txt", "w") 
        file.write(username_info+"\n")
        file.close() 
        Label(screen1,text ="Registration success",fg = "green",font = ("calibri" ,11),command = login()).pack()
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x450")
    
    global username
    global password
    global username_entry
    global password_entry
    
    
    username = StringVar()
    password = StringVar()
    
    Label(screen1,text ="Please enter details below").pack()
    Label(screen1,text ="").pack()
    
    Label(screen1,text ="Username").pack()
    username_entry = Entry(screen1,text = username)
    username_entry.pack()
   
    Label(screen1,text ="Password").pack()
    Button( screen1,text = "Click to record",width = "10",height ="2",command = record_s).pack()
def record_s():    
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 3
    
    filename = "input.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio


    print('Recording')

    stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

    frames1 = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames1.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')


    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames1))
    wf.close()
    frequency_sampling , audio_signal = wavfile.read("input.wav")
    global ampsample2
    ampsample2 = abs(data[1])
    print(ampsample2)
    print("\n signal shape 1 : ",audio_signal.shape)
    print("\n Signal Datatype :",audio_signal.dtype)
    print("\n Signal Duration ",round(audio_signal.shape[0]/float(frequency_sampling),2),'seconds')
    Button( screen1,text = "Register",width = "10",height ="1",command = register_user).pack()
   
def login():
    print("login session")
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x450")
    
    global username
    global password
    global username_entry2
    
    
    
    username2 = StringVar()
    password = pyaudio.PyAudio()
    
    Label(screen2,text ="Please enter details below").pack()
    Label(screen2,text ="").pack()
    
    Label(screen2,text ="Username").pack()
    username_entry2 = Entry(screen2,text = username2)
    username_entry2.pack()
    Label(screen2,text ="Password").pack()
    Button(screen2,text = "record",width = "10",height ="2",command = record_o).pack()
    Button(screen2,text = "LOGIN",width = "10",height ="2",command = login_success).pack()   
def login_success():
   
    
    username_info = username_entry2.get()
    print(username_info)
    file=open("username2.txt", "w") 
    file.write(username_info+"\n")
    file.close() 
    
    
    
    fp=open("username.txt", "r")
    fp2=open("username2.txt", "r")
    dp = fp2.read()
    sp = fp.read()
    
    if( dp == sp ):
            
            print("LOGIN SUCCESSFULL..!")
            global screen3
            screen3 = Toplevel(screen)
            screen3.title("Login")
            screen3.geometry("500x450")
            Label(screen3,text ="LOGIN SUCCESSFULL..!").pack()
    else:
            print("LOGIN UNSUCCESSFULL..!")
        
def record_o():    
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 3
    
    filename = "output.wav"

    password = p = pyaudio.PyAudio()  # Create an interface to PortAudio


    print('Recording')

    stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

    frames2 = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames2.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf1 = wave.open(filename, 'wb')
    wf1.setnchannels(channels)
    wf1.setsampwidth(p.get_sample_size(sample_format))
    wf1.setframerate(fs)
    wf1.writeframes(b''.join(frames2))
    wf1.close()   
    frequency_sampling , audio_signal = wavfile.read("output.wav")
    global ampsample 
    ampsample = abs(data[1])
    print(ampsample)
    print("\n signal shape 2 : ",audio_signal.shape)
    print("\n Signal Datatype 2 :",audio_signal.dtype)
    print("\n Signal Duration 2 ",round(audio_signal.shape[0]/float(frequency_sampling),2),'seconds')
    
    
def main_screen(): 
    global screen
    screen = Tk()
    screen.geometry("500x450")
    screen.title("notes 1.0")
    Label(text ="Notes 1.0",bg ="grey",width = "300",height ="2", font = ("calibri",13)).pack()
    Label(text ="").pack()
    Button(text = "Login",width = "30",height ="2",command = login).pack()
    Label(text ="").pack()
    Button(text = "Register",width = "30",height ="2",command = register).pack()
    screen.mainloop()
    
main_screen()

