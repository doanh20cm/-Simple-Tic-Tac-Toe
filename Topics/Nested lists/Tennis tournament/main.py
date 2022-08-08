result = [_[0] for _ in [input().split() for _ in range(int(input()))] if _[1] == 'win']
print(f"{result}\n{len(result)}")