function isAnagram(s::String, t::String)::Bool
    c0 = Dict(c => count(i->i==c, s) for c in s)
    c1 = Dict(c => count(i->i==c, t) for c in t)
    return c0 == c1
end

cases = [
    ("anagram", "nagaram", true),
    ("rat", "car", false),
    ("a", "b", false),
    ("a", "a", true),
    ("ab", "ba", true),
]

for (s, t, exp) in cases
    got = isAnagram(s, t)
    @assert got == exp "Failed case ($(s), $(t)) - expecting ($(exp)), got ($(got))."
end
