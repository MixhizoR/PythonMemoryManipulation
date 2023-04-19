from pymem import Pymem

pymem=Pymem("ac_client.exe")

def MemoryChanger(userInput):
    if userInput == ' ':
        userInput = 0
    else:
        userInput = int(userInput)
    baseaddress = pymem.base_address + 0x18AC00
    ammo_pointer = GetAddress(baseaddress, [0x140])
    pymem.write_int(ammo_pointer, userInput)

def GetAddress(baseaddress, offsets):
    
    baseaddress = pymem.read_int(baseaddress)
    
    for offset in offsets:
        
        if offset != offsets[-1]:
            baseaddress = pymem.read_int(baseaddress+offset)
            
        else:
            return baseaddress+offset