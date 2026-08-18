function minimumMoves(s::String)::Int64
    curr = 1
    hits = 0
    while curr <= length(s)
        if s[curr] == 'X'
            hits += 1
            curr += 3
        else
            curr += 1
        end
    end
    return hits
end

cases = [
    ("XXX", 1),
    ("XXOX", 2),
    ("OOOO", 0),
    ("X", 1),
    ("XX", 1),
    ("XXX", 1),
    ("XXXX", 2),
    ("XXXXX", 2),
    ("XXXXXX", 2),
    ("XXXXXXX", 3),
    ("XXXOXXX", 2),
    ("XXXXOXXX", 3),
    ("O", 0),
    ("OO", 0),
    ("OOO", 0),
    ("OXOX", 1),
]

for (s, exp) in cases
    got = minimumMoves(s)
    @assert got == exp "Failed case ($(s)) - expecting ($(exp)), got ($(got))."
end
