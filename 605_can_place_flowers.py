from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if i - 1 >= 0 and flowerbed[i - 1] == 1:  # 如果前一個位置存在，且該位置有種花，那此位置不能種花
                continue
            if (
                i + 1 < len(flowerbed) and flowerbed[i + 1] == 1
            ):  # 如果後一個位置存在，且該位置有種花，那此位置不能種花
                continue
            if flowerbed[i] == 0:  # 前後都沒有種花
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flowerbed = [0] + flowerbed + [0]
        zero_count = 0
        counter = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                zero_count += 1
            elif flowerbed[i] == 1:
                counter += (zero_count - 1) // 2
                zero_count = 0
        
        counter += (zero_count - 1) // 2
        return True if counter - n >= 0 else False