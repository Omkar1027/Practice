#include <stdio.h>

long long maximumSubarraySum(int* nums, int numsSize, int k) {
    long long maxNum=0, tempMaxNum=0;
    int no=0;
    for(int i=0;i<numsSize-k+1;i++){
        tempMaxNum=nums[i];
        for(int j=i;j<i+k-1;j++){
            for(int a=j;a>=i;a--){
                if(nums[j]==nums[a-1]){
                    break;
                }
            }
            if(nums[j]!=nums[j+1]){
                printf("For i :%d, for j: %d, added nums[j+1]: %d\n",i,j,nums[j+1]);
                tempMaxNum+=nums[j+1];
            }
            else break;
            if((j==i+k-2) && (nums[j]!=nums[j+1]) && (maxNum<tempMaxNum)){
                printf("Updated maxNum: %lld\n", tempMaxNum);
                maxNum=tempMaxNum;
            }
        }
    }
    return maxNum;
}



int main() {
    int nums[] = {9,9,9,1,2,3}; // Example input array
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int k = 3; // Example value of k

    long long result = maximumSubarraySum(nums, numsSize, k);
    printf("Maximum Subarray Sum: %lld\n", result);

    return 0;
}
