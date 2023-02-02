A python library that uses socketing to allow people to fly a tello drone using python
Author: Aarav Prakash

Example code:

from tellolib import tello

tello = tello.Tello(1111)
tello.takeoff()

In this instance, 1111 is the UDP port that the computer sets the server to communicate with the tello to be.

List of commands:

takeoff() sends a command to the tello to take off
land() sends a command to the tello to land

movement commands

forward(num)

backward(num)

left(num)

right(num)

User can rotate clockwise or counterclockwise

rotatecw(degree)

rotateccw(degree)

sendcommand(str) sends command str to tello

receive() receives a message if the tello sends one

To install:

pip install tellolib

link to PyPI: https://pypi.org/project/tellolib/
