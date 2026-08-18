function sortPeople(names::Vector{String}, heights::Vector{Int64})::Vector{String}
    person_to_height = [x for x in zip(names, heights)]
    sort!(person_to_height, by=i->i[2], rev=true)
    return [x for (x,y) in person_to_height]
end

cases = [
    (["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
    (["Alice", "Bob", "Bob"], [155, 185, 150], ["Bob", "Alice", "Bob"]),
    (["Alice"], [120], ["Alice"]),
    (["Alice", "Bob"], [180, 120], ["Alice", "Bob"]),
    (["Alice", "Bob"], [120, 180], ["Bob", "Alice"]),
]

for (names, heights, exp) in cases
    got = sortPeople(names, heights)
    @assert got == exp "Failed case ($(names), $(heights)) - expecting ($(exp)),  got ($(got))."
end
