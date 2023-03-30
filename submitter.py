#!usr/bin/env python
# -*- coding: utf-8 -*-

import os, argparse
from datetime import date
from pathlib import Path


# main function
if __name__ == "__main__":
    copyrightMessage = (
        "Contact: software@cbica.upenn.edu\n\n"
        + "This program is NOT FDA/CE approved and NOT intended for clinical use.\nCopyright (c) "
        + str(date.today().year)
        + " University of Pennsylvania. All rights reserved."
    )

    cwd = Path(__file__).resolve().parent
    all_files_and_folders = os.listdir(cwd)

    parser = argparse.ArgumentParser(
        prog="Experiment_Submitter",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Submit GPU experiments on CUBIC Cluster.\n\n"
        + copyrightMessage,
    )

    parser.add_argument(
        "-r",
        "--runnerscript",
        metavar="",
        default=os.path.join(cwd, "runner.sh"),
        type=str,
        help="'runner.sh' script to be called.",
    )
    parser.add_argument(
        "-e",
        "--email",
        metavar="",
        default="user -at- site.domain",
        type=str,
        help="Email address to be used for notifications.",
    )
    parser.add_argument(
        "-gpu",
        "--gputype",
        metavar="",
        default="gpu",
        type=str,
        help="The parameter to pass after '-l' to the submit command.",
    )

    args = parser.parse_args()

    for i in range(11):
        jobname = "gpuCheck_" + args.gputype + "_" + str(i)
        
        command = (
            "qsub -N L_"
            + jobname
            + " -M "
            + args.email
            + " -l "
            + args.gputype
            + " "
            + args.runnerscript
        )
        print(command)
        os.system(command)
