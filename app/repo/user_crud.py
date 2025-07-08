from datetime import datetime as dt
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="map.log"
)

nums = [x for x in range(20000)]

logging.info(f"start the for in {dt.now()}")
sq_nums = []
for i in nums:
    result = i**2
    sq_nums.append(result)
print(f"first for {sq_nums}")
logging.info(f"end the for in {dt.now()}")


logging.info(f"start the map in {dt.now()}")
squares = list(map(lambda x: x**2, nums))
print(f"this is map {squares}")
logging.info(f"end the map in {dt.now()}")