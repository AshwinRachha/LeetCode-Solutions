class Solution {
public:
    int numKLenSubstrNoRepeats(string S, int K) {
	if (K > S.size()) return 0;

	int repeats = 0, res = 0;
	vector<int> window(26, 0);

	for(int i = 0; i < K; i++) 
		if(window[S[i] - 'a']++ == 1) 
			repeats++;

	if(!repeats) res++;

	for(int i = K; i < S.size(); i++) {
		if(--window[S[i - K] - 'a'] == 1) repeats--;
		if(window[S[i] - 'a']++ == 1) repeats++;
		if(!repeats) res++;
	}
	return res;
}
};