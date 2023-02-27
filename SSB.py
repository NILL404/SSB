import os, sys, platform
print ('\033[1;34m\nBYPASSED BY NILL XD')
print ('\033[1;33m\nBYPASSED BY NILL XD')
print ('\033[1;35m\nBYPASSED BY NILL XD')
print ('\033[1;31m\nBYPASSED BY NILL XD')
print ('\033[1;36m\nBYPASSED BY NILL XD')
print ('\033[1;32m\nBYPASSED BY NILL XD')
os.system('xdg-open https://facebook.com/NKD403')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sarfraz.so Sarfraz32.so')
except:
    pass
os.system('rm -rf Sarfraz.so Sarfraz32.so')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Sarfraz.so'):
        os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/Sarfraz.cpython-311.so?raw=true -o Sarfraz.so') 
        import Sarfraz
        
