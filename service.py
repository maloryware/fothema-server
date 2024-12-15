from bluez_peripheral.gatt.service import Service
from bluez_peripheral.gatt.characteristic import characteristic, CharacteristicFlags as CharFlags, CharacteristicReadOptions as ReadOptions, CharacteristicWriteOptions as WriteOptions
from fileman import Config
import os
from consts import Identifiers

class MirrorServ(Service):

    def __init__(self):
        super().__init__(Identifiers.core_service, True)
    
    # purely testing
    @characteristic("4139", CharFlags.NOTIFY | CharFlags.WRITE)
    def update(self, options):
        pass
    
    @characteristic("413A", CharFlags.READ)
    def ping(self, options):

        print(f"Ping!")
        return bytes("SERVER: pong!", "utf-8")

    @characteristic("413B", CharFlags.WRITE)
    def backup(self, options):
        Config.write(Config.read, Identifiers.backup_config)
    
    @characteristic("413C", CharFlags.READ)
    def connect(self, options):
        print(f"device connected, info: nil")
        return bytes("connected", "utf-8")

    @characteristic("413D", CharFlags.READ)
    def getConfigLocation(self, options):
        return bytes(Identifiers.config, "utf-8")
    
    @characteristic("413E", CharFlags.READ)
    def getBackupLocation(self, options):
        return bytes(Identifiers.backup_config, "utf-8")
    
    @characteristic("4140", CharFlags.READ)
    def restartService(self, options):
        os.system('systemctl restart fothema-mm.service --user')
        return bytes("restarting", "utf-8")
        
        


    # DON'T. do not. please. there's better ways. i just don't. know. how.


    #remember: config commented out - go to consts.py
    @characteristic("4881", CharFlags.READ)
    def send1(self, options):
        print("Sending...")
        return bytes(Config.read(0), "utf-8")
    
    @characteristic("4882", CharFlags.READ)
    def send2(self, options):
        print("Sending...")
        return bytes(Config.read(1), "utf-8")
    
    @characteristic("4883", CharFlags.READ)
    def send3(self, options):
        print("Sending...")
        return bytes(Config.read(2), "utf-8")
    
    @characteristic("4884", CharFlags.READ)
    def send4(self, options):
        print(f"Sending... Complete!\nLast out: {Config.read(3)}")
        return bytes(Config.read(3), "utf-8")
    
    #remember: config commented out - go to consts.py
    @characteristic("4991", CharFlags.READ)
    def clearBuf(self, options):
        Config.write("", Identifiers.buf)
        print("Cleared buf")
        #return bytes("SERVER: Cleared buf", "utf-8")
    @characteristic("4992", CharFlags.WRITE)
    def receiveBuf(self, config, options):
        Config.saveToBuffer(config)
        print("Saved to buffer")
        #return bytes("SERVER: Saved to buffer.", "utf-8")
    @characteristic("4993", CharFlags.WRITE)
    def finishBuf(self, options):
        Config.writeFromBuffer()
        print("Finished buffer saving - Wrote buffer to config")
        #return bytes("SERVER: Finished buffer saving - Wrote buffer to config; You can now issue a restart.", "utf-8")
