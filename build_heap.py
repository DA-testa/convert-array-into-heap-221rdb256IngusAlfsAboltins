def heapify(data, i, n, swaps):
    min_idx = i
    left_child_idx = 2 * i + 1
    right_child_idx = 2 * i + 2

    if left_child_idx < n and data[left_child_idx] < data[min_idx]:
        min_idx = left_child_idx

    if right_child_idx < n and data[right_child_idx] < data[min_idx]:
        min_idx = right_child_idx

    if i != min_idx:
        swaps.append((i, min_idx))
        data[i], data[min_idx] = data[min_idx], data[i]
        heapify(data, min_idx, n, swaps)


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        heapify(data, i, n, swaps)
    return swaps


def main():
    text = input()
    if text[0] == "I" :
         n = input();
         data = list(map(int,input().split))
         assert len(data) == int(n)
         swaps = build_heap(data)
         print(len(swaps))
         for i, j in swaps:
            print(i, j)
 
    
    
    
if __name__ == "__main__":
    main()
