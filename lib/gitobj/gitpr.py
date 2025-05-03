"""
test class git obj
"""

import subprocess
import shutil
import os


class GitPullRequest:
    """quick"""

    site: str = "foo"
    filter: str = "bloomv1"
    audio_dac: dict = {"type": "R2R", "bit": 24, "can_dsd": True}

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
    def get_workspace_by_pr(url: str, pr_num: int):
        """
        Testing workspace cloning of pull-requests Reason for doing this is that
        processing PRs are often done by forks which a normal git clone operation
        to branch will not work. However GitHub has the pull request submission and
        saved in a different refs localtion 'pulls'
        """

        # TODO: GitHub module does not appear to be able to sparse and clone all files
        # g = github.Github()
        # repo = g.get_repo("PyGithub/PyGithub")
        # pr = repo.get_pull(3287)
        # return pr.get_files()

        tmp_workspace_dir = "temp"
        if os.path.exists(tmp_workspace_dir):
            shutil.rmtree(tmp_workspace_dir)
        os.mkdir(tmp_workspace_dir)
        os.chdir(tmp_workspace_dir)

        # Use call to not care about stdout/stderr but only return code
        cmd_git_init: list[str] = "git init .".split()
        subprocess.call(cmd_git_init, stdout=None, timeout=5)

        cmd_add_remote: list[str] = f"git remote add origin {url}".split()
        subprocess.call(cmd_add_remote, stdout=None, timeout=5)

        # Use run to capture output and not always print to screen/log
        cmd_fetch: list[str] = f"git fetch origin pull/{pr_num}/merge:pr_workspace".split()
        process_output: subprocess.CompletedProcess = subprocess.run(cmd_fetch, check=False, capture_output=True, timeout=600)
        if process_output.returncode != 0:
            print(f"{process_output.stdout=}")
            print(f"{process_output.stderr=}")

        # Switch to the pr workspace
        cmd_checkout: list[str] = "git checkout pr_workspace".split()
        process_output: subprocess.CompletedProcess = subprocess.run(cmd_checkout, check=False, capture_output=True, timeout=600)
        if process_output.returncode != 0:
            print(f"{process_output.stdout=}")
            print(f"{process_output.stderr=}")
