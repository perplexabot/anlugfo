function numJewelsInStones(jewels::String, stones::String)::Int64
    return sum([1 for stone in stones if stone in jewels])
end

cases = [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0),
    ("", "abc", 0),
    ("ad", "", 0),
    ("abc", "d", 0),
    ("a", "A", 0),
]

for (jewels, stones, exp) in cases
    got = numJewelsInStones(jewels, stones)
    @assert got == exp "Failed case ($(jewels), $(stones)) - expecting ($(exp)), got ($(got))."
end
