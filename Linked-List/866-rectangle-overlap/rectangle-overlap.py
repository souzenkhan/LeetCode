class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        if(rec1[0] == rec1[2] or 
            rec1[1] == rec1[3] or 
            rec2[0] == rec2[2] or
            rec2[1] == rec2[3]):
            return False
        #x1 y1 x2 y2
        #0.  1. 2  3
        return not(rec1[2] <= rec2[0] or #left
                    rec1[3] <= rec2[1] or #top
                    rec1[0] >= rec2[2] or #right
                    rec1[1] >= rec2[3])