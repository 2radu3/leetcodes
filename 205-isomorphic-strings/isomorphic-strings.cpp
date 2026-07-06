class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> mapS;
        unordered_map<char, char> mapT;

        if (s.size() != t.size()) return false;
        for(int i = 0; i < s.size(); i++) {
            char cs = s[i];
            char ct = t[i];
            if(mapS.count(cs) && mapS[cs] != ct) return false;
            if(mapT.count(ct) && mapT[ct] != cs) return false;

            mapS[cs] = ct;
            mapT[ct] = cs;
        }
        return true;
    }
};