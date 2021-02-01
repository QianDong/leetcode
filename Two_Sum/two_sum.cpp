class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        vector<int> returnvalue;
        int i=0, j=0, d=0;
        for (i=0; i<numbers.size(); i++){
                d=target-numbers[i];
                j=i+1;
                for (j=i+1;j<numbers.size();j++){
                    if (d==numbers[j]){
                        returnvalue.push_back(i+1);
                        returnvalue.push_back(j+1);
                        return returnvalue;
                    }
                }
        }
    }
};
