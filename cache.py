import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def is_rate_limited(ip: str):
    """Check if an IP has exceeded request limits."""
    requests = redis_client.incr(ip)
    if requests == 1:
        redis_client.expire(ip, 60)  # 1-minute window
    return requests > 10
