#
# The purupose of this code is to get a timeseriese of microwave readings into a csv file.

import time
from pyHS100 import SmartPlug
import sys

# ****************************************************************************************************


def main():
    microwave_ON = False
    # Connect to microwave.
    # Create a filename based on datetime and what we're capturing.
    #now = datetime.now()
    #datetimestr = now.strftime("%m-%d-%H:%M:%S")
    filename = '../../data/us/microwave.csv'
    # # Create an instance of the plug (use Discover to figure out IP)
    plug = SmartPlug("192.168.86.200")
    n = 0
    max_current_off = 0.0
    m_current_off = 0.0
    times_above_current = 2.5
    string_id = 'off'
    i = 0.0
    p = 0.0

    # Append this reading to the microwave csv file.
    with open(filename, 'a+') as f:
        while True:
            # Take reading
            try:
                measurements = plug.get_emeter_realtime()
                p = measurements['power']
                i = measurements['current']
            except:
                print(print("Reading error:", sys.exc_info()[0]))
            # The microsoft is currently not microwaving something...
            if (microwave_ON == False):
                # If the current is significantly larger than the previous reading, we say the
                # microwave is on.
                max_current_off = times_above_current * \
                    m_current_off if m_current_off > 0.0 else times_above_current*i
                if (i > max_current_off):
                    microwave_ON = True
                    print(
                        'microwave is on.  p: {}  i: {} m_current_off: {} max_current_off: {}'.format(p, i, m_current_off, max_current_off))
                # Calculate rolling mean when microwave is off.
                else:
                    string_id = 'off'
                    n = n + 1
                    m_current_off = m_current_off + \
                        (i - m_current_off) / n
            # This reading has the current drawing far less power than the previous reading.
            # We say because of this the microwave is no longer microwaving something.
            elif (microwave_ON == True and i < max_current_off):
                microwave_ON = False
                print('Microwave is Off....i: {} is  < than max: {}'.format(
                    i, max_current_off))
            string_id = 'on' if microwave_ON == True else 'off'
            rowStr = '{},{},{},{}\n'.format(time.time(), p, i, string_id)
            print(rowStr)
            f.write(rowStr)
            f.flush()
            # Wait a sec between readings.
            time.sleep(1)
# *************************************************************************************************


if __name__ == '__main__':
    main()
