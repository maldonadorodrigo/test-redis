import redis
import os
import time

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
 print(f" Testando redis em {REDIS_HOST}:{REDIS_PORT}")
while True:
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.ping()
        print(f" Conectado ao Redis em {REDIS_HOST}:{REDIS_PORT}")
    except redis.ConnectionError as e:
        print(f"❌ Falha na conexão: {e}")
    time.sleep(3)
