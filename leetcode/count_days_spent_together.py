"""
Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city
    from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the
    dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format
    "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that
    the number of days per month can be represented as:
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

Example 1:
    Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
    Output: 3
    Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August
        16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the
        answer is 3.

Example 2:
    Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
    Output: 0
    Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.



Constraints:
    All dates are provided in the format "MM-DD".
    Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
    The given dates are valid dates of a non-leap year.

A:
    alice/bob leaves before he/she arrives -> not possible (possible to be equal)
    no overlap -> return 0
    does it count if bob leaves the same day alice arrives? -> we'll find out i guess

D:
    make set of days in rome for aice and bob
    return length of intersection
"""


class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        month_to_days = {
            month + 1: day
            for month, day in enumerate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
        }

        alice_month_arrive, alice_day_arrive = [int(x) for x in arriveAlice.split('-')]
        alice_month_leave, alice_day_leave = [int(x) for x in leaveAlice.split('-')]

        alice_days_in_rome = set()
        for m in range(int(alice_month_arrive), int(alice_month_leave) + 1):
            month_end_day = (
                month_to_days[m] + 1 if m != alice_month_leave else int(alice_day_leave) + 1
            )
            month_start_day = alice_day_arrive if m == alice_month_arrive else 1
            for d in range(month_start_day, month_end_day):
                alice_days_in_rome.add((m, d))

        bob_month_arrive, bob_day_arrive = [int(x) for x in arriveBob.split('-')]
        bob_month_leave, bob_day_leave = [int(x) for x in leaveBob.split('-')]

        bob_days_in_rome = set()
        for m in range(int(bob_month_arrive), int(bob_month_leave) + 1):
            month_end_day = month_to_days[m] + 1 if m != bob_month_leave else int(bob_day_leave) + 1
            month_start_day = bob_day_arrive if m == bob_month_arrive else 1
            for d in range(month_start_day, month_end_day):
                bob_days_in_rome.add((m, d))

        return len(alice_days_in_rome.intersection(bob_days_in_rome))


sol = Solution()

cases = [
    #    ("08-15", "08-18", "08-16", "08-19", 3),
    #    ("10-01", "10-31", "11-01", "12-31", 0),
    ("09-01", "10-19", "06-19", "10-20", 49),
]

for (arrA, leavA, arrB, leavB, exp) in cases:
    assert (
        got := sol.countDaysTogether(arrA, leavA, arrB, leavB)
    ) == exp, f"Failed case ({leavA}, {arrA}, {leavB}, {arrB}) - expecting ({exp}), got ({got})."
