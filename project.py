from pymem import Pymem
import time

pymem=Pymem("ac_client.exe")

def MemoryChanger(userInput):
    baseaddress = pymem.base_address + 0x18AC00
    ammo_pointer = GetAddress(baseaddress, [0x140])
    pymem.write_int(ammo_pointer, userInput)
    ammo = pymem.read_int(ammo_pointer)
    return ammo

def GetAddress(baseaddress, offsets):
    
    baseaddress = pymem.read_int(baseaddress)
    
    for offset in offsets:
        
        if offset != offsets[-1]:
            baseaddress = pymem.read_int(baseaddress+offset)
            
        else:
            return baseaddress+offset