from typing import Any
import uvloop
import random

loop = uvloop.new_event_loop()


async def dd_main() -> None:
    """simulate a loop task gather"""

    tasklist = []
    for tasknum in range(1, 4):
        task = loop.create_task(update_storage(str(tasknum)))
        tasklist.append(task)
    await uvloop.__asyncio.gather(*tasklist)


async def update_storage(id: str = "default") -> None:
    """long running process"""
    for zzz in range(10):
        print(f"Updating storage[{id}] on device - {zzz}")
        await uvloop.__asyncio.sleep(random.randrange(1, 5))


def parse_payload() -> dict[str, Any]:
    """Simulator for parsing custom configuration payload"""

    print("Running parse_payload")
    warnings: list[str] = []

    print("Checking payload if it exists ...")

    print("Found payload and will load for user configuration.")
    warnings.append("Invalid configuration found in payload but will proceed with defaults")

    return {"warning": warnings}


def clone_device() -> dict[str, Any]:
    """Representation for cloning to device as a client-server with network"""

    print("Running clone_device")
    warnings: list[str] = []

    print("Contacting backend ...")
    warnings.append("A network issue was encountered while communicating with backend.")

    print("Synchronizing with device ...")
    warnings.append("Device has not come online within 10s, will retry.")

    try:
        loop.run_until_complete(dd_main())
    except KeyboardInterrupt:
        print("Ok interruption is fine.")
    finally:
        loop.close()

    return {"warning": warnings}


def generate_report() -> dict[str, Any]:
    """Report request from server on the results"""

    print("Running generate_report")
    warnings: list[str] = []
    warnings.append("The report generation timed out, please retry again after some time")

    return {"warning": warnings}
