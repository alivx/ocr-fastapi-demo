from redis import Redis
from rq import Queue
import time
q = Queue(connection=Redis(host='localhost', port=6379),is_async=True, default_timeout=3600, async_timeout=3600, result_ttl=3600)

from rq.decorators import job

@job('low', connection=Redis(host='localhost', port=6379), timeout=5)
def add(x, y):
    return x + y

jobs = add.delay(3, 4)
time.sleep(1)

xxx = job.fetch(id=jobs.id, connection=redis)
result = job.latest_result()  #  returns Result(id=uid, type=SUCCESSFUL)
if result == result.Type.SUCCESSFUL: 
    print(result.return_value) 
else: 
    print(result.exc_string)
