from typing import Iterable, Iterator, Any


class Unique:
    def __init__(self, iterable: Iterable, ignore_case: bool = False, **kwargs):
        self.iterable = iterable
        self.ignore_case = ignore_case

    def __iter__(self) -> Iterator[Any]:
        seen = set()
        for item in self.iterable:
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in seen:
                seen.add(key)
                yield item
