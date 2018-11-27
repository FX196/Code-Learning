package LeetCode;

class Solution_3 {
    public int lengthOfLongestSubstring(String s) {
        String curr = "";
        int start = 0;
        int max = 0;
        for (int i = 0; i < s.length(); i++) {
            curr = s.substring(start, i);
            max = i - start > max ? i - start : max;
            while (curr.indexOf(s.charAt(i)) != -1) {
                start += 1;
                curr = curr = s.substring(start, i);
            }
        }
        max = s.length() - start > max ? s.length() - start : max;

        return max;
    }

    public static void main(String args[]) {
        Solution_3 s = new Solution_3();
        System.out.println("" + s.lengthOfLongestSubstring(" "));
    }
}
