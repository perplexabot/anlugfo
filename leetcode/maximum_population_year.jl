function maximumPopulation(logs::Vector{Vector{Int64}})::Int64
    year_histo = Dict()
    for log in logs
        start = log[1]
        stop = log[2] - 1
        for year in range(start, stop, step=1)
            if year in keys(year_histo)
                year_histo[year] += 1
            else
                year_histo[year] = 1
            end
        end
    end
    return minimum([year for year in keys(year_histo) if year_histo[year] == maximum(values(year_histo))])
end

cases = [([[1993, 1999], [2000, 2010]], 1993), ([[1950, 1961], [1960, 1971], [1970, 1981]], 1960)]

for (logs, exp) in cases
    got = maximumPopulation(logs)
    @assert got == exp "Failed case ($(logs)) - expecting ($(exp)), got ($(got))."
end
