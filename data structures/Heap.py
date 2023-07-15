import math


class MinHeap:
    def __init__(self):
        self.array = [dict]  # index elements at 1
        self._OFFSET = len(self.array)

    @property
    def size(self):
        return len(self.array) - self._OFFSET

    def append(self, item, priority: int):
        item = {"item": item, "priority": priority}
        self.array.append(item)
        self._heapify_up(len(self.array) - 1)

    def _heapify_up(self, index: int):
        if self._parent_index(index) == 0:
            return  # root added to heap

        if self.get_parent(index)["priority"] > self.array[index]["priority"]:
            # Swap values of parent and child elements
            self._swap_elements(index, self._parent_index(index))
            self._heapify_up(self._parent_index(index))

    def _swap_elements(self, i1: int, i2: int):
        self.array[i1], self.array[i2] = self.array[i2], self.array[i1]

    def poll(self):
        top = self.array[1].copy()
        # Swap values of first and last elements
        self._swap_elements(1, len(self.array) - 1)
        self.array.pop(len(self.array) - 1)

        self._heapify_down(1)
        return top["item"]

    def _heapify_down(self, index: int):
        if self._is_leaf(index):
            return # Make sure left index is not empty before swapping down
        elif self.array[index]["priority"] > self.get_left_child(index)["priority"]:
            self._swap_elements(index, self._left_index(index))
            self._heapify_down(self._left_index(index))

        else:
            if not self._is_contained(self._right_index(index)):
                return # Make sure right index is not empty before swapping down
            elif self.array[index]["priority"] > self.get_right_child(index)["priority"]:
                self._swap_elements(index, self._right_index(index))
                self._heapify_down(self._right_index(index))

    def _is_leaf(self, index: int) -> bool:
        return not (self._is_contained(self._left_index(index))
                    or self._is_contained(self._right_index(index)))

    def _is_contained(self, index: int) -> bool:
        return index < len(self.array) - self._OFFSET

    @staticmethod
    def _parent_index(index: int) -> int:
        return math.floor(index / 2)

    @staticmethod
    def _left_index(index: int) -> int:
        return 2 * index

    @staticmethod
    def _right_index(index: int) -> int:
        return 2 * index + 1

    def get_parent(self, index: int):
        return self.array[self._parent_index(index)]

    def get_children(self, index: int):
        return [self.get_left_child(index), self.get_right_child(index)]

    def get_left_child(self, index: int):
        return self.array[2 * index]

    def get_right_child(self, index: int):
        return self.array[2 * index + 1]

    def print(self):
        i = 0
        lower_bound = 0
        upper_bound = 1

        while upper_bound <= (len(self.array) + 2 ** i):
            # Recalculate upper bound if last row is not full
            if len(self.array) - self._OFFSET < upper_bound:
                upper_bound = len(self.array) - self._OFFSET

            for j in range(lower_bound + self._OFFSET, upper_bound + self._OFFSET):
                print(self.array[j]["priority"], end=" ")
            print()

            i += 1
            lower_bound = 2 ** i - 1
            upper_bound = 2 ** (i + 1) - 1


heap = MinHeap()
heap.append("d", 5)
heap.append("e", 4)
heap.append("a", 3)
heap.append("c", 2)
heap.append("b", 1)

heap.print()
heap.poll()
heap.print()
heap.poll()
heap.poll()
heap.poll()
heap.poll()


