#loop that execute 5 times
for i in range(1,6):
#str variable 'filename'
 filename = f"file{i}.txt"
#create a new file that cpecified in 'write mode'
 with open(filename, "w") as f:
#writes str in each created file
  f.write(f"This is file {i}.")

