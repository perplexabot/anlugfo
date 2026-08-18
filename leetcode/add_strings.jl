function addStrings(num1::String, num2::String)::String
    x = num1
    y = num2
    if length(x) > length(y)
        a = "0" ^ (length(x) - length(y))
        y = a * y
    else
        b = "0" ^ (length(y) - length(x))
        x = b * x
    end

    carry = 0
    final = []
    for (a,b) in zip(reverse(x), reverse(y))
        z = parse(Int,a) + parse(Int,b) + carry
        append!(final, string(z % 10))
        carry = fld(z,10)
    end

    if !iszero(carry)
        append!(final, string(carry))
    end

    return join(reverse(final))
end

cases = [
    ("11", "123", "134"),
    ("456", "77", "533"),
    ("0", "0", "0"),
]

for (a, b, exp) in cases
    got = addStrings(a, b)
    @assert got == exp "Failed case ($(a) + $(b)) - expecting ($(exp)), got ($(got))."
end
