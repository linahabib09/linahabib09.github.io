from gpiozero import LED
from gpiozero import Button
import time
from threading import Thread, Event
import os

_led = LED(17)
_button = Button(2, bounce_time=0.05)


def dot():
    _led.on()
    time.sleep(0.2)
    _led.off()
    time.sleep(0.2)

def dash():
    _led.on()
    time.sleep(1)
    _led.off()
    time.sleep(0.2)

    
MORSE = {'A':'.- ' , 'B':'-... ' , 'C':'-.-. ' , 'D':'-.. ' , 'E':'. ' ,
         'F':'..-. ' , 'G':'--. ' , 'H':'.... ' , 'I':'.. ' , 'J':'.--- ' , 
         'K':'-.- ' , 'L':'.-.. ' , 'M':'-- ' , 'N':'-. ' , 'O':'--- ' , 'P':'.--. ' , 
         'Q':'--.- ' , 'R':'.-. ' , 'S':'... ' , 'T':'- ' , 'U':'..- ' , 'V':'...- ' , 
         'W':'.-- ' , 'X':'-..- ' , 'Y':'-.-- ' , 'Z':'--.. ' , '1':'.---- ' , 
         '2':'..--- ' , '3':'...-- ' , '4':'....- ' , '5': '..... ' , '6':'-.... ' , 
         '7':'--... ' , '8':'---.. ' , '9':'----. ' , '0':'----- ' , ' ':'  '}

REVERSE_MORSE = {v.strip(): k for k, v in MORSE.items() if k != ' '}

def letter_to_dots(letter):
    '''
    (str) --> str
    Converts alphabet or numerical value of any case to morse. Ignores
    invalid input and '  ' for space.
    '''
    new = str(letter).upper()
    return MORSE.get(new , '')

def dots_to_letter(dots):
    '''
    (str) --> str
    Converts morse to alphabet or numerical value. Ignores
    invalid input and '  ' for space.
    '''
    return REVERSE_MORSE.get(dots , '')
        

def convert_words(words):
    '''
    (str) --> str
    Converts phrases into morse code. Calls letter_to_dots function.
    '''
    translation = ''
    for char in words:
        translation += letter_to_dots(char)

    return translation

def convert_dots(dots):
    '''
    (str) --> str
    Converts morse code into phrases. Calls dots_to_letter function.
    '''
    listy = dots.split('  ')
    word = ''
    translation = ''
    for item in listy:
        if not item.strip():
            continue #skips empty word chunks
        new = item.split()
        for letter in new:
            word += dots_to_letter(letter)
        translation = translation + word + ' '
        word = ''
    return translation.strip()

# Device will call convert_words or convert_dots based on the signal received from the raspberry pi.

# function for awaiting button signal

stop_event = Event() #ensures stop event is protected

def signal_in():
    while not stop_event.is_set():

        message = []
        _button.wait_for_press() #press once to start texting
        _button.wait_for_release()


        while not stop_event.is_set():

            start = time.perf_counter()
            _button.wait_for_press()
            gap_time = time.perf_counter() - start
        
            if gap_time >= 1 and gap_time < 1.5:
                message.append(" ")
            elif gap_time >= 1.5 and gap_time <= 3:
                message.append("  ")


            start = time.perf_counter()
            _button.wait_for_release()
            press_time = time.perf_counter() - start

            if press_time <= 0.4:
                message.append('.')
            elif press_time <= 0.9:
                message.append('-')
            else:
                print("Received:" , convert_dots("".join(message)))
                break #resets message to wait for new one (ie. button press)
        

def signal_out():
    space = False
    while not stop_event.is_set():
        user_input = input("Connection secured. Send a message or type 'q' to leave: ")
        if user_input == 'q':
            stop_event.set()
            _led.close()
            _button.close()
            return
            # exit program for test phase, to re-run command "python3 morse_code_key.py"
            #os.system('sudo shutdown now')
        else:
            morse = convert_words(user_input)
            for char in morse:
                if char == ' ':
                    if space:
                        time.sleep(1)
                        space = False
                        continue
                    time.sleep(0.7)
                    space = True
                else:
                    space = False
                    if char == '.':
                        dot()
                    elif char == '-':
                        dash()
                    
                    

# only runs encrypt/decrypt code if program is run directly. Can import elsewhere to use functions.                
if __name__ == "__main__":
    
    # thread for background listening and start command
    thread_in = Thread(target=signal_in, daemon=True) #daemon ends the thread when program exits
    thread_in.start()

    signal_out()