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

width = blt.params['width']
height = blt.params['height']
dwell_time = blt.params['dwell_time']
doc = session.FIB.Scan.AcquireImage("SE", Bpp.Grayscale_16_bit, width, height, dwell_time)

img16 = np.asarray(doc.Image)

path = os.path.expanduser("~/balthazar/fib_16bit.png")
plt.imsave(path, img16, cmap="gray", vmin=0, vmax=65535)
print("Saved to:", path)

plt.figure(figsize=(w/100, h/100), dpi=100)
plt.imshow(img16, cmap="gray", vmin=0, vmax=65535)
plt.axis("off")
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.show()

