

In order to make this bot working, follow this steps :

  1 - Create a "Videos" folder at the root level


GIT HUB 

1. Setup and Initial Check
Ensure Git is installed: git --version.
Configure user information if not already done:
bash
Copy code
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
Navigate to the project directory in the terminal.
Check the current status and branch: git status.
2. Pull Latest Changes from the Main Branch
Before creating a new branch, it's good practice to ensure you're working with the most up-to-date version of the main branch (often main or master).

Switch to the main branch: git checkout main.
Pull the latest changes: git pull.
3. Create a New Branch
Create a new branch off the main branch for your feature or fix. Replace feature-branch with a descriptive name for your branch.

git checkout -b feature-branch.
4. Make Changes and Commit
With your new branch checked out, you can start making changes to the code.

After making changes, check which files have been modified: git status.
Add files to be committed: git add . (to add all changes) or git add path/to/file (to add specific files).
Commit your changes: git commit -m "A descriptive message about your changes".
5. Push Changes to the Remote Repository
After committing your changes locally, you need to push them to the remote repository.

Push your branch and changes: git push -u origin feature-branch.
6. Create a Pull Request (PR)
To merge your changes into the main branch, you need to create a pull request.

Go to the repository on GitHub/GitLab/Bitbucket in your web browser.
You’ll likely see a prompt to create a pull request for your newly pushed branch. Click on "Compare & pull request" or navigate to the "Pull Requests" tab and click "New pull request".
Select your feature-branch as the "compare" branch and the main branch (e.g., main or master) as the "base" branch.
Fill in the PR title and description. Clearly describe the changes and any specific instructions or questions for reviewers.
Click "Create pull request".
7. Review and Merge
Wait for code reviews and any required checks (CI/CD, code quality, etc.) to pass.
Address any comments or requested changes from reviewers.
Once the pull request is approved and all checks pass, it can be merged into the main branch. This is often done through the UI of GitHub/GitLab/Bitbucket. Some projects may require squashing commits or rebasing before merging.
8. Cleanup
After merging, it’s a good practice to delete the feature branch from the remote repository (there's usually a button in the UI after merging) and switch back to the main branch locally:

git checkout main.
Pull the latest changes: git pull.
Delete the local branch if desired: git branch -d feature-branch.
