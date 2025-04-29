"""
main test file
"""

# import github
import subprocess
import shutil
import os
from lib import constants
from lib.gitobj.gitpr import GitPullRequest


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


def main():
    """main entrypoint"""
    print("Hello from pullrequest!")
    print(f"{constants.git_url}")
    inc_pr = GitPullRequest(111, "main", "fix-plot-twist2")
    inc_pr.filter = "bloomV3"
    ret_val = inc_pr.clone()
    print(f"{ret_val=}")
    val = GitPullRequest.creep(5, 4)
    print(f"{val=}")

    # Testing
    url = "https://github.com/PyGithub/PyGithub.git"
    get_workspace_by_pr(url, 3287)


if __name__ == "__main__":
    main()
