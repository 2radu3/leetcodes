class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                el = (i == 0 or flowerbed[i - 1] == 0)
                er = (i == length - 1 or flowerbed[i + 1] == 0)

                if el and er:
                    flowerbed[i] = 1
                    n -= 1

        return n <= 0
              