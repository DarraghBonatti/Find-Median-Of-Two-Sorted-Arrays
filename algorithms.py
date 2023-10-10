class Solutions:
    def findMedianSortedArrays(self, nums1, nums2):
            
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
            list = []
            i = 0
            j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    list.append(nums1[i])
                    i += 1
                else:
                    list.append(nums2[j])
                    j +=1
            
            while i < len(nums1):
                list.append(nums1[i])
                i += 1

            while j < len(nums2):
                list.append(nums2[j])
                j +=1

            count = len(list)
            if count % 2 == 0:
                x = count // 2
                median = (list[x] + list[x-1]) / 2

            else:
                median = list[len(list)//2]
            
            return median
nums1 =[1,2]
nums2 = [3,4]
S = Solutions()
print(S.findMedianSortedArrays(nums1,nums2))