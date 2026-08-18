function slowestKey(releaseTimes::Vector{Int64}, keysPressed::String)::String
    if length(releaseTimes) == 1
        return keysPressed[1]
    end

    max_hold = releaseTimes[1]
    pot_keys = Set([keysPressed[1]])

    index = 2
    while index <= length(releaseTimes)
        hold_time = releaseTimes[index] - releaseTimes[index-1]
        if hold_time > max_hold
            max_hold = hold_time
            pot_keys = Set([keysPressed[index]])
        elseif hold_time == max_hold
            push!(pot_keys, keysPressed[index])
        end
        index += 1
    end

    return string(maximum(pot_keys))
end

cases = [
    ([9, 29, 49, 50], "cbcd", "c"),
    ([12, 23, 36, 46, 62], "spuda", "a"),
    ([9, 29, 49, 50], "cbcd", "c"),
]

for (releaseTimes, keys, exp) in cases
    got = slowestKey(releaseTimes, keys)
    @assert got == exp "Failed case ($(releaseTimes), $(keys)) - expecting ($(exp)), got ($(got))."
end
