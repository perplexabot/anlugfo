function diStringMatch(s::String)::Vector{Int64}
    right = 0
    left = 0
    perm = [0]
    for c in s
        if c == 'I'
            right += 1
            append!(perm, right)
        else
            left -= 1
            append!(perm, left)
        end
    end
    return [x - left for x in perm]
end

cases = [
    ("IDID", [0, 4, 1, 3, 2]),
    ("III", [0, 1, 2, 3]),
    ("DDI", [3, 2, 0, 1]),
    ("", []),
    ("I", [0]),
    ("H", [0]),
]

for (s, exp) in cases
    got = diStringMatch(s)
    @assert got == exp "Failed case ($(s)) - expecting ($(exp)), got ($(got))."
end
