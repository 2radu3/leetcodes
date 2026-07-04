class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set(nums1.begin(), nums1.end());
        vector<int> res;
        unordered_set<int> alreadyAdded;
        
        for (int x : nums2) {
            if (set.count(x) && !alreadyAdded.count(x)) {
                res.push_back(x);
                alreadyAdded.insert(x);
            }
        }

        return res;
    }
};