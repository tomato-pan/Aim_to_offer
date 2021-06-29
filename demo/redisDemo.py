import redis

conn = redis.Redis(host="127.0.0.1",port=6379)
conn.set("aa",1231)
val = conn.get("aa")
print(val)