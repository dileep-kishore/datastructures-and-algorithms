'''Reading lines from text'''
ROSALIND = open("/home/dileep/7th sem/data structures and algos/assignment0/compute_MWt.py", "r")
NUM_LINES = sum(1 for line in ROSALIND)
LINES = [dummy for dummy in range(NUM_LINES) if dummy%2 == 0]
RESULT = ''
for dummy2 in LINES:
    ROSALIND.seek(0, 0)
    RESULT += ROSALIND.readlines()[dummy2]
print(RESULT)
ROSALIND.close()
