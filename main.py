#!/usr/bin/env python
"""
main test file
"""

from pydantic_settings import BaseSettings
from dotenv import dotenv_values
import os

# import github
import lib.shared as shd
import lib.winners.wincombo as combowin
import lib.mylistr.runstrtimer as rstim
from lib.eventcache.eventcache import EventCache
import lib.mppool.run_pool as mp


class Settings(BaseSettings):
    database_url: str = ""
    auth_key: str = ""
    debug: bool = False

    class Config:
        env_file: str = "settings.env"


def main():
    """main entrypoint"""
    print("Hello from pullrequest!")

    # pydantic much heavier than dotenv
    settings = Settings()
    print(f"Database URL: {settings.database_url}")
    config = {
        **dotenv_values(".env.shared"),
        **dotenv_values(".env.secret"),
        **os.environ,
    }
    print(f"Quick config {config['GLOBAL_NAME']}")

    shd.config_test()
    shd.clone_test()
    shd.contextrunner()

    combowin.demo_combo_choice_sample()
    rstim.run_loop_test()

    run1: mp.Runnable = mp.NormalRun()
    run1.run_function(mp.f)

    runner: mp.Runnable = mp.PoolRun()
    runner.run_function(mp.f)
    runner.report()

    test_event: EventCache = EventCache()
    for event in shd.produce_synthetic_event_list():
        test_event.update(event["name"], event["time"])

    # Testing
    # url = "https://github.com/PyGithub/PyGithub.git"
    # GitPullRequest.get_workspace_by_pr(url, 3287)


if __name__ == "__main__":
    main()
