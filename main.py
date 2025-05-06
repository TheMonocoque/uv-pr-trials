#!/usr/bin/env python
"""
main test file
"""

# import github
from functools import partial
from pathlib import Path

from lib import constants
from lib.gitobj.gitpr import GitPullRequest
import lib.gitobj.constants as const
import lib.winners.wincombo as combowin
import lib.mylistr.runstrtimer as rstim


def main():
    """main entrypoint"""
    print("Hello from pullrequest!")
    mydir = Path(__file__).resolve().parent
    print(f"Directory: {mydir}")
    print(f"{constants.git_url}")
    print(f"{const.site_url}")
    inc_pr = GitPullRequest(111, "main", "fix-plot-twist2")
    inc_pr.filter = "bloomV3"
    ret_val = inc_pr.clone()
    print(f"{ret_val=}")

    specify_prnum_ghpr: partial = partial(GitPullRequest, base_branch="main", head_branch="mybranch")
    pr2 = specify_prnum_ghpr(123)
    pr2.clone()

    specify_prnum_branch_ghpr: partial = partial(GitPullRequest, base_branch="main")
    pr3 = specify_prnum_branch_ghpr(123, head_branch="food")
    pr3.clone()

    combowin.demo_combo_choice_sample()
    rstim.run_loop_test()


    # Testing
    # url = "https://github.com/PyGithub/PyGithub.git"
    # GitPullRequest.get_workspace_by_pr(url, 3287)


if __name__ == "__main__":
    main()
