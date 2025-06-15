#!/bin/env python3

import sys
import os

# Make it able to import src/
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '../../src'
        )
    )
)

from checks import FilePermissionCheck, FileOwnershipCheck
from helper import PrintHeader, PrintInfo

if __name__ == '__main__':
    PrintHeader()
    PrintInfo("info", "1 - Control Plane Components")
    PrintInfo("info", "1.1 - Master Node Configuration Files")

    kops = False
    if kops:
        in_file = "/etc/kubernetes/manifests/kube-apiserver.manifest"
    else:
        in_file = "/etc/kubernetes/manifests/kube-apiserver.yaml"

    check_1_1_1 = FilePermissionCheck(
        title="1.1.1  - Ensure that the API server pod specification file permissions are set to 644 or more restrictive (Automated)",
        level=1,
        automated=True,
        scored=True,
        file=in_file,
        max_allowed=0o644,
    )

    check_1_1_1.Run()
    check_1_1_1.Print()

    check_1_1_2 = FileOwnershipCheck(
        title="1.1.2  - Ensure that the API server pod specification file ownership is set to root:root (Automated)",
        level=1,
        automated=True,
        scored=True,
        file=in_file,
        required_uid=0,
        required_gid=0,
    )

    check_1_1_2.Run()
    check_1_1_2.Print()

