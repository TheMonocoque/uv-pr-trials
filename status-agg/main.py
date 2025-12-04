#!/usr/bin/env python

import lib.synthetic_device as sdev
import lib.message_aggregator as msa


def main():
    print("Hello from status-aggregator!")

    agg = msa.MessageAggregator().create_list()

    # Test setting to invalid level
    # agg.severity_level = "critical"

    # Run workflow to create synthetic data
    devices: list[str] = ["sda", "sdb", "sdc", "sdd"]
    wf = sdev.SyntheticDevice().add_devices(devices)
    agg.aggregate(wf.parse_payload())
    agg.aggregate(wf.clone_device())
    agg.aggregate(wf.generate_report())

    # Display the messages
    agg.print_messages()


if __name__ == "__main__":
    main()
