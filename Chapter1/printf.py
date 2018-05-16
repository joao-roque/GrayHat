from ctypes import *

# python 3.6 requires the extra b before string 
msvcrt = CDLL("msvcrt")
message_string = b"Hello World\n"

msvcrt.printf(b"Testing: %s", message_string)

