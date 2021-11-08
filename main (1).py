def rot(num):
    port = ''
    lonkiv = [kons for kons in str(num)]
    if '6' in lonkiv:
        redfa = a.index('6')
        a.insert(redfa, '9')
        a.pop(redfa + 1)
    else:
        for kons in lonkiv:
            port += kons
    return print(port)
