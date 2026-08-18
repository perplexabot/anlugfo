function largestSumAfterKNegations(nums::Vector{Int64}, k::Int64)::Int64
    cnt = k
    sort!(nums)

    for i in range(1,length(nums), step=1)
        if iszero(cnt) || nums[i] >= 0
            break
        end

        if nums[i] < 0
            nums[i] *= -1
            cnt -= 1
        end
    end

    if 0 in nums || cnt <= 0
        return sum(nums)
    end

    if iszero(cnt % 2)
        return sum(nums)
    else
        _, ind = findmin(nums)
        nums[ind] *= -1
        return sum(nums)
    end

end

cases = [
    ([4, 2, 3], 1, 5),
    ([3, -1, 0, 2], 3, 6),
    ([2, -3, -1, 5, -4], 2, 13),
    ([-100], 1, 100),
    ([-100], 2, -100),
    ([-2, 5, 0, 2, -2], 3, 11),
]

for (nums, k, exp) in cases
    got = largestSumAfterKNegations(nums, k)
    @assert got == exp "Failed case ($(nums), $(k)) - expecting ($(exp)), got ($(got))."
end
