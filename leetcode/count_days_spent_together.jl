function countDaysTogether(arriveAlice::String, leaveAlice::String, arriveBob::String, leaveBob::String)::Int64
    month_to_days = Dict(month => day for (month,day) in enumerate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
    alice_month_arrive, alice_day_arrive = [parse(Int, x) for x in split(arriveAlice, '-')]
    alice_month_leave, alice_day_leave = [parse(Int, x) for x in split(leaveAlice, '-')]
    alice_days_in_rome = Set()

    for m in range(alice_month_arrive, alice_month_leave)
        month_start_day = 1
        if m == alice_month_arrive
            month_start_day = alice_day_arrive
        end

        month_end_day = alice_day_leave
        if m != alice_month_leave
            month_end_day = month_to_days[m]
        end

        for d in range(month_start_day, month_end_day, step=1)
            push!(alice_days_in_rome, (m,d))
        end
    end

    bob_month_arrive, bob_day_arrive = [parse(Int, x) for x in split(arriveBob, '-')]
    bob_month_leave, bob_day_leave = [parse(Int, x) for x in split(leaveBob, '-')]
    bob_days_in_rome = Set()

    for m in range(bob_month_arrive, bob_month_leave)
        month_start_day = 1
        if m == bob_month_arrive
            month_start_day = bob_day_arrive
        end

        month_end_day = bob_day_leave
        if m != bob_month_leave
            month_end_day = month_to_days[m]
        end

        for d in range(month_start_day, month_end_day, step=1)
            push!(bob_days_in_rome, (m,d))
        end
    end

    return length(intersect(bob_days_in_rome, alice_days_in_rome))
end

cases = [
    ("08-15", "08-18", "08-16", "08-19", 3),
    ("10-01", "10-31", "11-01", "12-31", 0),
    ("09-01", "10-19", "06-19", "10-20", 49),
]

for (arrA, leavA, arrB, leavB, exp) in cases
    got = countDaysTogether(arrA, leavA, arrB, leavB)
    @assert got == exp "Failed case ($(leavA), $(arrA), $(leavB), $(arrB)) - expecting ($(exp)), got ($(got))."
end
