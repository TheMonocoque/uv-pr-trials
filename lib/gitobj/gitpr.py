"""
test class git obj
"""


class GitPullRequest:
    """quick"""

    site: str = "foo"
    filter: str = "bloomv1"
    audio_dac: dict = { "type": "R2R", "bit": 24, "can_dsd": True }


    def __init__(self, prnum: int, base_branch: str, head_branch: str):
        self.pr: int = prnum
        self.base_branch: str = base_branch
        self.head_branch: str = head_branch

    def clone(self) -> int:
        """clone"""
        print(f"Cloning {self.pr} that delivers to {self.base_branch} from {self.head_branch}")
        print(f"Play on dac {self.filter} that delivers to {self.audio_dac}")
        return self.pr + len(self.base_branch) + len(self.head_branch)

    def scan(self, scan_type: str = "Fast Scan") -> None:
        """scan"""
        print(f"Running scan mode {scan_type}")

    @staticmethod
    def creep(a: int, b: int) -> int:
        """just dumb multiplier to try staticmethod"""
        return a * b
