from bluez_peripheral.gatt.service import Service
from bluez_peripheral.gatt.characteristic import characteristic, CharacteristicFlags as CharFlags
from bluez_peripheral.gatt.descriptor import descriptor, DescriptorFlags as DescFlags
import struct
from identifiers import Identifiers




class MirrorServ(Service):
    def __init__(self):
        super().__init__(Identifiers.core_service, True)


    @characteristic("4139", CharFlags.NOTIFY | CharFlags.WRITE)
    def update(self, options):
        pass
    
    @characteristic("413A", CharFlags.READ)
    def ping(self, options):
        return bytes("pong!")



    def connect(self):
        print("bazinga")