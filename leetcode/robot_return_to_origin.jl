function judgeCircle(moves::String)::Bool
    c = Dict('U'=>0, 'D'=> 0, 'L'=> 0, 'R'=>0)
    for move in moves
        c[move] = count(i->i==move, moves)
    end
    return c['U'] == c['D'] && c['L'] == c['R']
end

cases = [
    ("UD", true),
    ("D", false),
    ("LL", false),
    ("RRLL", true),
    ("ULDR", true),
    ("UR", false),
    ("URD", false),
]

for (moves, exp) in cases
    got = judgeCircle(moves)
    @assert got == exp "Failed case ($(moves)) - expecting ($(exp)), got ($(got))."
end
