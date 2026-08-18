function search(nums::Vector{Int64}, target::Int64)::Int64
    if isempty(nums)
        return -1
    end

    l = 1
    r = length(nums)

    while true
        if l > r
            return -1
        end

        mid = l + fld(r-l,2)
        if nums[mid] == target
            return mid
        elseif target > nums[mid]
            l = mid + 1
        else
            r = mid - 1
        end
    end
end

cases = [
    #  0  1  2  3  4  5
    ([-1, 0, 3, 5, 9, 12], 9, 5),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([-1, 0, 3, 5, 9, 12], 12, 6),
    ([1], 1, 1),
    ([1], 2, -1),
    ([1, 2], 1, 1),
    ([1, 2], 2, 2),
]

for (nums, target, exp) in cases
    got = search(nums, target)
    @assert got == exp "Failed case ($(nums), $(target)) - expecting ($(exp)), got ($(got))."
end
