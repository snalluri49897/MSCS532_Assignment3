class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _load_factor(self):
        return self.size / self.capacity

    def _resize(self):
        old_table = self.table

        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for head in old_table:
            current = head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        if self._load_factor() > 0.75:
            self._resize()

        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        previous = None

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next

                self.size -= 1
                return True

            previous = current
            current = current.next

        return False

    def display(self):
        for i in range(self.capacity):
            current = self.table[i]
            chain = []

            while current:
                chain.append(f"({current.key}:{current.value})")
                current = current.next

            print(f"{i}: {' -> '.join(chain)}")


if __name__ == "__main__":
    ht = HashTable()

    ht.insert("Alice", 100)
    ht.insert("Bob", 200)
    ht.insert("Charlie", 300)

    print("Search Bob:", ht.search("Bob"))

    ht.delete("Bob")

    print("Search Bob after deletion:", ht.search("Bob"))

    print("\nHash Table Contents:")
    ht.display()