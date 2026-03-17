def parrot(voltage, state = 'a stiff', action = 'voom'):
    print("-- This parrot wouldn't", action, end = ' ')
    print("if you put", voltage, "volts through it.", end = ' ')

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
