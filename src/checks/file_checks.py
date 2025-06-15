#!/bin/env python3

import os
from .check import Check
from helper import PrintInfo

class FilePermissionCheck(Check):
    _file: str
    _max_allowed: int

    def __init__(
            self,
            *args,
            file: str="",
            max_allowed:int=0o644,
            **kwargs
            ):
        super().__init__(*args, **kwargs)
        self._file = file
        self._max_allowed = max_allowed
    
    def Run(self):
        if self._executed:
            return

        if not os.path.exists(self._file):
            self._executed = False
            self._pass = False
            PrintInfo(severity="info", message=self._title)
            PrintInfo(severity="info", message="     * File not found")
            return

        file_mode = os.stat(self._file).st_mode & 0o777
        if file_mode <= self._max_allowed:
            self._pass = True
        else:
            self._pass = False
        self._executed = True


class FileOwnershipCheck(Check):
    _file: str
    _required_uid: str
    _required_gid: str

    def __init__(
            self,
            *args,
            file: str="",
            required_uid: int = 0,
            required_gid: int = 0,
            **kwargs
            ):
        super().__init__(*args, **kwargs)
        self._file = file
        self._required_uid = required_uid
        self._required_gid = required_gid
    
    def Run(self):
        if self._executed:
            return

        if not os.path.exists(self._file):
            self._executed = False
            self._pass = False
            PrintInfo(severity="info", message=self._title)
            PrintInfo(severity="info", message="     * File not found")
            return

        stat_info = os.stat(self._file)
        if stat_info.st_uid == self._required_uid and stat_info.st_gid == self._required_gid:
            self._pass = True
        else:
            self._pass = False
        self._executed = True
