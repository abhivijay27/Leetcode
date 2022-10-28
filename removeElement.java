class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length == 0){
            return 0;
        }
        if(nums.length == 1){
            if(nums[0] == val){
                return 0;
            }
            else{
                return 1;
            }
        }
        int count = 0;
        for(int i = 0;i < nums.length;){
            if(nums[i] != val){
               nums[count] = nums[i];
               count++;
            }
            i++;
        }
        return count;
    }
}
