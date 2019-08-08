class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        total = (C-A)*(D-B) + (G-E)*(H-F)
        overlap_x = max(min(C,G)-max(A,E),0)
        overlap_y = max(min(D,H)-max(B,F),0)
        return total - overlap_x*overlap_y