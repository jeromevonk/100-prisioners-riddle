
from sequence import get_random_sequence



def find_loops(sequence):
  # Get the length
  n = len(sequence)

  # Create a list with n items, from 0 to n-1 (attention, second parameter of range is non-inclusive)
  remaining_indexes = [i for i in range(0, n)]
  loops = []

  while len(remaining_indexes) > 0:
    # Create a new loop
    completed = False
    loop = []
    
    # Start the loop
    starter = remaining_indexes[0]
    index = starter

    while completed == False:
      # Append to loop
      loop.append(index)

      # Remove from 'remaining'
      remaining_indexes.remove(index)

      # Get the next number
      index = sequence[index]


      # Check for a completed loop
      if index == starter:
        completed = True
      
    # Add loop to list
    loops.append(loop)

  return loops

def get_greatest_loop_length(loops):
  max_length = 0
  
  for loop in loops:
    loop_len = len(loop)
    if loop_len > max_length:
      max_length = loop_len

  return max_length

def run_riddle(i):
  # Get the sequence
  #sequence = [18,5,31,2,22,43,51,94,3,88,68,35,30,17,53,11,15,37,24,8,75,66,81,55,74,98,40,6,45,85,38,20,84,96,54,72,50,42,59,33,25,60,46,1,9,19,69,76,82,86,67,16,97,10,90,29,61,32,77,4,64,79,52,63,87,80,34,41,93,28,78,14,95,62,65,49,0,23,27,7,26,92,58,44,57,13,83,99,39,12,73,36,48,71,56,21,91,70,47,89]
  sequence = get_random_sequence()

  # Look for the loops
  loops = find_loops(sequence)

  # Print results
  max_length = get_greatest_loop_length(loops)

  print("Riddle #{}, {} loops, max length is: {}".format(i, len(loops), max_length))

  return max_length < 51
