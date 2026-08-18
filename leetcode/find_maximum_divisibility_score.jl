function maxDivScore(nums::Vector{Int64}, divisors::Vector{Int64})::Int64
    candidates = Set()
    curr_max = -Inf
    for d in divisors
        cnt = 0
        for n in nums
            if iszero(n % d)
                cnt += 1
            end
        end

        if cnt > curr_max
            curr_max = cnt
            candidates = Set([d])
        end

        if cnt == curr_max
            candidates = push!(candidates, d)
        end
    end

    return minimum(candidates)
end

cases = [
    ([4, 7, 9, 3, 9], [5, 2, 3], 3),
    ([20, 14, 21, 10], [5, 7, 5], 5),
    ([12], [10, 16], 10),
    ([12], [1], 1),
]

for (nums, divs, exp) in cases
    got = maxDivScore(nums, divs)
    @assert got == exp "Failed case ($(nums), $(divs)) - expecting ($(exp)), got ($(got))."
end
