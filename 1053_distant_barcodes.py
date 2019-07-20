class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        size = len(barcodes)
        i = 0
            
        for k, v in collections.Counter(barcodes).most_common():
            while v > 0:
                barcodes[i] = k
                v -= 1
                i += 2
                if i >= size: i = 1
        return barcodes