from datetime import datetime as dt
import logging
from functools import reduce

logging.basicConfig(
    level=logging.DEBUG,
    filename="map.log"
)

nums = [x for x in range(1, 20)]
"""reduce"""
total = reduce(lambda a, b: a + b, nums)
print(total)

"""filter"""
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

"""map"""
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