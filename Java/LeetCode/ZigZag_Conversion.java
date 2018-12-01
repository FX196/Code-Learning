package LeetCode;

import java.util.Arrays;

class Solution_6 {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        if (s.length() < numRows) return s;
        String[] strings = new String[numRows];
        Arrays.fill(strings, "");
        int row = 0;
        int step = 1;
        for (char c : s.toCharArray()) {
            strings[row] += c;
            if (row == 0) {
                step = 1;
            } else if (row == numRows - 1) {
                step = -1;
            }
            row += step;
        }
        StringBuilder strBuilder = new StringBuilder();
        for (String str : strings) {
            strBuilder.append(str);
        }
        return strBuilder.toString();
    }
}