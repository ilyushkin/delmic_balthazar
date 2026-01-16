import balthazar as blt
from tescanautomation import Automation
from tescanautomation.Common import Bpp
import numpy as np
import matplotlib.pyplot as plt


microscope_ip = blt.params['ip_address']

session = Automation(microscope_ip)  # default port 8300
session.FIB.Detector.Set(0, 'SE')

w, h, dwell = 512, 512, 1000
doc = session.FIB.Scan.AcquireImage("SE", Bpp.Grayscale_16_bit, w, h, dwell)

doc.Image.show()
