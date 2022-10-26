class Solution {
    private int result = 0;
  public int maxLength(List<String> arr) {
      if(arr == null)
          return 0;
      dfs(arr,"",0);
      return result;
  }
    public void dfs(List<String>arr,String path,int idx){
        boolean isUnique = checkUnique(path);
        if(isUnique)
            result = Math.max(path.length(),result);
        if(idx == arr.size() || !isUnique)
            return;
        for(int i = idx;i<arr.size();i++)
            dfs(arr, path + arr.get(i), i+1);
    }
    public boolean checkUnique(String s){
        Set<Character> set = new HashSet<>();
        for(char c: s.toCharArray()){
            if(set.contains(c))
                return false;
            set.add(c);
        }
        return true;
    }
}
