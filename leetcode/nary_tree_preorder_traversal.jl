using DataStructures

struct Node
    val::Int64
    children

    function Node(val=0, children=nothing)
        new(val, children)
    end
end


function preorder(root::Node)::Vector{Int64}
    out = []
    Q = DataStructures.Deque{Node}()

    push!(Q, root)
    while !isempty(Q)
        curr = popfirst!(Q)
        if !isnothing(curr)
            push!(out, curr.val)
            if !isnothing(curr.children)
                pushfirst!(Q, curr.children...)
            end
        end
    end

    return out
end

case0 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
case1 = Node(
    1,
    [
        Node(2),
        Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
        Node(4, [Node(8, [Node(12)])]),
        Node(5, [Node(9, [Node(13)]), Node(10)]),
    ],
)

cases = [
    (case0, [1, 3, 5, 6, 2, 4]),
    (case1, [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]),
]

for (case, exp) in cases
    got = preorder(case)
    @assert got == exp "Failed case ($(case)) - expecting ($(exp)), got ($(got))."
end
