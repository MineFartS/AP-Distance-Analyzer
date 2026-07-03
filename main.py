from time import sleep
from philh_myftp_biz.pc import Path
from philh_myftp_biz.time import now
from philh_myftp_biz import gps

records = Path(f'records-{now().unix}.json').JSON.List
records.save([])

while True:
    
    pos = gps.fetch()

    record = {
        'coords': pos,
        'ping': -1
    }

    frecord: dict = records[-1] if records.read() else record
    record['dist'] = (pos - frecord['coords']).meters

    print(record)
    
    if record not in records.read():
        records += record

    sleep(1)
