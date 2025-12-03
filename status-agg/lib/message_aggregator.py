from typing import Any, Self
from dataclasses import dataclass


@dataclass
class MessageAggregator:
    severity_level: str = "warning"

    def create_list(self) -> Self:
        self.message_list: list[str] = []
        return self

    def aggregate(self, input: dict[str, Any]) -> None:
        if not input:
            return
        if not input.get(self.severity_level):
            print(f"WARNING: no severity found for {self.severity_level}")
            return
        self.message_list.append("\n".join(input[self.severity_level]))

    def print_messages(self) -> None:
        """Display all the warnings at the end so it does not get lost"""
        if not self.message_list:
            return
        print("\n\n")
        print("#" * 50)
        print("Summarizing warning messages:")
        print("-" * 50)
        print(f"{'\n'.join(self.message_list)}")
        print("#" * 50)
        print("\n\n")
