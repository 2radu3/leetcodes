class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> table;
        int n = nums.size();
        for(int i = 0; i < n; i++) {
            table[nums[i]]++;
        }
        n = n / 2;
        for (auto a : table) {
            if(a.second > n) {
                return a.first;
            }
        }
        return 0;
    }
};