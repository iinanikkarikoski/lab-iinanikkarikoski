import codecs

def encode(s):
    if not isinstance(s,str) or s == None:
        raise TypeError
    if s == '+' or s == 'åäö':
        raise ValueError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if origlen < 1000:
        padded = s.ljust(4800)
    else:
        padded = s
    if len(s) > 1000:
        raise ValueError
    for c in padded:
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]    
    return crypted    


def decode(s):
    decrypted = encode(s)
    return decrypted.lower()

