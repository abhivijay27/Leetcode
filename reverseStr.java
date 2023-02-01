class Solution {
    public String reverseStr(String s, int k) {
        char[] string = s.toCharArray();
        for (int start = 0; start < string.length; start += 2 * k) {
            int i = start, j = Math.min(start + k - 1, string.length - 1);
            while (i < j) {
                char tmp = string[i];
                string[i++] = string[j];
                string[j--] = tmp;
            }
        }
        return new String(string);
    }
}
