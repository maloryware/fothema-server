from bluez_peripheral.gatt.service import Service
from bluez_peripheral.gatt.characteristic import characteristic, CharacteristicFlags as CharFlags
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
    def ping(self):
        toSend = bytes("pong!")
        print(f"Ping function called! Sending {toSend}")
        return bytes("pong!", "utf-8")

    @characteristic("413B", CharFlags.READ)
    def send(self, arg):
        print(f"2nd argument: {arg}")
        toSend = bytes(json.dumps(Config.read()), "utf-8")
        print(f"Sending config")
        return toSend
    
    @characteristic("413C", CharFlags.WRITE)
    def receive(self, config):
        Config.write(config)
        print("Updating config")

    @characteristic("413D", CharFlags.WRITE)
    def backup(self):
        Config.write(Config.read, Identifiers.backup_config)
    
    @characteristic("413E", CharFlags.READ)
    def connect(self, deviceInfo):
        print(f"device connected, info: {deviceInfo}")

    @characteristic("4140", CharFlags.READ)
    def resetDefault(self, options):
        print("Resetting config to default [UNIMPLEMENTED]")
