class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []

        for i in range(len(transactions)):
            curr = transactions[i].split(',')

            is_invalid = int(curr[2]) > 1000

            for j in range(len(transactions)):
                if i == j:
                    continue

                nxt = transactions[j].split(',')

                if (curr[0] == nxt[0]
                    and curr[-1] != nxt[-1]
                    and abs(int(curr[1]) - int(nxt[1])) <= 60):

                    is_invalid = True
                    break

            if is_invalid:
                invalid.append(transactions[i])

        return invalid
