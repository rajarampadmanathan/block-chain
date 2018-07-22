import redis
import re

idle_max = 300

r = redis.StrictRedis(host="npe-rbl-ems-redis.kx1tl9.clustercfg.usw2.cache.amazonaws.com", port=6379, password='41a96714-7639-43c6-9bf2-d55644fda262', ssl=True)
print (r)
print ("Kill -1")
cl = r.exists("hello")
print ("Kill -2")
cl = r.execute_command("client", "list")
print ("Kill -3")
pattern = r"addr=(.*?) .*? idle=(\d*)"
regex = re.compile(pattern)
for match in regex.finditer(cl):
    if int(match.group(2)) > idle_max:
        r.client_kill(match.group(1))
        print ("Kill " + match.group(1))
r.save();