import re
from typing import Callable
def generator_numbers(text):
    pattern = r' \d+\.\d+ | \d+ '
    for match in re.findall(pattern,text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    return sum(func(text))


