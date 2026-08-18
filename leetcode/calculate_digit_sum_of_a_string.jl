function digitSum(s::String, k::Int64)::String
    curr = s
    while length(curr) > k
        new = []
        for chunk in [curr[i:min(i+k-1,end)] for i in range(1,length(s), step=k)]
            if !isempty(chunk)
                append!(new, string(sum(parse(Int,x)  for x in chunk)))
            end
        end
        curr = join(new)
    end
    return curr
end

cases = [("11111222223", 3, "135"), ("00000000", 3, "000"), ("1", 4, "1")]

for (s, k, exp) in cases
    got = digitSum(s, k)
    @assert got == exp "Failed case ($(s), $(k)) - expecting ($(exp)), got ($(got))."
end
