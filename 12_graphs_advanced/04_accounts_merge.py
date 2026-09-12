"""
Problem: Given a list of accounts, each [name, email1, email2, ...],
merge accounts that share at least one email (same person may have
listed slightly different names, but shared emails prove it's the
same account). Return the merged accounts, each with the name first
and all emails sorted, deduplicated.
Source : LeetCode 721 - Accounts Merge

Example:
    Input:  [["John","johnsmith@mail.com","john_newyork@mail.com"],
              ["John","johnsmith@mail.com","john00@mail.com"],
              ["Mary","mary@mail.com"],
              ["John","johnnybravo@mail.com"]]
    Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
              ["Mary","mary@mail.com"],
              ["John","johnnybravo@mail.com"]]

Idea: a less obvious Union-Find application than 02/03 - the union-
find here operates over *account indices*, not over an explicit
graph of nodes/edges. Walk every account's emails; the first time an
email is seen, remember which account index it came from. If that
same email shows up again under a different account, union those two
account indices together - shared emails are the "edges" proving two
account entries belong to the same real person. After processing
everything, group emails by their account's *root* index, and each
group becomes one merged account. This pattern - deriving union
operations from shared attributes rather than an explicit edge list -
generalizes to any "merge records that share some key" problem.
"""


def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    n = len(accounts)
    parent = list(range(n))

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> None:
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    email_to_account: dict[str, int] = {}
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_account:
                union(i, email_to_account[email])
            else:
                email_to_account[email] = i

    grouped: dict[int, set[str]] = {}
    for email, i in email_to_account.items():
        root = find(i)
        grouped.setdefault(root, set()).add(email)

    return [[accounts[root][0]] + sorted(emails) for root, emails in grouped.items()]


def _normalize(merged):
    return sorted(tuple(acc) for acc in merged)


if __name__ == "__main__":
    tests = [
        ([
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ], [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]),
        ([["A", "a1@mail.com"]], [["A", "a1@mail.com"]]),
    ]

    for i, (accounts, expected) in enumerate(tests, 1):
        got = accounts_merge(accounts)
        status = "PASS" if _normalize(got) == _normalize(expected) else "FAIL"
        print(f"Test {i}: {status} (got {got}, expected {expected})")
