#In order ror this example-code to work, make sure you have a
#card with at least one folder, containing at least two mp3:s.
#The folders should be named 01, 02 etc and files should be named
#001.mp3, 002.mp3 etc.
from utime import sleep_ms, sleep
from picodfplayer import DFPlayer


#Constants. Change these if DFPlayer is connected to other pins.
UART_INSTANCE=1
TX_PIN = 4
RX_PIN = 5
BUSY_PIN = 18

#Create player instance
player=DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)
sleep(2)
player.setVolume(20)
#Check if player is busy.
print('Playing?', player.queryBusy())
#Play the first song (001.mp3) from the first folder (01)

print('Playing track 001.mp3 in folder 01')
if not player.queryBusy():
    player.playTrack(2, 2)
#Wait 5 seconds...
sleep(2)

#Pause
print('Pausing')
player.pause()

#Wait 2 seconds...
sleep(2)

#Resume
print('Resuming play')
player.resume()

#Wait 5 seconds
sleep(5)

#Pause by directly sending the pause  (0x0E) command to the command line and printing the output.
print('Pausing by sending the pause command manually, and printing the output')
print(str(player.sendcmd(0x0E, 0x00, 0x00)))

print('You can try me out by sending commands in the console, such as player.resume()')