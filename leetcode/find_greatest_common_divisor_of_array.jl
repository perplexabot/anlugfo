function findGCD(nums::Vector{Int64})::Int64
    return gcd(minimum(nums), maximum(nums))
end

cases = [([2, 5, 6, 9, 10], 2), ([7, 5, 6, 8, 3], 1), ([3, 3], 3), ([0, 10], 10)]

for (nums, exp) in cases
    got = findGCD(nums)
    @assert got == exp "Failed case ($(nums)) - expecting ($(exp)), got ($(got))."
end
