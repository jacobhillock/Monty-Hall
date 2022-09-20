import argparse
import random
import time

def args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(description='Description.')
  parser.add_argument('--auto', '-a', action='store_true', help='')
  parser.add_argument('--switch', '-s', action='store_true', help='')
  args = parser.parse_args()
  return args

def get_guess(options: list[int], auto: bool, prev: int=0) -> int:
  guess = 0
  if auto:
    new_options = list(filter(lambda o: o != prev, options))
    guess = random.choice(new_options)
  else: 
    while guess not in options:
      guess = int(input(f'Which door do you want? {", ".join([str(o) for o in options])}: '))
  
  return guess

def game(auto: bool, switch: bool=True) -> bool:
  number = 3
  options = [i + 1 for i in range(number)]
  win = random.choice(options)
  
  guess = get_guess(options, auto)

  remaining = list(filter(lambda o: o not in [win, guess], options))
  remove = random.choice(remaining)
  options = list(filter(lambda o: o != remove, options))

  guess = get_guess(options, auto, guess if switch else 0)

  return win == guess

def main() -> None:
  random.seed(time.time())
  arg = args()
  if arg.auto:
    total = 100000
    wins = 0
    for i in range(total):
      wins = wins + 1 if game(True, arg.switch) else wins
    print(wins/total)
  else:
    print('Winner!!' if game(False) else 'Loser!!')

if __name__ == '__main__':
  main()