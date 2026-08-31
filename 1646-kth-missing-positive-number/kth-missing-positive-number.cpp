class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
            int cnt = 0;
            int i = 1;
            unordered_map<int,bool> is_present;

            for(int i = 0; i < arr.size();i++){
                is_present[arr[i]] = true;
            }

            while(cnt != k){
                if(!is_present[i]){
                    cnt++;
                    
                }
                i++;
            }

            return --i;
    }
};