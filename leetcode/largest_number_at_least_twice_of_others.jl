function dominantIndex(nums::Vector{Int64})::Int64
    min0 = -1
    min1 = -2
    for num in nums
        if min1 > min0
            min0 = max(min0, num)
        else
            min1 = max(min1, num)
        end
    end

    if min(min0,min1) * 2 <= max(min0, min1)
        return argmax(nums)
    else
        return -1
    end
end

cases = [
    ([3, 6, 1, 0], 2),
    ([1, 2, 3, 4], -1),
    ([1, 4], 2),
    ([1, 2], 2),
    ([1, 1], -1),
    ([3, 2], -1),
    ([0, 0, 0, 1], 4),
]

for (nums, exp) in cases
    got = dominantIndex(nums)
    @assert got == exp "Failed case ($(nums)) - expecting ($(exp)), got ($(got))."
end
