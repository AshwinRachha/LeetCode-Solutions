
class Solution {
public:
    string entityParser(string text) {
        string result = "";
        unordered_map<string, string> html ({{"&quot;", "\""},
                                             {"&apos;", "\'"},
                                             {"&amp;", "&"},
                                             {"&gt;", ">"},
                                             {"&lt;", "<"},
                                             {"&frasl;", "/"}});
        for(int i=0; i<text.size(); i++){
            if(text[i] == '&'){
                bool found_match = false;
                for(int k=4; i + k <= text.size() && k<=7; k++){
                    string extra = text.substr(i, k);
                    if(html.count(extra)){
                        result+=html[extra];
                        i+=k-1;
                        found_match = true;
                        break;
                    }
                }
                if(!found_match){
                    result+=text[i];
                }
            } else {
                result+=text[i];
            }
        }
        return result;
    }
};