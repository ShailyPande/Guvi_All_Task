# Write a Python program using Function to which will do the following-
#a) The function will create a text file with the current timestamp.
#b) The file content should have the content of the current timestamp

from datetime import datetime

def write_current_timestamp_to_file():
    """
    write current timestamp to a file named 'timestamp.txt'

    """
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_name = "timestamp.txt"

    with open (file_name,'w') as file:
        file.write(f" Current timestamp: {current_timestamp}")

        print(f"Timestamp written to {file_name}")

write_current_timestamp_to_file()

#2 Write another Python function to read from a text file.The function will take the name of the text file
#and display the content of the file into the console.


def read_a_file(file_name):
    with open(file_name,'r') as file:
        content = file.read()
        print(f'The content in the file- {content}')


file_name = "testing_task_7.txt"
read_a_file(file_name)


