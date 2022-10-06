import matplotlib.pyplot as plt

notesChrome = makeScale(startFreq) # Gets frequencies of your chromatic scale (check the makingScales.py file)

t = np.linspace(0,1,200) # t is the time from 0-1 second with 200 points in between

fig, axs = plt.subplots(3, 4,sharex=True,sharey=True)

# Check out makingScales.py to see the makeSin function
axs[0][0].plot(t,makeSin(t,notesChrome[0])) # C (low)
axs[0][1].plot(t,makeSin(t,notesChrome[1])) # C#
axs[0][2].plot(t,makeSin(t,notesChrome[2])) # D
axs[0][3].plot(t,makeSin(t,notesChrome[3])) # D#
axs[1][0].plot(t,makeSin(t,notesChrome[4])) # E
axs[1][0].set_ylabel('$\sin(t\pi f)$')
axs[1][1].plot(t,makeSin(t,notesChrome[5])) # F
axs[1][2].plot(t,makeSin(t,notesChrome[6])) # F#
axs[1][3].plot(t,makeSin(t,notesChrome[7])) # G
axs[2][0].plot(t,makeSin(t,notesChrome[8])) # G#
axs[2][1].plot(t,makeSin(t,notesChrome[9])) # A
axs[2][1].set_xlabel('t')
axs[2][2].plot(t,makeSin(t,notesChrome[10])) # A#
axs[2][2].set_xlabel('t')
axs[2][3].plot(t,makeSin(t,notesChrome[11])) # B
fig.tight_layout()
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
