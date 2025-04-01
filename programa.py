import os
import ctypes



if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dllfile = dir_path + '/base58.so'
    pathdll = os.path.realpath(dllfile)
    base58 = ctypes.CDLL(pathdll)
    
    print(dir(base58))
