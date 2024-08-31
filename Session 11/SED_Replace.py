def sed(pattern, replacement, input_file, output_file):
    try:
        with open(input_file,'r') as file:
            content=file.read()
        updated_content=content.replace(pattern,replacement)
        with open(output_file,'w') as file:
            file.write(updated_content)
    except Exception as e:
        print(f"Error : {e}")
        exit(1)
sed('old_string','new_string','input.txt','output.txt')

# Output
# Hello world!
# This is a python file