#!/usr/bin/python3
#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    def getPrimes(n):
        """ Returns a list of prime numbers up to n """
        sieve = [1 for _ in range(n + 1)]
        sieve[0], sieve[1] = 0, 0
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = 0
        return [i for i, v in enumerate(sieve) if v]

    max_num = max(nums)
    primes = getPrimes(max_num)

    Maria_score = 0
    Ben_score = 0

    for n in nums:
        available = [True for _ in range(n + 1)]
        current_primes = [p for p in primes if p <= n]
        turn_maria = True
        
        while current_primes:
            prime = current_primes.pop(0)
            if available[prime]:
                for i in range(prime, n + 1, prime):
                    available[i] = False
            for prime in current_primes:
                if not available[prime]:
                    current_primes.remove(prime)
            turn_maria = not turn_maria
        
        if turn_maria:
            Ben_score += 1
        else:
            Maria_score += 1

    if Maria_score > Ben_score:
        return "Maria"
    elif Maria_score < Ben_score:
        return "Ben"
    else:
        return None


# Test
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
