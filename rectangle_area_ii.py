#!/usr/bin/python3
from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # total_area = 0

        # for rectangle in rectangles:
        #     print(total_area)
        #     total_area += rectangle[0]*rectangle[1]*rectangle[2]*rectangle[3]

        # return total_area
        return rectangles

def main():
    solution = Solution()
    rectangles: List[int] = []
    for i in range(4):
        rectangle: List[int] = []
        for val in input('enter 4 coords: ').split(' '):
            rectangle.append(int(val))
        rectangles.append(rectangle)
    print(solution.rectangleArea(rectangles))

main()
