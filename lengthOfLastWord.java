class Solution {
    public int lengthOfLastWord(String s) {
        int wordidx = s.length()-1;
        int idx = 0;
        while(wordidx >= 0){
            if(s.charAt(wordidx) != ' '){
                idx++;
            }
            else if(s.charAt(wordidx) == ' ' && idx != 0){
                break;
            }
            wordidx--;
        }
        return idx;
    }
}
