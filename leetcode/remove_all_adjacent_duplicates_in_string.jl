function removeDuplicates(s::String)::String
    tmp = []
    for c in s
        if !isempty(tmp) && tmp[end] == c
            pop!(tmp)
        else
            push!(tmp,c)
        end
    end
    return join(tmp)
end

cases = [
    ("abbaca", "ca"),
    ("azxxzy", "ay"),
    ("x", "x"),
    ("xx", ""),
    ("abba", ""),
]

for (s, exp) in cases
    got = removeDuplicates(s)
    @assert got == exp "Failed case ($(s)) - expecting ($(exp)), got ($(got))."
end
