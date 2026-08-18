function greatestLetter(s::String)::String
    if length(s) < 2
        return ""
    end

    cnts = Dict()
    for c in s
        if uppercase(c) in keys(cnts)
            push!(cnts[uppercase(c)], c)
        else
            cnts[uppercase(c)] = Set([c])
        end
    end

    possible = [string(x) for x in keys(cnts) if length(cnts[x]) > 1]
    return maximum(possible, init="")
end

cases = [
    ("lEeTcOdE", "E"),
    ("arRAzFif", "R"),
    ("AbCdEfGhIjK", ""),
    ("A", ""),
    ("Aa", "A"),
    ("Ab", ""),
    ("ab", ""),
    ("Aba", "A"),
]

for (s, exp) in cases
    got = greatestLetter(s)
    @assert got == exp "Failed case ($(s)) - expecting ($(exp)), got ($(got))."
end
