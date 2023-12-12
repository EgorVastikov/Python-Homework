from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self._cache = OrderedDict()

    def get(self, key):
        if key not in self._cache:
            return None
        self._cache.move_to_end(key)
        return self._cache[key]

    @property
    def oldest(self):
        if self._cache:
            return next(reversed(self._cache.items()))
        return None

    @oldest.setter
    def oldest(self, new_elem):
        key, value = new_elem
        if key in self._cache:
            del self._cache[key]
        elif len(self._cache) >= self.capacity:
            self._cache.popitem(last=False)
        self._cache[key] = value

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self._cache.items():
            print(f"{key} : {value}")


cache = LRUCache(3)
cache.oldest = ("key1", "value1")
cache.oldest = ("key2", "value2")
cache.oldest = ("key3", "value3")
cache.print_cache()

print(cache.get("key2"))

cache.oldest = ("key4", "value4")
cache.print_cache()