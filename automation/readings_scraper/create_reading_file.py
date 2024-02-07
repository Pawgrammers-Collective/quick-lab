def create_reading_file(class_num, title, questions):
    
    folder_path = "../reading_assignments/file_name"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the file
    with open(file_path, "w") as file:
        file.write(f"# {title}\n\n {questions}")