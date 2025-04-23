

# Introduction to Git and GitHub Tutorial for High School Students [Yousef]

This tutorial introduces high school students to Git and GitHub, focusing on basic version control concepts and collaboration. It’s designed to be simple, hands-on, and engaging for beginners.

## Learning Objectives
By the end of this tutorial, students will be able to:
1. Understand what Git is and why version control is useful.
2. Create a GitHub account and set up a repository.
3. Perform basic Git commands (init, add, commit, push, pull).
4. Collaborate with others by cloning a repository and submitting changes.
5. Resolve simple merge conflicts during collaboration.

## Tutorial Outline

### 1. What is Git and Why Use It? (10 minutes)
- **Explain Git**: Git is a tool that tracks changes in your code or files, like a "save history" for your projects.
- **Why Use Git?**: 
  - Save different versions of your work.
  - Collaborate with others without overwriting their changes.
  - Recover old versions if something goes wrong.
- **What is GitHub?**: A website where you store Git repositories online to share and collaborate.
- **Activity**: Show a simple example of a project with multiple versions (e.g., a text file edited by two people).

### 2. Setting Up Git and GitHub (15 minutes)
- **Step 1: Install Git**
  - Download and install Git from [git-scm.com](https://git-scm.com/).
  - Verify installation: Open a terminal (or Command Prompt) and type `git --version`.
- **Step 2: Create a GitHub Account**
  - Go to [github.com](https://github.com) and sign up for a free account.
- **Step 3: Configure Git**
  - Set up your name and email in Git:
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```
- **Activity**: Have students install Git, create a GitHub account, and configure their Git settings.

### 3. Creating Your First Repository (15 minutes)
- **Step 1: Create a Repository on GitHub**
  - On GitHub, click “New Repository,” name it `my-first-repo`, and make it public.
  - Add a README file and create the repository.
- **Step 2: Clone the Repository**
  - Copy the repository URL (e.g., `https://github.com/username/my-first-repo.git`).
  - In the terminal, navigate to a folder and run:
    ```bash
    git clone <repository-url>
    ```
- **Step 3: Make Changes and Commit**
  - Open the cloned folder, edit the README.md file (e.g., add “Hello, this is my first Git project!”).
  - In the terminal, run:
    ```bash
    git add README.md
    git commit -m "Update README with a greeting"
    git push origin main
    ```
- **Activity**: Students create a repository, clone it, make a change, and push it to GitHub.

### 4. Collaborating with Others (20 minutes)
- **Step 1: Add a Collaborator**
  - On GitHub, go to your repository’s “Settings” > “Collaborators” and invite a classmate by their GitHub username.
- **Step 2: Clone and Edit as a Collaborator**
  - The collaborator clones the repository using `git clone <url>`.
  - They edit a file (e.g., add their name to a CONTRIBUTORS.txt file) and push their changes:
    ```bash
    git add CONTRIBUTORS.txt
    git commit -m "Add my name to contributors"
    git push origin main
    ```
- **Step 3: Pull Changes**
  - The original owner pulls the collaborator’s changes:
    ```bash
    git pull origin main
    ```
- **Activity**: Pair students up. Each student invites their partner as a collaborator, makes changes, and pulls their partner’s changes.

### 5. Handling Merge Conflicts (10 minutes)
- **What is a Merge Conflict?**: When two people edit the same part of a file, Git needs help to decide which changes to keep.
- **Example**:
  - Both students edit the same line in README.md and push their changes.
  - The second push will fail, and Git will show a conflict.
  - Resolve it by editing the file to combine both changes, then:
    ```bash
    git add README.md
    git commit -m "Resolve merge conflict"
    git push origin main
    ```
- **Activity**: Simulate a merge conflict by having both students edit the same line in a file, then guide them through resolving it.

### 6. Wrap-Up and Q&A (10 minutes)
- Recap key commands: `git clone`, `git add`, `git commit`, `git push`, `git pull`.
- Discuss real-world uses (e.g., group projects, open-source contributions).
- Answer student questions.

## Homework Assignments
1. **Create a Personal Repository**:
   - Create a new GitHub repository called `my-todo-list`.
   - Add a README.md file with a simple to-do list (e.g., “Buy groceries, Do homework”).
   - Commit and push the changes to GitHub.
   - Submit the repository URL to the teacher.
2. **Collaborate on a Group Repository**:
   - In groups of 2–3, create a shared repository.
   - Each student adds their name to a CONTRIBUTORS.txt file and pushes their changes.
   - Pull the group’s changes and resolve any conflicts.
   - Submit the repository URL and a screenshot of the CONTRIBUTORS.txt file.
3. **Explore GitHub**:
   - Find one open-source project on GitHub (e.g., a game or simple app).
   - Write a short paragraph (3–5 sentences) about what the project does and why it’s interesting.
   - Submit the paragraph and the project’s GitHub URL.

## Tips for Teachers
- Use a projector to demonstrate Git commands live.
- Encourage students to ask questions during hands-on activities.
- Provide a cheat sheet with basic Git commands:
  ```bash
  git clone <url>          # Copy a repository to your computer
  git add <file>           # Stage changes for commit
  git commit -m "message"  # Save changes with a message
  git push origin main     # Upload changes to GitHub
  git pull origin main     # Download changes from GitHub
  ```
- Keep the pace slow and check for understanding, as Git can be intimidating for beginners.

