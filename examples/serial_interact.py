#!/usr/bin/env python

import serial
from pexpect_serialspawn import SerialSpawn

s = serial.Serial('COM20', baudrate=115200, timeout=1)
ss = SerialSpawn(s)
ss.interact()
