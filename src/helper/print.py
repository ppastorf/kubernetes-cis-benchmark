#!/bin/env python3

bldred = '\033[1;31m'
bldgrn = '\033[1;32m'
bldblu = '\033[1;34m'
bldylw = '\033[1;33m'
bldcyn = '\033[1;36m'
bldgry = '\033[1;37m'
txtrst = '\033[0m'

def PrintHeader():
    print(f'''{bldylw}# ------------------------------------------------------------------------------
# Kubernetes CIS benchmark
#
# NeuVector, Inc. (c) 2020-
#
# NeuVector delivers an application and network intelligent container security
# solution that automatically adapts to protect running containers. Don’t let
# security concerns slow down your CI/CD processes.
# ------------------------------------------------------------------------------ 
''')

def PrintInfo(severity: str, message: str, level: int =None, automated=None, scored=None):
    match level:
        case None:
            level_msg = ""
        case _:
            level_msg = f"[Level {level}]"

    match automated:
        case None:
            automated_msg = ""
        case True:
            automated_msg = f"{bldcyn}[Automated]{txtrst}"
        case False:
            automated_msg = f"{bldcyn}[Manual]{txtrst}"

    match scored:
        case None:
            scored_msg = ""
        case True:
            scored_msg = f"[Scored]"
        case False:
            scored_msg = f"[Not Scored]"


    match severity:
        case "info":
            severity_msg = f"{bldblu}[INFO]{txtrst}"
        case "pass":
            severity_msg = f"{bldgrn}[PASS]{txtrst}"
        case "warn":
            severity_msg = f"{bldred}[WARN]{txtrst}"

    print(f"{severity_msg}{level_msg}{automated_msg}{scored_msg} {message}")
