from riddle import run_riddle

NUMBER_OF_TRIES = 100

# Hold results
counter = 0
succeeded = 0

# Run the riddle NUMBER_OF_TRIES times
for i in range(1, NUMBER_OF_TRIES+1):
  result = run_riddle(i)
  counter += 1
  if result:
    succeeded += 1

print("Succeed {} out of {}. That's {}%".format(succeeded, counter, (succeeded/counter)*100 ))