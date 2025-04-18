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

    class Int(Structure):
        _fields_ = [("first_16", c_int, 16),
                    ("second_16", c_int, 16)]

    
    """

class ArmInstructionBase_S(Structure):
     _fields_ = [
         ("Lower28bits", c_ulong, 28),
         ("Condition", c_ulong, 4)
     ]
    def encode():
        pass
    def decode(byteArr):
        pass

class ArmInstructionDataProcessing_S(ArmInstructionBase_S):
     _fields_ = [
         ("Op2", c_ulong, 12), # 0-11
         ("Rs", c_ulong, 4), # 12-15
         ("Rn", c_ulong, 4), # 16-19
         ("S", c_ulong, 1), # 20
         ("OpCode", c_ulong, 4), # 21-24
         ("I", c_ulong, 1), # 25
         ("Rsv1", c_ulong, 2), # 26-27, 0b00
         ("Condition", c_ulong, 4) # 28-31
     ]

class ArmInstructionMultiply_S(ArmInstructionBase_S):
     _fields_ = [
         ("Rm", c_ulong, 4), # 0-3
         ("Rsv1", c_ulong, 4), # 4-7, 0b1001
         ("Rs", c_ulong, 4), # 8-11
         ("Rn", c_ulong, 4), # 12-15
         ("Rd", c_ulong, 4), # 16-19
         ("S", c_ulong, 1), # 20
         ("A", c_ulong, 1), # 21
         ("Rsv1", c_ulong, 6), # 22-27, 0b000000
         ("Condition", c_ulong, 4) # 28-31
     ]
class BitsInByte(Structure):
    _fields_ = [
        ("Bit0", c_ubyte, 1),
        ("Bit1", c_ubyte, 1),
        ("Bit2", c_ubyte, 1),
        ("Bit3", c_ubyte, 1),
        ("Bit4", c_ubyte, 1),
        ("Bit5", c_ubyte, 1),
        ("Bit6", c_ubyte, 1),
        ("Bit7", c_ubyte, 1)        
    ]
class NibblesInByte(Structure):
    _fields_ = [
       ("Nibble0", c_ubyte, 4),
       ("Nibble1", c_ubyte, 4)
    ]
class ArmInstruction_U(Union):
    _fields_ = [
       ("asBits", BitsInByte * 4),
       ("asNibbles", NibblesInByte * 4),
        ("asBytes", c_ubyte * 4),
        ("asHalfs", c_ushort * 2),
        ("asWord", c_ulong * 1),
        ("asInstructionBase", ArmInstructionBase_S),
    ]

    
