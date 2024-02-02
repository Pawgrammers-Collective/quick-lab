# Software Requirements

## Vision

```
Minimum Length: 3-5 sentences
What is the vision of this product?
What pain point does this project solve?
Why should we care about your product?
```

1. What is the vision of this product?
   - Our vision is to develop an intelligent, user-friendly system that streamlines the setup process for lab assignments, ensuring that students can focus on learning rather than the intricacies of environment configuration. By automating the environment setup, we aim to create a seamless, error-free process that adapts to various operating systems and Python versions, guaranteeing that every participant starts from a standardized, fully-prepared platform. This project will not only enhance the efficiency and accessibility of labs but also foster a more inclusive and engaging learning experience by removing technical barriers and allowing students to dive straight into coding.
2. What pain point does this project solve?
   - The automated setup for Python labs significantly cuts down the time students spend on manual configurations, ensures a consistent coding environment across various systems, and shifts the focus from technical setup to the core learning of Python. This approach eliminates the technical hurdles and disparities, making coding more accessible and enjoyable for everyone involved. It democratizes the learning process, allowing students to dive straight into coding with a solid, uniform foundation.
3. Why should we care about your product?
   - We’re streamlining the lab assignment process by automating the setup.

## Scope (In/Out)

```
- IN - What will your product do
- Describe the individual features that your product will do.
- High overview of each. Only need to list 4-5
- Example:
  - The web app will provide information to the users about all the different Cat Cafe’s in the area
  - The web app will provide both walking and driving directions to each of the destinations
  - Users will be able to “Star” their favorite shops.
  - Each shop will contain reviews of the customer’s experiences
- OUT - What will your product not do.
  - These should be features that you will make very clear from the beginning that you will not do during development. These should be limited and very few. Pick your battles wisely. This should only be 1 or 2 things. Example: My website will never turn into an IOS or Android app.
```

- IN: What will your product do

  - Will create and initialize a local repo in desired directory
  - Will automatically install/activate Virtual environment to directory
  - Will add a .gitignore
  - Will create empty remote repo with same name
  - Will add remote origin to Github Repo

- OUT: What will your product not do.
  - This app will not automate the actual lab work

### Minimum Viable Product vs

1. What will your MVP functionality be?
   - Given a name, at least makes a readme, creates files and folders locally, makes venv.

### Stretch Goals

1. What stretch goals are you going to aim for?
   - Will create local and remote repositories
   - Will added README template to README.md
   - Will link remote and local repos, create first commit and push
   - Will `pip freeze > requirements.txt`

## Functional Requirements

List the functionality of your product. This will consist of tasks such as the following:

1. A user can copy the script down from our Organization’s GitHub Repository
2. User will be able to run script command in terminal to run script

### Data Flow

> Describe the flow of data in your application. Write out what happens from the time the user begins using the app to the time the user is done with the app. Think about the “Happy Path” of the application. Describe through visuals and text what requests are made, and what data is processed, in addition to any other details about how the user moves through the site.

1. Prompt for repo name
2. Ensure user is logged into GitHub on browser
3. Prompt user for OS
4. Script will proceed to create repos, directories, and required files

## Non-Functional Requirements (301 & 401 only)

> Non-functional requirements are requirements that are not directly related to the functionality of the application but still important to the app.
> Examples include:
> Security
> Usability
> Testability
> etc….
> Pick 2 non-functional requirements and describe their functionality in your application.
> If you are stuck on what non-functional requirements are, do a quick online search and do some research. Write a minimum of 3-5 sentences to describe how the non-functional requirements fits into your app.
> You MUST describe what the non-functional requirement is and how it will be implemented. Simply saying “Our project will be testable for testibility” is NOT acceptable.
> Tell us how, why, and what.

1. Security:

- User GitHub information will not be stored anywhere
- How it will be implemented: For enhanced security and user privacy, we won’t store Github information in our app. Instead, we’ll use GitHub’s secure authentication process, allowing users to log in directly with Github to verify their identity.

2. Usability:

- The user interface should be intuitive and user-friendly.
- How it will be implemented: Clear instructions guide users, and regular testing gathers feedback for continuous improvements. This ensures the app is accessible and enjoyable for users with varying technical backgrounds.
