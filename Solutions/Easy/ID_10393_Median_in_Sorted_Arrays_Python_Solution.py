#Python Solution
import statistics
def find_median_sorted_arrays(input):
    """ 
    :type input: Dict[str, List[int]]
    :rtype: float
    """

    nums1 = input["nums1"]
    nums2 = input["nums2"]
    
    return statistics.median(nums1 + nums2)
