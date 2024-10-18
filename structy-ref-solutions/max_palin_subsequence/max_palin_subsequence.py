# O
def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})
  
  
def _max_palin_subsequence(string, i, j, memo):
  key = (i, j)
  if key in memo:
    return memo[key]
  
  if i == j:
    return 1
  
  if i > j:
    return 0
  
  if string[i] == string[j]:
    memo[key] = 2 +_max_palin_subsequence(string, i + 1, j - 1, memo)
  else:
    memo[key] = max( 
      _max_palin_subsequence(string, i + 1, j, memo),
      _max_palin_subsequence(string, i, j - 1, memo)
    )
  
  return memo[key]
  
  
  
  
  
​
  
  
  
  
  
  
  
  
  
  
# O(n^2) time and O(n^2) space
# def max_palin_subsequence(string):
#   return _max_palin_subsequence(string, 0, len(string) - 1, {})
  
# def _max_palin_subsequence(string, start, end, memo):
#   key = (start, end)
#   if key in memo:
#     return memo[key]
  
#   if start == end:
#     return 1
  
#   if start > end:
#     return 0
​
#   if string[start] == string[end]:
#     start += 1
#     end -= 1
#     memo[key] = 2 + _max_palin_subsequence(string, start, end, memo)
#     return memo[key]
#   else: 
#     memo[key] = max(
#       _max_palin_subsequence(string, start + 1, end, memo), 
#       _max_palin_subsequence(string, start, end - 1, memo)
#     )
#     return memo[key]