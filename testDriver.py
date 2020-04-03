import re

stringd = '''hello? there A-Z-R_T(,**), world, welcome to python.
this **should? the next line#followed- by@ an#other %million^ %%like $this.'''
final = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in stringd.split("\n")]
print(''.join(final).rstrip()+'.txt')