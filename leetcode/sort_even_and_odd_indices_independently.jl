function sortEvenOdd(nums::Vector{Int64})::Vector{Int64}
    if length(nums) < 3
        return nums
    end

    e = [x for (ind, x) in enumerate(nums) if iseven(ind-1)]
    o = [x for (ind, x) in enumerate(nums) if isodd(ind-1)]

    sort!(e,rev=true)
    sort!(o)

    final = []
    while !isempty(e)
        push!(final, pop!(e))
        if !isempty(o)
            push!(final, pop!(o))
        end
    end
    return final
end


cases = [
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([2, 1], [2, 1]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([5, 9666, 32], [5, 9666, 32]),
    ([32, 12222, 4], [4, 12222, 32]),
    ([4, 1, 2, 3], [2, 3, 4, 1]),
]

for (nums, exp) in cases
    got = sortEvenOdd(nums)
    @assert got == exp "Failed case ($(nums)) - expecting ($(exp)), got ($(got))."
end
