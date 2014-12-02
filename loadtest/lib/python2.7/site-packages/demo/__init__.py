import os, unittest

# figure all the modules available
dir = os.path.split(__file__)[0]
mods = {}
l = []
__all__ = []
for file in os.listdir(dir):
    if not file.endswith('.py') or file == '__init__.py':
        continue
    name = file[5:-3]
    mods[name] = __import__(file[:-3], globals(), locals(), [])
    __all__.append(name)
    l.append(mods[name].suite())

def suite():
    return unittest.TestSuite(l)

