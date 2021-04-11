#!/usr/bin/python3
import time,sys
from deluge_client import DelugeRPCClient

tID = sys.argv[1]
dHost = "127.0.0.1"
dPort = 58846
dUser = "localclient"
dPass = "40d0fa1bad181404a7ed3821d83aff7c7833970c"

client = DelugeRPCClient(dHost,dPort,dUser,dPass)
client.connect()
while client.connected == False:
        time.sleep(3)
        client = DelugeRPCClient(dHost,dPort,dUser,dPass)
        client.connect()

time.sleep(3)
tData = client.call('core.get_torrent_status',tID,{})
print(tData)
while tData[b'state'] == b'Downloading' or tData[b'state'] == b'Paused':
#         if len(tData[b'peers']) < 1:
        if len(tData[b'peers']) < 1 or len(tData[b'num_seeds']) == 0:
                client.call('core.pause_torrent',tID)
                time.sleep(3)
                client.call('core.resume_torrent',tID)
                time.sleep(2)
                client.call('core.force_reannounce',[tID])
                time.sleep(3)
                tData = client.call('core.get_torrent_status',tID,{})
        else:
                exit()
exit()
