class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums1)):
            print(f"i={i}")
            for j in range(len(nums2)):
                print(j)
                if nums1[i]==nums2[j]:
                    if len(nums2)-1>=j+1:
                        if nums2[j+1]>nums2[j]:
                            r.append(nums2[j+1])
                            break
                        else:
                            cut=nums2[j+1:]
                            for p in cut:
                                if nums2[j]<p:
                                    r.append(p)
                                    break

                            if nums2[j]>p:
                                r.append(-1)
                            

                    else:
                        r.append(-1)

        return r


                



                

                

        