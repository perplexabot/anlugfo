function maximumTime(time::String)::String
    new = []
    if time[begin:2] == "??"
        append!(new, "23")
    elseif startswith(time[begin:2], "?")
        if parse(Int, time[2]) < 4
            append!(new, "2" * time[2])
        else
            append!(new, "1" * time[2])
        end
    elseif endswith(time[begin:2], "?")
        if parse(Int, time[1]) < 2
            append!(new, time[1] * "9")
        else
            append!(new, time[1] * "3")
        end
    else
        append!(new, time[begin:2])
    end

    append!(new, ":")

    if time[4] == '?'
        append!(new, "5")
    else
        append!(new, time[4])
    end

    if time[5] == '?'
        append!(new, "9")
    else
        append!(new, time[5])
    end
    return join(new, "")
end

cases = [
#     12345
    ("2?:?0", "23:50"),
    ("0?:3?", "09:39"),
    ("1?:22", "19:22"),
    ("??:??", "23:59"),
    ("2?:??", "23:59"),
    ("??:?9", "23:59"),
    ("?4:03", "14:03"),
    ("00:01", "00:01"),
]

for (time, exp) in cases
    got = maximumTime(time)
    @assert got == exp "Failed case ($(time)) - expecting ($(exp)), got ($(got))."
end
