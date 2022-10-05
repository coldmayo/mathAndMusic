import matplotlib.pyplot as plt # For plotting
import numpy as np # Math
from pysine import sine # sine function plays sound at the given frequency
from random import randint # If you want to have a random number as the initial frequency

# Makes a Chromatic Scale using a given frequency as the lowest note
# Using the equation b = a*2^(n/1200) which is the equation to calculate the note (b) that is n cents apart from a (check README)

def makeScale(startFreq):
    notes = []
    cents = 100 # There are 100 cents between each note in the chromatic scale
    currFreq = startFreq
    for i in range(13): # There are 12 notes in the chromatic scale, the last note is the 1st note but an octave above
        b = currFreq*(2**(cents/1200))
        notes.append(b)
        currFreq = b
        b = 0
    return notes # Returns list of frequencies that correspond to notes in the scale

# Makes a major scale using any given frequency
# Major Scales follow the step pattern: whole, whole, half, whole, whole, whole, half
# A whole step is a full transition from one note to another. Example: A -> B, C -> D
# A half step is a half transition from one note to another. Example: A -> A#, C# -> D

def majorScale(startFreq):
    notes = []
    currFreq = startFreq
    for i in range(8): # 7 notes in a major scale, last note is the 1st note but an octave above
        if i == 2 or i == 6:
            cents = 100 # Half steps are 100 cents
        else:
            cents = 200 # Whole steps are 200 cents
        b = currFreq*(2**(cents/1200))
        notes.append(b)
        currFreq = b
        b = 0
    return notes
  
# Makes a minor scale using any given frequency
# Minor Scales follow the step pattern: whole, half, whole, whole, half, whole, whole

def minorScale(startFreq):
    notes = []
    currFreq = startFreq
    for i in range(8): # 7 notes in a minor scale, last note is the 1st note but an octave above
        if i == 1 or i == 4:
            cents = 100 # Half steps are 100 cents
        else:
            cents = 200 # Whole steps are 200 cents
        b = currFreq*(2**(cents/1200))
        notes.append(b)
        currFreq = b
        b = 0
    return notes

# Makes a scale of given length with each note being of equal temperment

def oddLenScale(leng,startFreq):
    notes = []
    currFreq = startFreq
    cents = 1200/leng # The lowest note of a scale and the highest should have 1200 cents bwteen them
    for i in range(leng+1):
        b = currFreq*(2**(cents/1200))
        notes.append(b)
        currFreq = b
        b = 0
    return notes

# Function for a sin wave using frequency

def makeSin(x,Freq):
    return np.sin(x*np.pi*Freq)

# Function that plays the scale selected uses (uses the minor/majorScale/oddLenScale/makeScale functions)

def playScale(startFreq,maOrMin,leng=0): # leng is for the oddLenScale function, will be zero if left alone
    bpm = 100 #bpm that the scale will be played at
    quart = 60/bpm # length at which a frequency will be played for a quarter note
    half = 60/bpm * 2 # length at which a frequency will be played for a half note (2 times the length of a quarter note)
    
    maOrMin = maOrMin.lower() # needed maOrMin to be case sensitive, this variable tells the function which scale to play
    
    if maOrMin == "major":
        notes = majorScale(startFreq)
    elif maOrMin == "chromatic":
        notes = makeScale(startFreq)
    elif maOrMin == "odd":
        notes = oddLenScale(leng,startFreq)
    elif maOrMin == "minor":
        notes = minorScale(startFreq)
    else:
        print("your chioces are 'major', 'chromatic', 'odd', or 'minor'")
        
    #  Plays up and down the scale in quarter notes. The highest note is a half note.
    for i in range(len(notes)):
        if i == len(notes)-1:
            sine(frequency=notes[i], duration=half)
        else:
            sine(frequency=notes[i], duration=quart)
    notes.reverse()
    for j in range(len(notes)):
        sine(frequency=notes[j], duration=quart)
