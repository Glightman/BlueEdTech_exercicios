import time as tm
for sec in range(5, 0, -1):
    tm.sleep(1)
    print(f'\033[04;31m{sec}')
for go in range(1, 11):
    tm.sleep(0.2)    
    print('\033[04;33;42mGO BLUE!!!!... ')