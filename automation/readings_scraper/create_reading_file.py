import os

def create_reading_file(title, class_num, questions, readings, videos, bookmarks):
   
    folder_path = "../reading_assignments"
    file_name = f"reading{class_num}.md"
    file_path = os.path.join(folder_path,"/",file_name)

    print("file_path:", file_path)
    print("title:", title)
    print("questions:", questions)
    print("readings:", readings)
    print("videos:", videos)
    print("bookmarks:", bookmarks)


    for question in questions:
        question_print = print(f"### {question}\n>*Answer*\n")

    for reading in readings:
        f"### {reading}\n\n"

    for video in videos:
        f"### {video}\n\n"

    for bookmark in bookmarks:
        f"### {bookmark}\n\n"

    create_template (title, question_print, readings, videos, bookmarks)


def create_template(title, question_print, readings, videos, bookmarks):

        # Define the template
    template = f"""
    # {title}

    Description of the assignment

    ## Reading
    {readings}
    
    ## Videos
    {videos}

    ## Bookmark and Review
    {bookmarks}
    
    ## Reading Questions
    {question_print}

    ## Things I want to know more about

    >*Answer*
    """
    
    return print (template)
#     # Create the file
#     with open(file_path, "w") as file:
#         file.write(f"# {template}")
#     return 'File created successfully!'


# print(create_reading_file(title, questions))