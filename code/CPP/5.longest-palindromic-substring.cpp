#include <iostream>
using namespace std;
class Solution
{
public:
    string longestPalindrome(string s)
    {
        int n = s.length();
        if (n == 1)
            return s;
        if (n == 2 && s[0] == s[1])
            return s;
        int d[1000][1000] = {0};
        int maxLength = 0;
        string maxS = "";
        for (int i = 0; i < n; i++)
        {
            d[i][i] = 1;
            if (i < n - 1 && s[i] == s[i + 1])
            {
                d[i][i + 1] = 2;
            }
        }
        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = 0; j < n; j++)
            {
                if (i + 1 < n && j - 1 >= 0 && s[i] == s[j] && d[i + 1][j - 1] > 0)
                    d[i][j] = d[i + 1][j - 1] + 2;
                if (d[i][j] > maxLength)
                {
                    maxLength = d[i][j];
                    maxS = s.substr(i, j - i + 1);
                }
            }
        }
        return maxS;
    }
};
int main()
{
    Solution so = Solution();
    string S = "babad";
    cout << so.longestPalindrome(S) << endl;
}