## Basic Git Commands
Understanding the basic commands in Git is essential for tracking changes in your projects and collaborating with others. This section will guide you through creating and managing your repositories with some fundamental Git commands.

Creating a New Repository (init)
A repository (or “repo”) is where all the files for a particular project are stored, along with the revision history.

Open your terminal and navigate to the directory where you want to create a new repository.
Run the git init command: git init
This command creates a new subdirectory named .git that houses all of your repository’s configuration files and history. Your current directory is now a Git repository, ready to track project files.
Cloning an Existing Repository
Cloning is the process of creating a local copy of a remote repository.

Find the repository you wish to clone. This could be a project on GitHub or another Git server. Copy the repository’s URL.
In your terminal, navigate to the directory where you want to clone the repository.
Run the git clone command followed by the copied URL: git clone https://github.com/exampleuser/example-repo.git
This command copies all the data from the repository to your local machine, allowing you to work on the project.
Adding and Committing Changes
After making changes to your project, you’ll want to save these changes to your repository. This process involves two steps: adding changes and committing them.

Adding Changes
With changes made to your project files, open your terminal and navigate to your repository’s directory.
Run the git add command to stage changes for commit. To add a specific file: git add filename.txt Or, to add all changed files: git add .
Committing Changes
After adding your changes, it’s time to commit them. Use the git commit command with a message describing what you’ve done: git commit -m "Your commit message"
This command saves your staged changes along with a descriptive message, which helps others understand what you’ve done and why.
Viewing the Commit History (log)
To see the history of your commits, including what changes were made and by whom:

In your terminal, make sure you’re in your repository’s directory.
Run the git log command: git log
You’ll see a list of commits, each with an author, date, and message. For a more condensed view, try git log --oneline.
Conclusion
Congratulations! You’ve now learned how to create a new Git repository, clone an existing one, stage and commit changes, and view the commit history. These are the foundational skills you need to start tracking your projects with Git.