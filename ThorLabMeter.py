__author__ = 'HansDaniel'

import visa
from ThorlabsPM100 import ThorlabsPM100

def setUp(deviceName):
    rm = visa.ResourceManager()
    inst = rm.open_resource(deviceName, timeout=1)
    return ThorlabsPM100(inst=inst)
