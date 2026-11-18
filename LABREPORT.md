# Lab Report: Student Task Manager

**Name: Hamza Inayat**
**Reg. No.: SP23-BSE-120**
Course: CSC418 DevOps for Cloud Computing, Lab Assignment 4
Repository: hamzainayat20/StudentManager, public on GitHub

## 1. Git and GitHub, and add, commit and push

Git is a tool on my own computer. It keeps the history of my files, so I can see what changed, go back to an older version, and work in branches. GitHub is a website that stores a Git repository online, so other people can see it, review changes, and work on the same project.

`git add` puts a changed file into the next commit, which is like marking it ready to save. `git commit` saves that change in the local history with a short message saying what I did. `git push` sends those saved commits from my computer to GitHub, so the online copy has them too.

## 2. Branches and pull requests, and what causes merge conflicts

A branch is a separate line of work. I used one branch for each feature, so adding a task, completing a task and deleting a task were each built and tested on their own, without breaking the main code. A pull request asks for a branch to be merged into main, and it shows the changed files so the work can be checked before it is merged.

A merge conflict happens when two branches change the same line in the same file in different ways, and Git cannot tell which version to keep. In this assignment I made that happen on purpose in the README file. Both branches changed the project status line, so the second merge stopped and asked me to choose.

## 3. Fetch and pull, and merge and rebase

`git fetch` only downloads new work from GitHub. It does not change my files. `git pull` downloads the new work and also merges it into my current branch, so my files change.

`git merge` joins two branches and keeps both histories, with a merge commit that shows where they joined. `git rebase` moves my commits on top of the other branch instead, so the history looks like a straight line. Merge keeps the true history of when work was done, while rebase makes the history tidier but rewrites my commits.

## 4. GitHub Issues and Actions

GitHub Issues are a to do list for the project. Each issue describes one piece of work, has a label, and can be linked to the pull request that does the work. That makes it clear what is being done, and what is still open.

GitHub Actions runs work automatically. In this project it runs the unit tests every time code is pushed to main, and on every pull request to main. If a test fails, the run is red and the problem is seen before the code is merged. If the tests pass, the run is green.

## 5. One difficulty I faced, and how I solved it

The hardest part was the merge conflict. At first I was not sure which change to keep, because both branches had changed the same line and both looked right. I opened the file, read the conflict markers, and saw the two versions side by side. I kept the version from the first branch, `Project status: In Progress`, removed the markers, tested the app again, and then committed the resolved file. After that I checked `git log` and `git status` to make sure the merge was complete and no conflict was left.
