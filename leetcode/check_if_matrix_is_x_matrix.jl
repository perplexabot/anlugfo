function checkXMatrix(grid::Vector{Vector{Int64}})::Bool
    if isempty(grid) || isnothing(grid)
        return true
    end

    for (row_ind, row) in enumerate(grid)
        diag_ind0 = row_ind
        diag_ind1 = length(row) - diag_ind0 + 1
        for (col_ind, elem) in enumerate(row)
            if col_ind == diag_ind0 || col_ind == diag_ind1
                if iszero(elem)
                    return false
                end
            else
                if !iszero(elem)
                    return false
                end
            end
        end
    end
    return true
end

cases = [
    ([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]], true),
    ([[5, 7, 0], [0, 3, 1], [0, 5, 0]], false),
]

for (grid, exp) in cases
    got = checkXMatrix(grid)
    @assert got == exp "Failed case ($(grid)) - expecting ($(exp)), got ($(got))."
end
