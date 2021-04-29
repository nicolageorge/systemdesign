import random

class Heap:
    def __init__(self):
        self.inner_list = []
        self.mhup = 0
        self.mhdown = 0


    def _from_list(self, unsorted_list: list) -> None:
        self.inner_list = unsorted_list

        for i in range( int(len(self.inner_list)/2) + 1, -1, -1):
            self._max_heapify_down(element_index=i)


    def _max_heapify_down(self, element_index: int) -> None:
        self.mhdown += 1
        left = 2 * element_index
        right = 2 * element_index + 1

        largest = element_index
        if left < len(self.inner_list) and self.inner_list[left] > self.inner_list[element_index]:
            largest = left
        if right < len(self.inner_list) and self.inner_list[right] > self.inner_list[largest]:
            largest = right

        if largest != element_index:
            self.inner_list[largest], self.inner_list[element_index] = self.inner_list[element_index], self.inner_list[largest]
            self._max_heapify_down(element_index = largest)


    def _max_heapify_up(self, e_index: int) -> None:
        self.mhup += 1
        parent_index = int(e_index/2)

        if self.inner_list[parent_index] < self.inner_list[e_index]:
            self.inner_list[parent_index], self.inner_list[e_index] = self.inner_list[e_index], self.inner_list[parent_index]
            self._max_heapify_up(parent_index)


    def insert(self, value: int) -> None:
        next_index = len(self.inner_list)
        self.inner_list.append(value)
        self._max_heapify_up(next_index)


    def extract_max(self) -> int:
        self.inner_list[0], self.inner_list[-1] = self.inner_list[-1], self.inner_list[0]
        element = self.inner_list.pop()
        self._max_heapify_down(element_index=0)
        return element


    def __str__(self):
        list_text = ', '.join([str(x) for x in self.inner_list])
        return f"List elements: {list_text}"

    def __len__(self):
        return len(self.inner_list)


def main():
    hip = Heap()

    random_list = [i for i in range(100000000)]
    hip._from_list(unsorted_list=random_list)
    # print(hip)

    # import pdb
    # pdb.set_trace()

    # sorted_list = []
    # while len(hip):
    #     sorted_list.append(hip.extract_max())

    # print(sorted_list)

    # import pdb
    # pdb.set_trace()


if __name__ == '__main__':
    main()