class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_table = defaultdict(int)
        for task in tasks:
            hash_table[task] += 1

        heap = []
        for letter in hash_table:
            count = hash_table[letter]
            heap.append([count, letter])
        
        # Ex) heap[0] = [4, 'A'] heap[2] = [3, 'D']
        heapq.heapify_max(heap)
        processed = deque()
        cool_down = defaultdict(int)
        time = 0

        while heap or processed:
            while processed:
                item = processed.pop()
                heapq.heappush_max(heap, item)

            while heap:
                if processed and cool_down[processed[-1][1]] == 0:
                    item = processed.pop()
                else:
                    item = heapq.heappop_max(heap)
                item[0] -= 1
                if cool_down[item[1]] > 0:
                    time += cool_down[item[1]]
                    for i in range(cool_down[item[1]]):
                        for key in cool_down:
                            if cool_down[key] > 0:
                                cool_down[key] -= 1
                time += 1
                if item[0] > 0:
                    processed.append(item)
                for key in cool_down:
                    if cool_down[key] > 0:
                        cool_down[key] -= 1

                cool_down[item[1]] += n
        
        return time

