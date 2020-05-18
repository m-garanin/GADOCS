![image](q1.png)

   **Step by Step**
===
It’s basic “how-to” when hosts in same local network.

So I would like build this workflow:
![](q2.png)

I used name “Server” PC and “Encoder” PC for my hosts.
##
   **“Server” PC**

**STEP 1**: Download [(link)](http://garaninapps.com/rtmpminiserver#downloads) and install the RTMPMiniServer. RUN IT.

![](q3.png)

**STEP 2**: press START

*Note: if you got error message “Port 1935 not available” then change port in Settings*

![](q4.png)

“yellow” icon means “wait” state (nobody connects to our server yet)

**STEP 3**: open Preview window

![](q5.png)
##
  **“Encoder” PC**

**STEP 4**: Open any RTMP-encoder. I use OBS on macOS: go to Settings —> Stream: select Custom service and type server and stream key.

![](q6.png)

**STEP 5**: press Start Streaming and your encoder starts send RTMP feed to RTMPMiniServer. So let’s go to “Server” PC for check result.

##

  **“Server” PC (check result)**

On “Server” PC I got this result:

![](q7.png)

  **Connect to NDI Workflow**

RTMPMiniServer converts incoming RTMP feed to NDI.
So just open any NDI software (vMix, OBS, Wirecast etc) and select NDI source called “MiniServer A- Line 1”.
For example I use “NDI Studio Monitor” from NewTek tools:

![](q8.png)

select “MiniServer A- Line 1”

![](q9.png)
