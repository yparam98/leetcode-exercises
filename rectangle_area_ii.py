#!/usr/bin/python3
from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        total_area: int = 0

        for rectangle in rectangles:
            base: int = rectangle[2]-rectangle[0]
            height: int = rectangle[3]-rectangle[1]
            area: int = base*height
        
            print('base: {0}, height: {1}, area: {2}'.format(base, height, area))
            
            total_area += area
            
        return total_area

def main():
    solution = Solution()
    rectangles: List[int] = []
    num_rects: int = int(input('how many rectangles? '))
    for i in range(num_rects):
        rectangle: List[int] = []
        for val in input('x1 y1 x2 y2: ').split(' '):
            rectangle.append(int(val))
        rectangles.append(rectangle)
    print(solution.rectangleArea(rectangles))

main()
