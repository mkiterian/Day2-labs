def fizz_buzz(number):
  msg = 'FizzBuzz'
  if isinstance(number, int):
    if number % 3 == 0 and number % 5 != 0:
      return msg[0:4]
    elif number % 5 == 0 and number % 3 != 0:
      return msg[4:]
    elif number % 3 == 0 and number % 5 == 0:
      return msg
    else:
      return number