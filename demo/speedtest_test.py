import speedtest as spt
from pprint import pprint


spd = spt.Speedtest()

download_speed = int(spd.download() /1024 /1024)
upload_speed = int(spd.upload() /1024 /1024)
# pprint(spd.get_servers())
# pprint(spd.get_best_server())
pprint(download_speed)
pprint(upload_speed)