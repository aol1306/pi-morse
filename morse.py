#!/usr/bin/python3
import time
import logging
import sys

LED_CHANNEL = 3

# only set dot length
DOT = 0.1
DASH = 3*DOT


CODE = {
'a' : '.-',
'b' : '-...',
'c' : '-.-.',
'd' : '-..',
'e' : '.',
'f' : '..-.',
'g' : '--.',
'h' : '....',
'i' : '..',
'j' : '.---',
'k' : '-.-',
'l' : '.-..',
'm' : '--',
'n' : '-.',
'o' : '---',
'p' : '.--.',
'q' : '--.-',
'r' : '.-.',
's' : '...',
't' : '-',
'u' : '..-',
'v' : '...-',
'w' : '.--',
'x' : '-..-',
'y' : '-.--',
'z' : '--..',
'.' : '.-.-.-',
',' : '--..--',
'?' : '..--..',
'/' : '-..-.',
'@' : '.--.-.',
'1' : '.----',
'2' : '..---',
'3' : '...--',
'4' : '....-',
'5' : '.....',
'6' : '-....',
'7' : '--...',
'8' : '---..',
'9' : '----.',
'0' : '-----',
}

logging.basicConfig(level=logging.DEBUG)

try:
    import RPi.GPIO as gpio
except RuntimeError:
    quit("Error importing RPi.GPIO. Try running with sudo.")

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(LED_CHANNEL, gpio.OUT, initial=gpio.LOW)

def dot():
    logging.debug("dot")
    logging.info("singal on")
    gpio.output(LED_CHANNEL, True)
    time.sleep(DOT)
    logging.info("singal off")
    gpio.output(LED_CHANNEL, False)

def dash():
    logging.debug("dash")
    logging.info("singal on")
    gpio.output(LED_CHANNEL, True)
    time.sleep(DASH)
    logging.info("singal off")
    gpio.output(LED_CHANNEL, False)

def part_of_letter_sleep():
    logging.debug("part of letter sleep")
    time.sleep(DOT)

def letter_sleep():
    logging.debug("letter sleep")
    time.sleep(DASH)

def word_sleep(): 
    logging.debug("word sleep")
    time.sleep(DOT*7)

def transmit_letter(letter):
    letter = letter.lower()
    logging.debug("transmitting letter "+letter)
    try:
        code = CODE[str(letter)]
    except KeyError:
        logging.error("no such letter")
        return
    size = len(code)
    i = 1
    for sign in code:
        if sign == '.':
            dot()
        if sign == '-':
            dash()
        if (i<size):
            part_of_letter_sleep()
        i += 1

def transmit_word(word):
    size = len(word)
    i = 1
    for letter in word:
        transmit_letter(letter)
        if (i<size):
            letter_sleep()
        i += 1

def transmit(text):
    text = text.split()
    size = len(text)
    i = 1
    for word in text:
        transmit_word(word)
        if (i<size):
            word_sleep()
        i += 1

if __name__ == "__main__":
    try:
        transmit(sys.argv[1])
        gpio.cleanup()
    except IndexError:
        quit("usage: ./morse.py '[text]'")
