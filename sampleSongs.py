from pysine import sine

# Plays Twinkle Twinkle Little star using the notes from the chromatic scale created in the makingScales.py file

def twinkleTwinkle(notes):
    bpm = 200 # bpm of the song (This song in particular can be played at 100 bpm as well)
    quart = 60/bpm # duration at which a quarter note is played depending on the bpm
    half = 60/bpm * 2 # duration at which a quarter note is played depending on the bpm
    
    # notes in the chromatic scale are indexed as such: C-0, C#-1, D-2, D#-3, ... , C-12 
    
    # First line
    sine(frequency=notes[2], duration=quart)
    sine(frequency=notes[2], duration=quart)
    sine(frequency=notes[9], duration=quart)
    sine(frequency=notes[9], duration=quart)
    sine(frequency=notes[11], duration=quart)
    sine(frequency=notes[11], duration=quart)
    sine(frequency=notes[9], duration=half)
    sine(frequency=notes[7], duration=quart)
    sine(frequency=notes[7], duration=quart)
    sine(frequency=notes[6], duration=quart)
    sine(frequency=notes[6], duration=quart)
    sine(frequency=notes[4], duration=quart)
    sine(frequency=notes[4], duration=quart)
    sine(frequency=notes[2], duration=half)
    
    # Second line
    sine(frequency=notes[9], duration=quart)
    sine(frequency=notes[9], duration=quart)
    sine(frequency=notes[7], duration=quart)
    sine(frequency=notes[7], duration=quart)
    sine(frequency=notes[6], duration=quart)
    sine(frequency=notes[6], duration=quart)
    sine(frequency=notes[4], duration=half)
    sine(frequency=notes[9], duration=quart)
    sine(frequency=notes[9], duration=quart)
    sine(frequency=notes[7], duration=quart)
    sine(frequency=notes[7], duration=quart)
    sine(frequency=notes[6], duration=quart)
    sine(frequency=notes[6], duration=quart)
    sine(frequency=notes[4], duration=half)
    
    # Third Line
    sine(frequency=notes[2], duration=quart)
    sine(frequency=notes[2], duration=quart)
    sine(frequency=notes[9], duration=quart)
    sine(frequency=notes[9], duration=quart)
    sine(frequency=notes[11], duration=quart)
    sine(frequency=notes[11], duration=quart)
    sine(frequency=notes[9], duration=half)
    sine(frequency=notes[7], duration=quart)
    sine(frequency=notes[7], duration=quart)
    sine(frequency=notes[6], duration=quart)
    sine(frequency=notes[6], duration=quart)
    sine(frequency=notes[4], duration=quart)
    sine(frequency=notes[4], duration=quart)
    sine(frequency=notes[2], duration=half)
    print('Fin')
    
# Plays the bassline of the song Peace Sells by Megadeth using the notes from the chromatic scale created in the makingScales.py file
# Tab can be found at: https://www.songsterr.com/a/wsa/megadeth-peace-sells-bass-tab-s12554 
# Conversions from bass tabs to notes is here: http://dennishavlena.com/tabmus.htm

def peaceSells(notes):
    bpm = 140 # bpm of the song
    quart = 60/bpm # duration at which a quarter note is played depending on the bpm
    half = quart * 2 # duration at which a half note is played (2 times the length of a quarter note)
    eith = quart * (1/2) # duration at which a eighth note is played (half the length of a quarter note)
    sixteen = eith * (1/2) # duration at which a eighth note is played (half the length of a eighth note)
    for i in range(4):
        sine(frequency=notes[4], duration=sixteen*3)
        sine(frequency=notes[2], duration=sixteen)
        sine(frequency=notes[4], duration=eith)
        sine(frequency=notes[7], duration=eith)
        sine(frequency=notes[4]/2, duration=eith)
        sine(frequency=notes[4], duration=eith)
        sine(frequency=notes[2], duration=eith)
        sine(frequency=notes[9], duration=sixteen)
        sine(frequency=notes[10], duration=sixteen)
    
        sine(frequency=notes[4], duration=sixteen*3)
        sine(frequency=notes[2], duration=sixteen)
        sine(frequency=notes[4], duration=eith)
        sine(frequency=notes[7], duration=eith)
        sine(frequency=notes[4]/2, duration=eith)
        sine(frequency=notes[4], duration=eith)
        sine(frequency=notes[9]/2, duration=eith)
        sine(frequency=notes[10]/2, duration=eith)
    print('Fin')
