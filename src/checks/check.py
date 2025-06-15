#!/bin/env python3

from helper import PrintInfo

class Check:
    _pass: bool
    _executed: bool

    _title: str
    _automated: bool
    _scored: bool
    _level: int
    
    def __init__(
            self,
            title: str,
            automated: bool=None,
            scored: bool=None,
            level: int=None,
        ):
        self._executed = False
        self._pass = False

        self._title = title
        self._automated = automated
        self._scored = scored
        self._level = level
    
    def Run(self):
        if self._executed:
            return

        self._executed = True
        self._pass = True

    def Print(self):
        if not self._executed:
           return
        
        if self._pass:
            PrintInfo("pass", self._title, level=self._level, automated=self._automated, scored=self._scored)
        else:
            PrintInfo("warn", self._title, level=self._level, automated=self._automated, scored=self._scored)

def RunChecks(*checks: Check):
    for check in checks:
        if not isinstance(check, Check):
            raise TypeError(f"Expected Check instance, got {type(check).__name__}")
        check.Run()
        check.Print()
