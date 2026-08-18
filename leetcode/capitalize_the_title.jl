function capitalizeTitle(title::String)::String
    final = []
    for word in split(title)
        if length(word) <= 2
            push!(final, lowercase(word))
        else
            push!(final, uppercase(word[1]) * lowercase(word[2:end]))
        end
    end
    return join(final, " ")
end

cases = [
    ("capiTalIze tHe titLe", "Capitalize The Title"),
    ("First leTTeR of EACH Word", "First Letter of Each Word"),
    ("i lOve leetcode", "i Love Leetcode"),
]

for (title, exp) in cases
    got = capitalizeTitle(title)
    @assert got == exp "Failed case ($(title)) - expecting ($(exp)), got ($(got))."
end
