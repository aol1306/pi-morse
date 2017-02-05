#!/usr/bin/python3
import time
import logging

# only set dot length
DOT = 0.3


DASH = 3*DOT

CODE = {
'a' : '.-',
'b' : '-...',
'c' : '-.-.',
'd' : '-..',
'e' : '.',
}

logging.basicConfig(level=logging.DEBUG)

def dot():
    logging.debug("dot")
    logging.info("singal on")
    time.sleep(DOT)
    logging.info("singal off")

def dash():
    logging.debug("dash")
    logging.info("singal on")
    time.sleep(DASH)
    logging.info("singal off")

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
        code = CODE[letter]
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

transmit('ab ab')
