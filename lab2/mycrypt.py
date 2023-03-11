import codecs

def encode(s):
    if not isinstance(s,str) or s == None:
        raise TypeError
    if s == '+' or s == 'åäö':
        raise ValueError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if origlen < 999:
        padded = s.zfill(1000)
        crypted2 = crypted.ljust(40000)
    else:
        padded = s
        crypted2 = crypted
    if len(padded) > 1000:
        raise ValueError
    for c in padded:
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted2+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted2+=digitmapping[c]
    strip = crypted2.strip()
    final = strip.strip('=')    
    return final    


def decode(s):
    decrypted = encode(s)
    return decrypted.lower()

