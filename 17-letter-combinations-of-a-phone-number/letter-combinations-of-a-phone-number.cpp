class Solution {
public:
    vector<string> res;
    vector<string> letterCombinations(string digits) {
        
        unordered_map<int, string> map;
        map[2] = "abc";
        map[3] = "def";
        map[4] = "ghi";
        map[5] = "jkl";
        map[6] = "mno";
        map[7] = "pqrs";
        map[8] = "tuv";
        map[9] = "wxyz";

        string s = "";
        backtrack(digits, s, map, 0);
        return res;
    }

    void backtrack(string& digits, string& s, unordered_map<int, string>& map, int index) {
        if(s.size() == digits.size()) {
            res.push_back(s);
            return;
        }

        string t = map[digits[index] - '0'];
        for(int i = 0; i < t.size(); i++) {
            s.push_back(t[i]);
            backtrack(digits, s, map, index + 1);
            s.pop_back();
        }
    }


};