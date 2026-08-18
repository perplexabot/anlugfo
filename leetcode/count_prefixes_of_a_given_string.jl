function countPrefixes(words::Vector{String}, s::String)::Int64
    return sum([1 for word in words if startswith(s, word)])
end

cases = [(["a", "b", "c", "ab", "bc", "abc"], "abc", 3), (["a", "a"], "aa", 2), (["b"], "a", 0)]

for (words, s, exp) in cases
    got = countPrefixes(words, s)
    @assert got == exp "Failed case ($(case)) - expecting ($(exp)), got ($(got))."
end
