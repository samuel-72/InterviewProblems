from typing import List

def product_except_self(nums: List[int]) -> List[int]:
  """
  nums: A list of integers
  return: A list where each element is the product of all the elements in the array except itself
  EG: Input: [1,2,3,4] Output: [24, 12, 8, 6]
  """
  n = len(nums)
  runner = 1
  op = []
  for elt in nums:
    op.append(runner)
    runner *= elt
  runner = 1
  for i in range(n-1, -1, -1):
    op[i] = runner * op[i]
    runner *= nums[i]
  print("Input : %s\nOutput : %s\n\n" % (nums, op))
  return op
  
  
def test_product_except_self(input, expected_output):
  assert product_except_self(input) == expected_output, "For Input %s the expected answer is %s" % (input, expected_output)


def main():
  product_except_self([1,2,3,4])
  test_product_except_self([1, 2, 3, 4], [24, 12, 8, 6])
  test_product_except_self([1, 2, 0, -1], [0, 0, -2, 0])
  test_product_except_self([1, 2, 0, 0], [0, 0, 0, 0])
  test_product_except_self([1, 2, -8, -1], [16, 8, -2, -16])
  
if __name__ == "__main__":
  main()
