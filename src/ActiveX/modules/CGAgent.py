# Chinagames iGame CGAgent ActiveX Control Buffer Overflow
# CVE-2009-1800

import logging 
log = logging.getLogger("Thug.ActiveX")

def CreateChinagames(self, arg0):
    if len(arg0) > 428:
        log.warning('CGAgent ActiveX CreateChinagames Method Buffer Overflow')

