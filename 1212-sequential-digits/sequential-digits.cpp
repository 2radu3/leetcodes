class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> res;
        for (int startDigit = 1; startDigit <= 9; startDigit++) {
            int num = startDigit;
            int nextDigit = startDigit + 1;

            while (num <= high && nextDigit <= 9) {
                num = num * 10 + nextDigit;

                if (num >= low && num <= high) {
                    res.push_back(num);
                }

                nextDigit++;
            }
        }
        sort(res.begin(), res.end());
        return res;
    }
};