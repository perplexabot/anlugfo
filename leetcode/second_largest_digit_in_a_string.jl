function secondHighest(s::String)::Int64
    digits = "0123456789"

    ds = Set()
    for c in s
        if c in digits
            push!(ds, c)
        end
    end

    if length(ds) < 2
        return -1
    end

    pop!(ds, maximum(ds))
    return parse(Int, maximum(ds))
end

cases = [
    ("dfa12321afd", 2),
    ("abc1111", -1),
]

for (s, exp) in cases
    got = secondHighest(s)
    @assert got == exp "Failed case ($(s)) - got ($(got)), expecting ($(exp))."
end
