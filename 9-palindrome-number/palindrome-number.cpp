class Solution {
public:
    bool isPalindrome(int x) {
        long int reversed = 0;
        int copie = x;
        while (copie > 0) {
            reversed = reversed * 10 + (copie%10);
            copie = copie / 10;
        }

        return reversed == x;
    }
};