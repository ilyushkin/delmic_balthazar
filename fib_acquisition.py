import balthazar as blt
import sys, os
from tescanautomation import Automation, GUI
from tescanautomation.Common import Bpp
import numpy as np
import matplotlib.pyplot as plt

app = GUI.Application(sys.argv)

microscope_ip = blt.params['ip_address']

session = Automation(microscope_ip)  # default port 8300
session.FIB.Detector.Set(0, 'SE')

w, h, dwell = 512, 512, 1000
doc = session.FIB.Scan.AcquireImage("SE", Bpp.Grayscale_16_bit, w, h, dwell)

img16 = np.asarray(doc.Image)

plt.imsave("fib_16bit.png", img16, cmap="gray", vmin=0, vmax=65535)

plt.imshow(img16, cmap="gray", vmin=0, vmax=65535)
plt.axis("off")
plt.show()
