class Solution {
public:
string entityParser(string text)
{
unordered_map <string, string> mp;
mp["&quot;"] = "\"";
mp["&apos;"] = "\'";
mp["&amp;"] = "&";
mp["&gt;"] = ">";
mp["&lt;"] = "<";
mp["&frasl;"] = "/";
string ans = "";
int start = 0;
for(int end = 0; end < text.size(); end++)
{
if(text[end] == '&')
{
start = end;
while(end+1 < text.size() && text[end+1] != '&')
end++;
while(end < text.size() && text[end]!=';')
end++;
string temp = text.substr(start, end - start +1);
if(mp.find(temp) != mp.end())
ans += mp[temp];
else
ans += temp;
}
else
{
ans += text[end];
}
}
return ans;
}
};
​