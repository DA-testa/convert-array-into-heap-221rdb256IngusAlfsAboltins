def heapify(data, i, n, swaps):
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child

    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        heapify(data, min_index, n, swaps)
def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        heapify(data, i, n, swaps)
    return swaps
def main():
    first_input = input().strip()
    if first_input == 'I':
        
        
        
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif first_input == 'F':
        file_name = input().strip()
        file_path = os.path.join('tests', file_name)
        with open(file_path, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
    else:
        return
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
        
        
if __name__ == "__main__":
    main()
