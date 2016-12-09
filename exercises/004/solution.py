#!/usr/bin/python
import string
n = string.ascii_lowercase[::-1]
j = n.replace('a', 'A')
m = j.replace('e', 'E')
n = m.replace('i', 'I')
o = n.replace('o', 'O')
p = o.replace('u', 'U')
print(p)
