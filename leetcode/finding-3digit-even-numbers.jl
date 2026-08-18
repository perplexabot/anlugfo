function findEvenNumbers(digits::Vector{Int64})::Vector{Int64}
    if length(digits) < 3
        return []
    end

    final = Set()
    for (ind0, d0) in enumerate(digits)
        if iszero(d0)
            continue
        end
        num = [string(d0)]
        for (ind1, d1) in enumerate(digits)
            if ind1 == ind0
                continue
            end

            push!(num,string(d1))
            for (ind2, d2) in enumerate(digits)
                if ind2 == ind1 || ind2 == ind0 || isodd(d2)
                    continue
                end
                push!(num,string(d2))
                push!(final, parse(Int,join(num)))
                pop!(num)
            end
            pop!(num)
        end
    end
    return sort!(collect(final))
end

cases = [
    ([2, 1, 3, 0], [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]),
    ([2, 2, 8, 8, 2], [222, 228, 282, 288, 822, 828, 882]),
    ([3, 7, 5], []),
    ([1], []),
    ([1, 2], []),
    ([2, 2, 2], [222]),
]

for (digits, exp) in cases
    got = findEvenNumbers(digits)
    @assert got == exp "Failed case ($(digits)) - expecting ($(exp)), got ($(got))."
end
