"""
There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an
    integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk
    (list) of values after each insertion. The concatenation of all the chunks should result
    in a list of the sorted values.

Implement the OrderedStream class:
    - OrderedStream(int n) Constructs the stream to take n values.
    - String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then
        returns the largest possible chunk of currently inserted values that appear next in the
        order.

Example:
    Input
    ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
    [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
    Output
    [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

    Explanation
    // Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
    OrderedStream os = new OrderedStream(5);
    os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
    os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
    os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
    os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
    os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
    // Concatentating all the chunks returned:
    // [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc",
        "ddddd", "eeeee"]
    // The resulting order is the same as the order above.

Constraints:
    - 1 <= n <= 1000
    - 1 <= id <= n
    - value.length == 5
    - value consists only of lowercase letters.
    - Each call to insert will have a unique id.
    - Exactly n calls will be made to insert.

A:
    input empty stream? return []
    n = 0? not possible
    negative ids?, not possible
    similar ids?, not possible

D:
    need_num = 1
"""

from typing import List


from bisect import bisect


class OrderedStream:
    def __init__(self, n: int):
        self.need_index = 0
        self.n = n
        self.lst = [None for _ in range(n)]

    def insert(self, idKey: int, value: str) -> List[str]:
        ind = bisect(self.lst, idKey, key=lambda x: x[1] if x else self.n + 1)
        self.lst.insert(ind, (value, idKey))

        if self.need_index == idKey - 1:
            tmp = self.need_index + 1
            while tmp < len(self.lst) and self.lst[tmp]:
                if self.lst[tmp][1] - self.lst[tmp - 1][1] > 1:
                    break
                tmp += 1

            start = self.need_index
            end = tmp

            self.need_index = tmp
            return [x[0] for x in self.lst[start:end]]

        return []


os = OrderedStream(5)
print(os.insert(3, "ccccc"))
print(os.insert(1, "aaaaa"))
print(os.insert(2, "bbbbb"))
print(os.insert(5, "eeeee"))
print(os.insert(4, "ddddd"))

print('----')

os = OrderedStream(9)
print(os.insert(9, "nghbm"))  # []
print(os.insert(7, "hgeob"))  # []
print(os.insert(6, "mwlrz"))  # []
print(os.insert(4, "oalee"))  # []
print(os.insert(2, "bouhq"))  # []
print(os.insert(1, "mnknb"))  # ["mnknb","bouhq"]
print(os.insert(5, "qkxbj"))  # []
print(os.insert(8, "iydkk"))  # []
print(os.insert(3, "oqdnf"))  # ["oqdnf","oalee","qkxbj","mwlrz","hgeob","iydkk","nghbm"]
