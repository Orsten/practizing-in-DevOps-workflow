#list of files
list = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
#where to merge file
merged_filename = "merged_file.txt"

#Open merged file 
with open(merged_filename, "w") as merged_file:
#Iterate over rhe files
 for file in list:
#open each file in read mode
  with open(file, "r") as f:
#write the contents of the file to the merged file
   merged_file.write(f.read() + "\n")

