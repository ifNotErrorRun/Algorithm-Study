#9498
def test_result(score):
  if 90 <= score <= 100:
    return "A"

  elif 80 <= score <= 89:
    return "B"

  elif 70 <= score <= 79:
    return "C"

  elif 60 <= score <= 69:
    return "D"

  else:
    return "F"

score = int(input())
print(test_result(score))