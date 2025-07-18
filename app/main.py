from typing import Any


class Dictionary:
    def __init__(self, capacity: int = 8,
                 load_factor_threshold: float = 0.7) -> None:
        self.capacity = capacity
        self.load_factor_threshold = load_factor_threshold
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_key = hash(key)
        if self.size / len(self.table) > self.load_factor_threshold:
            self.resize()
        index = hash_key % len(self.table)
        for i, element in enumerate(self.table[index]):
            if element[0] == key:
                self.table[index][i] = (key, value, hash_key)
                break
        else:
            self.table[index].append((key, value, hash_key))
            self.size += 1

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % len(self.table)
        for element in self.table[index]:
            if element[0] == key:
                return element[1]
        raise KeyError(key)

    def resize(self) -> None:
        new_capacity = len(self.table) * 2
        new_table = [[] for _ in range(new_capacity)]
        for package in self.table:
            for element in package:
                new_index = element[2] % new_capacity
                new_table[new_index].append(element)
        self.table = new_table
        self.capacity = new_capacity

    def __delitem__(self, key: Any) -> None:
        index = hash(key) % len(self.table)
        for i, element in enumerate(self.table[index]):
            if element[0] == key:
                del self.table[index][i]
                self.size -= 1
                break
        else:
            raise KeyError(key)

    def clear(self) -> None:
        self.table = [[] for _ in range(len(self.table))]
        self.size = 0
