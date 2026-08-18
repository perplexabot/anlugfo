"""
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0
    and 1 respectively. All students stand in a queue. Each student either prefers square or
    circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are
    placed in a stack. At each step:
    - If the student at the front of the queue prefers the sandwich on the top of the stack,
        they will take it and leave the queue.
    - Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable
    to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the
    ith sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of
    the jth student in the initial queue (j = 0 is the front of the queue). Return the number of
    students that are unable to eat.

Example 1:
    Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
    Output: 0
    Explanation:
    - Front student leaves the top sandwich and returns to the end of the line making
        students = [1,0,0,1].
    - Front student leaves the top sandwich and returns to the end of the line making
        students = [0,0,1,1].
    - Front student takes the top sandwich and leaves the line making
        students = [0,1,1] and sandwiches = [1,0,1].
    - Front student leaves the top sandwich and returns to the end of the line making
        students = [1,1,0].
    - Front student takes the top sandwich and leaves the line making
        students = [1,0] and sandwiches = [0,1].
    - Front student leaves the top sandwich and returns to the end of the line making
        students = [0,1].
    - Front student takes the top sandwich and leaves the line making
        students = [1] and sandwiches = [1].
    - Front student takes the top sandwich and leaves the line making
        students = [] and sandwiches = [].
    Hence all students are able to eat.

Example 2:
    Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
    Output: 3

Constraints:
    - 1 <= students.length, sandwiches.length <= 100
    - students.length == sandwiches.length
    - sandwiches[i] is 0 or 1.
    - students[i] is 0 or 1.

A:
    No sandwiches:
        return student size
    No students:
        return 0
    All students want one sandwich
        return number of students - the number of that sandwich
    All sandwiches are the same type
        return (len(sandwiches) - number of students who like that type) + students who like
        other type
    Sandwich length != student length
        not possible

D:
    Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
    wants 1, gets
    st = 11001, sa = 00011
    wants 1, back
    st = 10011, sa = 00011
    wants 1, back
    st = 00111, sa = 00011
    wants 0, gets
    st = 0111, sa = 0011
    wants 0, gets
    st = 111, sa = 011

    return len(st)

P:
    while len(set(students)) > 1:
        if student[0] == sandwiches[0]:
            student.pop(0)
            sandwiches.pop(0)
        else:
            student.append(student.pop(0))
    return len(students)

"""

from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque

        st = deque(students)
        sa = deque(sandwiches)
        while st and not (len(set(st)) == 1 and st[0] != sa[0]):
            if st[0] == sa[0]:
                st.popleft()
                sa.popleft()
            else:
                st.append(st.popleft())
        return len(st)


cases = [
    ([1, 1, 0, 0], [0, 1, 0, 1], 0),
    ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3),
    ([1, 1, 1], [0, 0, 1], 3),
    ([1], [0], 1),
    ([0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], 0),
]

sol = Solution()
for st, sa, exp in cases:
    assert (
        got := sol.countStudents(st, sa)
    ) == exp, f"Failed case ({st}, {sa}) - expecting ({exp}, got ({got})."
