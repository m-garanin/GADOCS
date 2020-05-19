 **SRT Proxy Addon**
============
 SRT ProxyAddon is easy way for accept signal in Studio from Location.
It does not require dedicated IP and port-forwarding manipulation.
Just click and use.
![image](SRTProxyAddon-1.png)

1. Run SRT MiniServer and press START
2. Click ProxyAddon icon. It opens “SRT Proxy Addon” window.
3. Press “Connect” for get public address. Use this as SRT URL.

So for this image stream parameters for Line #4 is:

`Server URL: srt://amst.garaninapps.com:20396`

`Stream ID: streamkey4WQS`

NOTES: SRT ProxyAddon is easy way, but usage of dedicated IP is still preferred way for big studio and heavy traffic.

FAQ

**What is cons and pros of usage proxy addon?**

*Cons – you don’t need dedicated IP and port-forwarding setup. It’s perfect for using for mobile studios.
Pros – this workflow has 3 participants: Publisher–> Proxy-server –> Studio
instead 2 participants for direct connection (Publisher–>Studio)*
![image](Proxy.png)

**Where are located proxy servers?**

Now we are providing few public proxy nodes in Europe.

**Can I deploy my proxy server?** (SOON)

Yes, you can deploy proxy node on your server and it’s very easy.
For example you can rent VPS from DigitalOcean or Scaleway or AWS and deploy proxy node. Many cloud providers allow hour-rate so you can turn on server only for event. See this [guide](http://help.garaninapps.com/2019/09/09/custom-proxy-server/).

**Our Studio in USA has dedicated IP and we happy with SRT MiniServer. What is advantage of proxy addon we can get?**

You can get advantage if your publisher in other country. Proxy node allows solve the “first mile” issue. More detailed explanation see [here](https://medium.com/garaninapps/proxy-add-on-for-rtmpminiserver-85a23edaffce).
