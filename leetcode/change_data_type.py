"""
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+

Write a solution to correct the errors:

The grade column is stored as floats, convert it to integers.

The result format is in the following example.

Example 1:
    Input:
    DataFrame students:
    +------------+------+-----+-------+
    | student_id | name | age | grade |
    +------------+------+-----+-------+
    | 1          | Ava  | 6   | 73.0  |
    | 2          | Kate | 15  | 87.0  |
    +------------+------+-----+-------+
    Output:
    +------------+------+-----+-------+
    | student_id | name | age | grade |
    +------------+------+-----+-------+
    | 1          | Ava  | 6   | 73    |
    | 2          | Kate | 15  | 87    |
    +------------+------+-----+-------+
Explanation:
    The data types of the column grade is converted to int.

A:
    non floats in grade column?
        assume no

    row count = 0?
        cool
"""

import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = [int(x) for x in students['grade']]
    return students


cases = [
    (
        pd.DataFrame(
            [[1, 'Ava', 6, 73.0], [2, 'Kate', 15, 87.0]],
            columns=['student_id', 'name', 'age', 'grade'],
        ),
        pd.DataFrame(
            [[1, 'Ava', 6, 73], [2, 'Kate', 15, 87]],
            columns=['student_id', 'name', 'age', 'grade'],
        ),
    )
]

for students, exp in cases:
    assert exp.equals(changeDatatype(students)), f"Failed case ({students})"
