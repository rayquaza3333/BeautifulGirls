import re

text= 'as..asas.a.ss.s.saa.as.s.asasasa.sa.sasas.as.ss'

x = r'^[as]'

print(re.findall(x,text))
