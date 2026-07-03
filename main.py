from philh_myftp_biz.time import now
from philh_myftp_biz.pc import Path
from philh_myftp_biz.web import IP
from philh_myftp_biz import gps
from time import sleep
from ping3 import ping

records = Path(f'records-{now().unix}.json').JSON.List
records.save([])

while True:
    
    pos = gps.fetch()

    record = {
        'coords': pos,
        'dist': None,
        'ping': ping(IP.ROUTER) or -1
    }

    frecord: dict = records[-1] if records.read() else record
    record['dist'] = (pos - frecord['coords']).meters

    print(record)
    
    if record not in records.read():
        records += record

    sleep(1)
