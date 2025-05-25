#!/usr/bin/env python
"""
main test file
"""

# import github
from functools import partial
from pathlib import Path
from contextlib import contextmanager

from lib import constants
from lib.gitobj.gitpr import GitPullRequest
import lib.gitobj.constants as const
import lib.winners.wincombo as combowin
import lib.mylistr.runstrtimer as rstim
from lib.eventcache.eventcache import EventCache


def produce_synthetic_event_list() -> list[dict]:
    """synthetic event list"""
    cycle: list[dict] = []
    cycle.append({"name": "Scanning", "time": 50})
    for inject_time in range(60, 199):
        cycle.append({"name": "ReportGeneration", "time": inject_time})
    cycle.append({"name": "Finished", "time": 10})
    print(f"Total synthetic events produced: {len(cycle)}")
    return cycle


def config_test():
    config: dict = {}
    config.update({"random": "relay"})
    config["app"] = {}
    config["app"].update({"name": "foo"})
    print(f"{config}")


def clone_test():
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


def contextrunner():
    """test contextmanager"""

    def acquire_resource(*args, **kwargs):
        print(args, kwargs)
        return { "message" : args[0], "keys": kwargs}

    def release_resource():
        print("Releasing resource")

    @contextmanager
    def resource_one(*args, **kwargs):
        resource = acquire_resource(*args, **kwargs)
        try:
            yield resource
        finally:
            release_resource()

    with resource_one("This is an example contextrunner", trivia="jeopardy") as resone:
        print(f"Resource ONE - {resone}")

    print("Done with contextrunner")


def main():
    """main entrypoint"""
    print("Hello from pullrequest!")

    config_test()
    clone_test()
    contextrunner()

    combowin.demo_combo_choice_sample()
    rstim.run_loop_test()

    test_event: EventCache = EventCache()
    for event in produce_synthetic_event_list():
        test_event.update(event["name"], event["time"])

    # Testing
    # url = "https://github.com/PyGithub/PyGithub.git"
    # GitPullRequest.get_workspace_by_pr(url, 3287)


if __name__ == "__main__":
    main()
