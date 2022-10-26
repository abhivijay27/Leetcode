class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
       int wordidx1 = 0, wordidx2 = 0;
       int idx1 = 0, idx2 = 0;
       while(wordidx1<word1.length && wordidx2<word2.length){
           if(word1[wordidx1].charAt(idx1)!=word2[wordidx2].charAt(idx2)){
               return false;
           }
           idx1++;
           idx2++;
           if(idx1 == word1[wordidx1].length()){
               idx1 = 0;
               wordidx1++;
           }
           if(idx2 == word2[wordidx2].length()){
               idx2 = 0;
               wordidx2++;
           }
       }
        return wordidx1 == word1.length && wordidx2 == word2.length;
    }
}
