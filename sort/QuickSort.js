function quickSort(nums) {
    sort(nums, 0, nums.length - 1)
    return nums;
}

function sort(nums, low, high) {
    if (low >= high)
        return
    let splitPosition = partition(nums, low, high)
    // split position上的元素已经是有序的，所以不再参与排序
    sort(nums, low, splitPosition - 1)
    sort(nums, splitPosition + 1, high)
}

function partition(nums, low, high) {
    console.log(low, '   ', high, '     ', nums)
    let v = nums[low]
    let i = low
    let j = high + 1

    while (true) {
        // 这里一定要在相等的元素上停下来，否则会造成极端的不平衡二叉调用
        while (nums[++i] < v) if (i === high) break;
        while (nums[--j] > v) if (j === low) break;

        if (i >= j) break;
        exchange(nums, i, j);
    }
    exchange(nums, low, j)
    return j

}

function exchange(nums, i, j) {
    let temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
}

function test() {
    console.log(quickSort([3, 2, 42, 231, 423, 2, 6, 32, 123]))
    console.log(quickSort([1, 1, 1, 1, 1, 1, 1, 1, 1]))
}

test()