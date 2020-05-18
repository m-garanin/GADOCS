
def add(lst, inf):
    lst.append(inf)
    
SRT = []
RTMP = []
SUPP = []

GROUPS = [('SRT Section', SRT),
          ('RTMP Section', RTMP),
          ('Other',SUPP)]

# SRT
add(SRT, 'srt-cross-line')
add(SRT, 'srt-custom-proxy')
add(SRT, 'srt-direct-connection')
add(SRT, 'srt-trial-info')

# RTMP
add(RTMP, 'rtmp-About-Start-and-Max-delay')
add(RTMP, 'rtmp-Custom-proxy-server')
add(RTMP, 'rtmp-Direct-connection-easy-way-for-check')
add(RTMP, 'rtmp-Direct-connection-from-internet')
add(RTMP, 'rtmp-How-to-connect-Mevo')
add(RTMP, 'rtmp-How-to-use-GoPro7')
add(RTMP, 'rtmp-Proxy-Addon')
add(RTMP, 'rtmp-Remote-control')
add(RTMP, 'rtmp-Trial-info')
add(RTMP, 'rtmp-Video-&-audio-issues')
add(RTMP, 'rtmp-VidiU-Teradek-connection-issue')
add(RTMP, 'rtmp-Windows-WiFi-issue')

add(RTMP, 'rtmp-set-proxy-addon')
add(RTMP, 'rtmp-step-by-step')
add(RTMP, 'rtmp-user-interface-guide')

# SUPPORT
add(SUPP, 'support-How-to-make-dump-of-stream-for-support')


# add(RTMP, '')


