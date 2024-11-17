from bluez_peripheral.util import *
from bluez_peripheral.gatt.service import ServiceCollection
from bluez_peripheral.advert import Advertisement
from bluez_peripheral.agent import NoIoAgent
from service import *
from identifiers import Identifiers
import asyncio

# for information on Bluetooth assigned numbers, see https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf

service_ids = [Identifiers.core_service]
appearance = 0
timeout = 99999


async def main():
    print("connected!")
    bus = await get_message_bus()
    agent = NoIoAgent()
    service = MirrorServ()
        
    await service.register(bus)
    await agent.register(bus)

    adapter = await Adapter.get_first(bus)

    advert = Advertisement("FOTHEMA Bluetooth Service", service_ids, appearance, timeout)
    
    await advert.register(bus, adapter)
    while True:
        # Update the heart rate.
        # Handle dbus requests.
        await asyncio.sleep(5)

    await bus.wait_for_disconnect()
    
asyncio.run(main())