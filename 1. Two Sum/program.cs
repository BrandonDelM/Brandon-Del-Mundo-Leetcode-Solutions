public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int index1 = 0;
        int index2 = 0;
        while (index1 <= nums.Length){
            if (nums[index1] + nums[index2] == target && index1 != index2){
                break;
            }
            index2++;
            if (index2 == nums.Length){
                index1++;
                index2 = 0;
            }
        }
        int[] value = new int[2];
        value = [index1, index2];
        return value;
    }
}