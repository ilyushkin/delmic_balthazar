import balthazar as blt
from tescanautomation import Automation


microscope_ip = blt.params['ip_address']

session = Automation(microscope_ip)  # default port 8300
session.FIB.Detector.Set(0, 'SE')
session.FIB.Detector.AutoSignal(0)
status = session.FIB.Beam.GetStatus()
if status != Automation.FIB.Beam.Status.On:
    session.FIB.Beam.On()
    # Wait for beam transition
    while session.FIB.Beam.GetStatus() == Automation.FIB.Beam.Status.OnOffInProgress:
        time.sleep(0.1)
print('Original Current:', session.FIB.Beam.GetCurrent(), ' pA')
print('Original Voltage:', session.FIB.Beam.GetVoltage(), ' V')
session.FIB.Beam.SetCurrent(10)
session.FIB.Beam.SetVoltage(30000)
print('New Current:', session.FIB.Beam.GetCurrent(), ' pA')
print('New Voltage:', session.FIB.Beam.GetVoltage(), ' V')