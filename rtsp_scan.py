paths = [
    "/live",
    "/stream1",
    "/stream2",
    "/stream",
    "/test",
    "/h264",
    "/h264/ch1/main/av_stream",
    "/h264/ch1/sub/av_stream",
    "/media",
    "/media/video1",
    "/media/video2",
    "/videoMain",
    "/videoSub",

    "/Streaming/Channels/101",
    "/Streaming/Channels/102",
    "/Streaming/Channels/201",
    "/Streaming/Channels/202",
    "/Streaming/Channels/301",

    "/ISAPI/Streaming/channels/101",
    "/ISAPI/Streaming/channels/102",

    "/cam/realmonitor?channel=1&subtype=0",
    "/cam/realmonitor?channel=1&subtype=1",

    "/trackID=1",
    "/trackID=2",

    "/live/main",
    "/live/sub",

    "/onvif1",
    "/onvif2",
    "/onvif/device_service",

    "/axis-media/media.amp",
    "/mpeg4",
    "/mjpeg"
]

import socket

ip = "<IP_ADDRESS>"
port = <PORT>

for p in paths:
    req = f"DESCRIBE rtsp://{ip}{p} RTSP/1.0\r\nCSeq: 1\r\n\r\n"

    s = socket.socket()
    s.settimeout(2)

    try:
        s.connect((ip, port))
        s.send(req.encode())
        res = s.recv(1024).decode(errors="ignore")

        print(f"[{p}] -> {res.splitlines()[0]}")

    except:
        pass

    finally:
        s.close()
