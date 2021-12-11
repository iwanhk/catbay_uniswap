#!/usr/bin/python3
"""
What are DEX ?
Token1 -> Token2

CPMM (x.y = k)

DECIMALS = 10 ** 9

x: Token1
y: Token2

x: 100_000 * DECIMALS
y: 100_000 * DECIMALS

Alice (50x -> y)

invariant = (100_000 * DECIMALS) ** 2

new_x: (100_000 + 50) * DECIMALS
newy_y:

new_x * new_y = (100_000 * DECIMALS) ** 2
new_y = (100_000 * DECIMALS) ** 2 / new_x

out = 100_000 * DECIMALS - new_y

====
A: (50x -> 49)
B: (50x -> 52)
Arbitrage: 
Market Makers: 
"""

DECIMALS = 10 ** 9
X: int = 100_000 * DECIMALS
Y: int = 100_000 * DECIMALS
INVARIANT: int = X * Y

def x_to_y(x_amount: int) -> int:
  """
  It converts x into y.
  """
  global X
  global Y
  global INVARIANT
  new_x = X + x_amount
  new_y = INVARIANT // new_x

  out_tokens = Y - new_y
  X = new_x
  Y = new_y
  INVARIANT = X * Y
  return out_tokens

print(f"X: {X / DECIMALS} Y: {Y / DECIMALS}")

print('Alice exchange 50 x tokens in y.')
out_tokens = x_to_y(50 * DECIMALS)
print("Y Tokens she'll get: ", out_tokens / DECIMALS)
print(f"X: {X / DECIMALS} Y: {Y / DECIMALS}")

print('Bob exchange 50 x tokens in y.')
out_tokens = x_to_y(50 * DECIMALS)
print("Y Tokens Bob will get: ", out_tokens / DECIMALS)
print(f"X: {X / DECIMALS} Y: {Y / DECIMALS}")

print('Alice exchange 50 x tokens in y.')
out_tokens = x_to_y(50 * DECIMALS)
print("Y Tokens she'll get: ", out_tokens / DECIMALS)
print(f"X: {X / DECIMALS} Y: {Y / DECIMALS}")

"""
ERC20(x) -> ERC20(y)
\
  ETH -> (y)
"""