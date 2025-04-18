from ctypes import *
"""
types defined in ctypes (they are all classes. create instance like ci = c_int(25), get value ci.value, change value ci.value=20): 
  c_bool, 
  c_char : char, 
  c_byte : char, 
  c_ubyte : unsigned char
  c_short : short
  c_ushort : unsigned short
  c_int : int
  c_uinit : unsigned int
  c_long : long
  c_ulong : unsigned long
  c_longlong : long long
  c_ulonglong : unsigned long long
  c_size_t : size_t
  c_float : float
  c_double : double
  c_longdouble : long double
  c_char_p : char *
  c_void_p : void *

  Structure and Union, _fields_ must be defined.
    class POINT(Structure):
        _fields_ = [("x", c_int),
                ("y", c_int)]
    point = POINT(10, 20)
    print(point.x, point.y)

    class RECT(Structure):
        _fields_ = [("upperleft", POINT),
                 ("lowerright", POINT)]

"""
