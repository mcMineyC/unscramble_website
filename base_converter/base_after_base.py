#constants
base10 = tuple("0123456789")
base64 = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
binary = tuple("01")
hexadecimal = tuple("0123456789ABCDEF")
message_base = tuple(" abcdefghijklmnopqrstuvwxyz.,!'-") #base 32

#accepts string and base, returns int
def base_to_int(btiString, btiBase):
    assert type(btiString) == str, "btiString must be a string"
    btiString = btiString[::-1]
    btiInt = 0
    for i in range(len(btiString)):
        btiInt += btiBase.index(btiString[i]) * len(btiBase) ** i
    return btiInt

#accepts int and base, returns string
def int_to_base(itbInt, itbBase):
    assert type(itbInt) == int, "itbInt must be an integer"
    itbString = ""
    while itbInt > 0:
        itbString = itbBase[itbInt % len(itbBase)] + itbString
        itbInt = itbInt // len(itbBase)
    return itbString

def base_to_base(btbString, btbBaseIn, btbBaseOut):
    return int_to_base(base_to_int(btbString, btbBaseIn), btbBaseOut)