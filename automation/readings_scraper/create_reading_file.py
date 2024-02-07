import os

def create_reading_file(title, class_num, questions, readings, videos, bookmarks):
   
    folder_path = "../reading_assignments"
    file_name = f"reading{class_num}.md"
    file_path = os.path.join(folder_path, file_name)

    # Uncomment below to print debug information
    # print("file_path:", file_path)
    # print("title:", title)
    # print("questions:", questions)
    # print("readings:", readings)
    # print("videos:", videos)
    # print("bookmarks:", bookmarks)

    create_template(title, questions, readings, videos, bookmarks)


def create_template(title, questions, readings, videos, bookmarks):

    # Define the template
    template = f"""
# {title}

Description of the assignment

## Reading\n
{readings.strip()}

## Videos\n
{videos.strip()}

## Bookmark and Review\n
{bookmarks.strip()}

## Reading Questions\n
{questions.strip()}

## Things I want to know more about

>*Answer*
"""
    

    return print (template)
#     # Create the file
#     with open(file_path, "w") as file:
#         file.write(f"# {template}")
#     return 'File created successfully!'


# print(create_reading_file(title, questions))