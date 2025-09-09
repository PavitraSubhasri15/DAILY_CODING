QUESTION:Number of People Aware of a Secret

On day 1, one person discovers a secret.

You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.

CODE:
class Solution:
    def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = [0] * (n + 2)
        share[1 + delay] += 1
        if 1 + forget <= n:
            share[1 + forget] -= 1
        curr_sharers = 0
        for day in range(2, n + 1):
            curr_sharers = (curr_sharers + share[day]) % MOD
            dp[day] = curr_sharers
            if day + delay <= n:
                share[day + delay] = (share[day + delay] + dp[day]) % MOD
            if day + forget <= n:
                share[day + forget] = (share[day + forget] - dp[day]) % MOD
        ans = 0
        for day in range(n - forget + 1, n + 1):
            ans = (ans + dp[day]) % MOD
        return ans
