# Serial spawn for pexpect

[![Build](https://github.com/antoniovazquezblanco/pexpect-serialspawn/actions/workflows/build.yml/badge.svg)](https://github.com/antoniovazquezblanco/pexpect-serialspawn/actions/workflows/build.yml)
[![PyPI](https://img.shields.io/pypi/v/pexpect-serialspawn)](https://pypi.org/project/pexpect-serialspawn/)
[![pexpect-serialspawn](https://snyk.io/advisor/python/pexpect-serialspawn/badge.svg)](https://snyk.io/advisor/python/pexpect-serialspawn)

Interact with serial devices using pexpect.

## Installation

Just use pip :)

```
pip install pexpect-serialspawn
```

## Usage

```python
import serial
from pexpect_serialspawn import SerialSpawn

# Initialize your serial device
ser = serial.Serial('COM1', 115200)

# Spawn a pexpect object
ss = SerialSpawn(ser, encoding='utf-8')

# Use as any other pexpect spawns...
ss.sendline('Hello')
ss.expect('World')
```
