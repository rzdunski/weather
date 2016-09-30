import os
import gettemp
import time

id_inside = '28-000001cbe681'
id_outside = '10-000800ba9da0'
temp_in = str(gettemp.gettemp(id_inside))
temp_out = str(gettemp.gettemp(id_outside))
os.chdir('/home/pi/')
filename = time.strftime('%d%m%y_'+ temp_in + '_' + temp_out)
temp_data=open(filename, 'w')
temp_data.write('/n')
temp_data.close() 

