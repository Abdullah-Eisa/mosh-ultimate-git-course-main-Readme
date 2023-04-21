import os

# Path to directory containing readme files
readme_dir =  "path/to/your/directory"

# Output file name
# output_file = "01 Getting Started combined_readme.md"
output_file = readme_dir+"\combined_readme.md"
# print(output_file)
# Create an empty string to store the combined readme contents
combined_readme = ""

# Iterate over all files in the directory
for file_name in os.listdir(readme_dir):
    # Check if the file is a readme file
    # print(file_name)
    if file_name.endswith(".md"):
        # Read in the contents of the file and add them to the combined readme string
        with open(os.path.join(readme_dir, file_name), "r") as f:
            combined_readme += f.read()
            
# Write the combined readme to a file
with open(output_file, "w") as f:
    f.write(combined_readme)
