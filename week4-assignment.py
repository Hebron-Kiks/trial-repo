def file_handling(input_file, output_file):
    try:
        #reading file
        with open(input_file,"r") as file:
            content=file.read()
        
        #procceng the data to uppercase
        upper=content.upper()
        
        #writing into file
        with open(output_file, "w") as file:
            file.write(upper)
        print(f"success. Modified content has been written to '{output_file}'")
    except FileNotFoundError:
        print("File '{input_file}'was not found")
    except Exception as e:
        print(f"an error occurred: {e}")

input_file=input("Enter the name of input file: ")
output_file=input("Enter the name of output file: ")

#calling the function
file_handling(input_file, output_file)



    
    