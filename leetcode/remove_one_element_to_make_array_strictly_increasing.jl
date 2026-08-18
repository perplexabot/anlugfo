function canBeIncreasing(nums::Vector{Int64})::Bool
    if length(nums) < 2
        return true
    end

    i = 1
    hits = 0
    ind = 1
    while i <= length(nums) -1
        if nums[i+1] <= nums[i]
            hits += 1
            ind = i
        end
        i += 1
    end

    if hits == 0
        return true
    end

    if hits == 1
        if (ind == 1) || (ind == length(nums) -1)
            return true
        end

        if (nums[ind-1] < nums[ind+1]) || (ind+2 <= length(nums) && nums[ind+2] > nums[ind])
            return true
        end
    end

    return false
end

cases = [
    ([1, 2, 10, 5, 7], true),
    ([2, 3, 1, 2], false),
    ([1, 1, 1], false),
    ([1], true),
    ([2, 1], true),
    ([1, 2], true),
    ([3, 2, 1], false),
    ([105, 924, 32, 968], true),
    ([100, 21, 100], true),
    ([512, 867, 904, 997, 403], true),
]

for (nums, exp) in cases
    got = canBeIncreasing(nums)
    @assert got == exp "Failed case ($(nums)) - expecting ($(exp)), got ($(got))."
end
