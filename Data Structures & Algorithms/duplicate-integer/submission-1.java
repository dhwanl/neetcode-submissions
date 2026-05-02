class Solution {
    public boolean hasDuplicate(int[] nums) {
        int leng = nums.length;

        for (int i = 0; i < leng; i++) {
            int prev = nums[i];
            for (int j = i + 1; j < leng; j++) {
                if (prev == nums[j]) {
                return true;
                }
            }
        }

        return false;
    }
}