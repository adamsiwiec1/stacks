import pyshark

capture = pyshark.LiveCapture(interface='eth0')
capture.sniff(timeout=10,packet_count=10)

while True:
    for packet in capture.sniff_continuously(packet_count=5):
        print('Just arrived:', packet)