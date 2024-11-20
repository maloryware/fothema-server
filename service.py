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
        return bytes("pong!")

    @characteristic("413B", CharFlags.READ)
    def send(self):
        return bytes(json.dumps(Config.read))
    
    @characteristic("413C", CharFlags.WRITE)
    def receive(self):
        Config.write()

    @characteristic("413D", CharFlags.WRITE)
    def backup(self):
        Config.write(Config.read, Identifiers.backup_config)

    def connect(self):
        print("bazinga")