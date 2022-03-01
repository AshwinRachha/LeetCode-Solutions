class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
    if (!numerator) return "0";
    string res;
    if (numerator < 0 ^ denominator < 0) res += '-';
    long num = numerator < 0 ? (long)numerator*(-1) : (long)numerator;
    long den = denominator < 0 ? (long)denominator*(-1) : (long)denominator;
    long integral = num/den, rem = num%den;
    res += to_string(integral);
    if (rem == 0) return res;
    res += '.';
    unordered_map<long, long> mp;
    rem *= 10;
    while (rem) {
        if (mp.find(rem) != mp.end()) {
            res.insert(mp[rem],1,'(');
            res += ')';
            break;
        }
        mp[rem] = res.size();
        long quotient = rem/den;
        res += to_string(quotient);
        rem = (rem%den)*10;
    }

    return res;
}
};