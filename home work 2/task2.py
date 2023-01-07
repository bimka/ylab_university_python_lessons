# https://university.ylab.site/python/lecture-2-hw/

"""
Задача №2.
Вам дан class Movie. Реализуйте у него метод scheldule. Он будет 
генерировать дни, в которые показывают фильм.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        days = []
        num_of_intervals = len(self.dates)
        for interval in range(num_of_intervals):
            start_of_period = self.dates[interval][0]
            end_of_period = self.dates[interval][1]
            num_of_days = (end_of_period - start_of_period).days + 1
            for i in range(num_of_days):
                current_day = start_of_period + timedelta(i)
                days.append(current_day)
        return days


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)