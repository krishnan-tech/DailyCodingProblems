def productExceptSelf(nums):
    answer = [1]*len(nums)
    answer[0] = 1
    for i in range(1, len(nums)):
        answer[i] = answer[i-1] * nums[i-1]
    rightProduct = 1
    for i in range(len(nums)-1, -1, -1):
        answer[i] = answer[i] * rightProduct
        rightProduct *= nums[i]
    return answer

if __name__ == '__main__':
    nums=[1,2,3,4,5]
    productExceptSelf(nums)
