#!/usr/bin/env python

import lib.shared as libshare
import lib.message_aggregator as msa


def main():
    print("Hello from status-aggregator!")

    agg = msa.MessageAggregator().create_list()

    # Test setting to invalid level
    # agg.severity_level = "critical"

    # Run workflow to create synthetic data
    agg.aggregate(libshare.parse_payload())
    agg.aggregate(libshare.clone_device())
    agg.aggregate(libshare.generate_report())

    # Display the messages
    agg.print_messages()


if __name__ == "__main__":
    main()
