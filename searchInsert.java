class Solution {
    public int searchInsert(int[] nums, int target) {
        int i = 0,j = nums.length - 1,output = 0,mid;
        int count = (nums.length)/2;
        while(count>=0){
            mid = (i+j)/2;
            if(nums[mid] == target){
                return mid;
            }
            else if(nums[mid]<target){
                //System.out.println("In i mid"+nums[mid]);
                i = mid;
            }
            else{
                //System.out.println("In j mid"+nums[mid]);
                j = mid;
            }
            //mid = (i+j)/2;
            //System.out.println(mid);
            count--;
            if(i == j)
                break;
            }
        //(num1>num2) ? (num1+num2):(num1-num2)
        if(nums[j]<target){
            return j+1;
        }
        else if(nums[j]>target && nums[i]>target){
            return i;
        }
         return j;
        } 
    }
