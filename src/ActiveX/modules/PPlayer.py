# Xunlei Thunder PPLAYER.DLL_1.WORK ActiveX Control

import logging
log = logging.getLogger("Thug.ActiveX")

def DownURL2(self, arg0, arg1, arg2, arg3):
    if len(arg0) > 1024:
        log.warning('Xunlei Thunder 5.x DownURL2 Overflow')

def SetFlvPlayerUrl(self, val):
    self.__dict__['FlvPlayerUrl'] = val

    if len(val) > 1060:
        log.warning('Xunlei Thunder XPPlayer Class FlvPlayerUrl Property Handling Buffer Overflow')

def SetLogo(self, val):
    self.__dict__['Logo'] = val

    if len(val) > 128:
        log.warning('PPStream (PowerPlayer.dll 2.0.1.3829) ActiveX Remote Overflow Exploit in Logo property')

