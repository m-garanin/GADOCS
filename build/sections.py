
def add(lst, pname, products):
    pname = pname.lower()
    lst.append(pname)
    G_POST_GROUP[pname] = lst
    G_POST_PRODUCTS[pname] = products.split(',')
    
SRT = []
SRT_BLOG = []

RTMP = []
RTMP_BLOG = []
SUPP = []

GROUPS = [('SRT Section', SRT),
          ('RTMP Section', RTMP),
          ('Other',SUPP)]

G_POST_GROUP = {} # {post: group}
G_POST_PRODUCTS = {} # {post: products }


srt_all = 'SRT MiniServer, SRT Streamer, RemoteExpert'
srt_server = 'SRT MiniServer'

rtmp_all = 'RTMP MiniServer'
rtmp_server = 'RTMP MiniServer'

# SRT
add(SRT, 'srt-cross-line', srt_all)
add(SRT, 'srt-custom-proxy', srt_server)
add(SRT, 'srt-direct-connection', srt_server)
add(SRT, 'srt-trial-info', srt_server)
add(SRT, 'srt-set-proxy-addon', srt_server)

# SRT-BLOG
add(SRT_BLOG, 'SRT-Cross-Line-Feature', srt_all)
add(SRT_BLOG, 'SRT-Short-review', srt_all)



# RTMP
add(RTMP, 'rtmp-About-Start-and-Max-delay', rtmp_server)
add(RTMP, 'rtmp-Custom-proxy-server', rtmp_server)
add(RTMP, 'rtmp-Direct-connection-easy-way-for-check', rtmp_server)
add(RTMP, 'rtmp-Direct-connection-from-internet', rtmp_server)
add(RTMP, 'rtmp-How-to-connect-Mevo', rtmp_server)
add(RTMP, 'rtmp-How-to-use-GoPro7', rtmp_server)
add(RTMP, 'rtmp-Proxy-Addon', rtmp_server)
add(RTMP, 'rtmp-Remote-control', rtmp_server)
add(RTMP, 'rtmp-Trial-info', rtmp_server)
add(RTMP, 'rtmp-Video-&-audio-issues', rtmp_server)
add(RTMP, 'rtmp-VidiU-Teradek-connection-issue', rtmp_server)
add(RTMP, 'rtmp-Windows-WiFi-issue', rtmp_server)

add(RTMP, 'rtmp-step-by-step', rtmp_server)
add(RTMP, 'rtmp-user-interface-guide', rtmp_server)

# RTMP-BLOG
add(RTMP_BLOG, 'Cases-of-using-RTMPMiniServer', rtmp_server)
add(RTMP_BLOG, 'How-RTMPMiniServer-differs-from-other-servers', rtmp_server)
add(RTMP_BLOG, 'LifeHacks-for-streamers', 'NTRStreamer')
add(RTMP_BLOG, 'Proxy-add-on-for-RTMPMiniServer', rtmp_server)



# SUPPORT
add(SUPP, 'support-How-to-make-dump-of-stream-for-support', 'SRT MiniServer, RTMP MiniServer')


# add(RTMP, '')


