from pymem import Pymem
import time

pymem=Pymem("ac_client.exe")

def main():
    baseaddress = pymem.base_address + 0x18AC00
    ammo_pointer = GetAddress(baseaddress, [0x140])
    while True:
        ammo = pymem.read_int(ammo_pointer)
        print(ammo)
        pymem.write_int(ammo_pointer, 99)
        time.sleep(0.4)

def GetAddress(baseaddress, offsets):
    
    baseaddress = pymem.read_int(baseaddress)
    
    for offset in offsets:
        
        if offset != offsets[-1]:
            baseaddress = pymem.read_int(baseaddress+offset)
            
        else:
            return baseaddress+offset
            
            
            
    

if __name__=="__main__":
    main()