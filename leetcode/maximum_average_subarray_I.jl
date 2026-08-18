function findMaxAverage(nums::Vector{Int64}, k::Int64)::Float64
    max_ave = sum(nums[begin:k])
    curr_ave = max_ave
    e = k + 1
    while e <= length(nums)
        curr_ave = curr_ave = curr_ave - nums[e - k] + nums[e]
        max_ave = max(max_ave, curr_ave)
        e += 1
    end
    return max_ave / k
end

cases = [
    ([1, 12, -5, -6, 50, 3], 4, 12.75000),
    ([5], 1, 5.00000),
    ([1, 10], 1, 10),
    ([1, 10], 2, 5.5),
    ([0, 0, 0], 3, 0),
    ([0, 0, 0], 2, 0),
    ([0, 0, 0], 1, 0),
]

for (nums, k, exp) in cases
    got = findMaxAverage(nums, k)
    @assert got == exp "Failed case ($(nums), $(k)) - expecting ($(exp)), got ($(got))."
end
