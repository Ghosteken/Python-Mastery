def min_coin_change(coins, amount):
    coins.sort(reverse=True)  # Sort the coins in descending order

    num_coins = 0
    i = 0

    while amount > 0 and i < len(coins):
        if coins[i] <= amount:
            num_coins += amount // coins[i]
            amount %= coins[i]
        i += 1

    return num_coins if amount == 0 else -1

# Example usage:
coins = [1, 5, 10, 25]
amount = 63
print(min_coin_change(coins, amount))  # Output: 6 (2x 25c, 1x 10c, 3x 1c)
