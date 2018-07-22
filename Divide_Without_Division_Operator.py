def get_quotient(dividend, divisor):
  """
  Takes as input a dividend and divisor and returns the quotient
  """
  if not dividend:
    print("Dividend needs to be provided.")
    return None
  if not divisor:
    print("Divisor needs to be provided.")
    return None
  sign = -1 if (dividend < 0) ^ (divisor < 0) else 1  
  current = quotient = 0
  # Think about long division, we try to find numbers smaller than the dividend
  # 
  for i in range(31,-1,-1):
    if current + (divisor << i) <= dividend:
      current += (divisor << i)
      quotient = quotient | 1 << i
  return quotient
  
  def test_get_quotient():
    assert(get_quotient(11438461287,3132976) == 3650)
    assert(get_quotient(100,3) == 33)
    
  if __name__ == "__main__":
    test_get_quotient()
