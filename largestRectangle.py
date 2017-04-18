N = int(input())
height = [int(x) for x in input().split()]

def largestRectangleArea(height):
    subStack, area, i = [], 0, 0
    while i <= len(height):
        if not subStack or (i < len(height) and height[i] > height[subStack[-1]]):
            subStack.append(i)
            i += 1
        else:
            last = subStack.pop()
            if not subStack:
                area = max(area, height[last] * i)
            else:
                area = max(area, height[last] * (i - subStack[-1] - 1))
    return area


if __name__ == "__main__":
    print(largestRectangleArea(height))
