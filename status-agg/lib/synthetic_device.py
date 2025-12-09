import random
from dataclasses import dataclass
from typing import Any, Self
import uvloop
import asyncio
from rich.progress import Progress, TaskID


@dataclass
class SyntheticDevice:
    loop: uvloop.Loop = uvloop.new_event_loop()

    def add_devices(self, dd: list[str] = ["sda", "sdb", "sdc"]) -> Self:
        """Builder to add devices"""
        self.device_list: list[str] = dd
        return self

    async def dd_main(self) -> None:
        """simulate a loop task gather"""

        tasklist = []
        for device in self.device_list:
            pbar = self.progress.add_task(f"Processing {device}...", total=100)
            task = self.loop.create_task(self.update_storage(device, pbar))
            tasklist.append(task)

        await asyncio.gather(*tasklist)

    async def update_storage(self, id: str, pbar: TaskID) -> None:
        """long running process"""
        for tdelay in range(10):
            while not self.progress.finished:
                self.progress.update(pbar, advance=10)
                await asyncio.sleep(random.randrange(1, 5))
        print(f"Finished sync on storage[{id.upper()}]")

    def parse_payload(self) -> dict[str, Any]:
        """Simulator for parsing custom configuration payload"""

        print("Running parse_payload")
        warnings: list[str] = []

        print("Checking payload if it exists ...")

        print("Found payload and will load for user configuration.")
        warnings.append("Invalid configuration found in payload but will proceed with defaults")

        return {"warning": warnings}

    def clone_device(self) -> dict[str, Any]:
        """Representation for cloning to device as a client-server with network"""

        print("Running clone_device")
        warnings: list[str] = []

        print("Contacting backend ...")
        warnings.append("A network issue was encountered while communicating with backend.")

        print("Synchronizing with device ...")
        warnings.append("Device has not come online within 10s, will retry.")

        try:
            with Progress() as self.progress:
                self.loop.run_until_complete(self.dd_main())
        except KeyboardInterrupt:
            print("Ok interruption is fine.")
        finally:
            self.loop.close()

        return {"warning": warnings}

    def generate_report(self) -> dict[str, Any]:
        """Report request from server on the results"""

        print("Running generate_report")
        warnings: list[str] = []
        warnings.append("The report generation timed out, please retry again after some time")
