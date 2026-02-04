if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    frist_runner = arr[0]
    for runner in arr[1:]:
        if frist_runner != runner:
            print(runner)
            break
            
