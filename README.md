# Serial spawn for pexpect

Interact with serial devices using pexpect.


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
