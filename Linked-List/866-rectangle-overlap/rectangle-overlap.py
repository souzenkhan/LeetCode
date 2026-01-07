class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        overlap_left = max(rec1[0], rec2[0])
        overlap_right = min(rec1[2], rec2[2])
        overlap_top = min(rec1[3], rec2[3])
        overlap_bottom = max(rec1[1], rec2[1])

        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_top - overlap_bottom

        overlaps = False

        if(overlap_width > 0 and overlap_height > 0):
            overlap_area = overlap_width * overlap_height
            if overlap_area > 0: 
                overlaps = True 


        return overlaps