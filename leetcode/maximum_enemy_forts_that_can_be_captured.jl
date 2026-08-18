function captureForts(forts::Vector{Int64})::Int64
    if length(forts) < 2
        return 0
    end

    if !(1 in forts)
        return 0
    end

    base_a = 1
    while base_a <= length(forts)
        if forts[base_a] == 1 || forts[base_a] == -1
            break
        end
        base_a += 1
    end
    base_b = base_a + 1

    max_cap = 0
    caps = 0

    while base_b <= length(forts)
        if iszero(forts[base_a] + forts[base_b])
            max_cap = max(max_cap, caps)
            base_a = base_b
            base_b = base_a + 1
            caps = 0
        elseif forts[base_b] == forts[base_a]
            base_a = base_b
            base_b = base_a + 1
            caps = 0
        else
            caps += 1
            base_b += 1
        end
    end

    return max_cap
end

cases = [
    ([1, 0, 0, -1, 0, 0, 0, 0, 1], 4),
    ([0, 0, 1, -1], 0),
    ([1, -1], 0),
    ([1], 0),
    ([-1], 0),
    ([0], 0),
    ([1, 0, -1], 1),
    ([1, 0, 0, -1], 2),
    ([-1, 0, 0, 1], 2),
    ([-1, 0, 1, 0, -1], 1),
    ([-1, 0, 0, 1, 0, 0, 0, -1], 3),
    ([1, 0, 0, -1, 0, 0, -1, 0, 0, 1], 2),
    ([0, -1, -1, 0, -1], 0),
    ([0, 0, 1, 0, 1, 1], 0),
    ([0, 0, 1, -1], 0),
]

for (forts, exp) in cases
    got = captureForts(forts)
    @assert got == exp "Failed case ($(forts)) - expecting ($(exp)), got ($(got))."
end
