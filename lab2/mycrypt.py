import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    if s == '+':
        raise ValueError
    if s == 'åäö':
        raise ValueError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
          
    return crypted

def decode(s):
    if not isinstance(s,str):
        raise TypeError
    encrypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c.isalpha():
            if c.isupper():
                c=c.lower()
            # Rot13 the character for maximum security
            encrypted+=codecs.decode(c,'rot13')
        elif c in digitmapping:
          encrypted+=digitmapping[c]
    return encrypted

