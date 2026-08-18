function percentageLetter(s::String, letter::String)::Int64
    return round((count(letter, s)/length(s))*100,RoundDown)
end

cases = [
    ("foobar", "o", 33),
    ("jjjj", "k", 0),
    ("j", "j", 100),
    ("kj", "k", 50),
    ("kj", "j", 50),
    ("jjj", "j", 100),
    ("j", "k", 0),
]

for (s, letter, exp) in cases
    got = percentageLetter(s, letter)
    @assert got == exp "Failed case ($(s), $(letter)) - expecting ($(exp)), got ($(got))."
end
