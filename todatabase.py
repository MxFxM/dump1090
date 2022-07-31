import sys
import time

import influxdb_client
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
write_api = client.write_api(write_options=SYNCHRONOUS)

# receive from stdin (piped input)
for line in sys.stdin:

    # split on whitespace
    pieces = line.split()

    # the line between the header and the data has no spaces, ignore it
    if len(pieces) < 2:
        continue

    # header has a . at the end
    if pieces[-1] == '.':
        continue

    flight = {}
    stringoutput = ""
    p = None

    # depending on length of the input, we have a flight number or not
    if len(pieces) == 9: # no flight number
        flight["id"] = pieces[0]
        flight["altitude"] = float(pieces[1])
        flight["speed"] = float(pieces[2])
        flight["lat"] = float(pieces[3])
        flight["lon"] = float(pieces[4])
        flight["track"] = float(pieces[5])
        flight["messages"] = int(pieces[6])
        flight["seen"] = int(pieces[7])
        stringoutput = f"flightdata,id={flight['id']} altitude={flight['altitude']} speed={flight['speed']} lat={flight['lat']} lon={flight['lon']} track={flight['track']} messages={flight['messages']} seen={flight['seen']}"
        p = influxdb_client.Point("flightdata").tag("device", "rtlsdr").field("id", flight["id"]).field("lat", flight["lat"]).field("lon", flight["lon"])

    elif len(pieces) == 10: #with flight number
        flight["id"] = pieces[0]
        flight["flight"] = pieces[1]
        flight["altitude"] = float(pieces[2])
        flight["speed"] = float(pieces[3])
        flight["lat"] = float(pieces[4])
        flight["lon"] = float(pieces[5])
        flight["track"] = float(pieces[6])
        flight["messages"] = int(pieces[7])
        flight["seen"] = int(pieces[8])
        stringoutput = f"flightdata,id={flight['id']} flight={flight['flight']} altitude={flight['altitude']} speed={flight['speed']} lat={flight['lat']} lon={flight['lon']} track={flight['track']} messages={flight['messages']} seen={flight['seen']}"
        p = influxdb_client.Point("flightdata").tag("device", "rtlsdr").field("id", flight["id"]).field("lat", flight["lat"]).field("lon", flight["lon"])

    else:
        # skip errors
        continue

    #print(f"{flight}")
    print(stringoutput)

    #write_api.write("test_bucket", "mxfxm", [stringoutput])
    write_api.write(bucket="test_bucket", org="mxfxm", record=p)
    break
