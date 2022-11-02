class Solution {
    public int[] plusOne(int[] digits) {
        int len = digits.length - 1;
        int carry = 0;
        if(digits[len] != 9){
            digits[len]++;
            return digits;
        }
        else{
            digits[len] = 0;
            //carry = 1
            for(int i = len-1;i>=0;i--){
                //carry = 0;
                if(digits[i]<9){
                    digits[i]++;
                    return digits;
                }
                else if(digits[i] == 9){
                    digits[i] = 0;
                  //  carry = 1;
                }
                //digits[i] = digits[i] + carry;
                
                //digits[i]++;
                
            }
        }
       int[] result = new int[digits.length+1];
       for(int i = 1;i<result.length;i++){
           result[i] = 0;
       }
       result[0] = 1;
       return result; 
    }
}
