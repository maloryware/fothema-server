from bluez_peripheral.gatt.service import Service
from bluez_peripheral.gatt.characteristic import characteristic, CharacteristicFlags as CharFlags, CharacteristicReadOptions as ReadOptions, CharacteristicWriteOptions as WriteOptions
from bluez_peripheral.gatt.descriptor import descriptor, DescriptorFlags as DescFlags
from fileman import Config
import json
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
        toSend = bytes("pong!")
        print(f"Ping function called! Sending {toSend}")
        return bytes("pong!", "utf-8")

    @characteristic("413B", CharFlags.READ)
    def send(self, options):
        # print(f"Sending config: {toSend}")
        print(f"sending config with offset={options.offset}")
        return bytes(json.dumps(Config.read()), "utf-8")
    
    @characteristic("413C", CharFlags.WRITE)
    def receive(self, config, options):
        Config.write(config)
        print("Updating config")

    @characteristic("413D", CharFlags.WRITE)
    def backup(self, options):
        Config.write(Config.read, Identifiers.backup_config)
    
    @characteristic("413E", CharFlags.READ)
    def connect(self, deviceInfo, options):
        print(f"device connected, info: {deviceInfo}")
        
    ###@characteristic("4140", CharFlags.READ)
    ###def resetDefault(self, options):
    ###    print("Resetting config to default [UNIMPLEMENTED]")
