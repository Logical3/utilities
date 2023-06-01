## Git Commands
### Creating a Branch from existing: 
```
git checkout -b <branch_name>
```
### Pushing a branch to remote:
```
git push -u origin <branch_name>
```
### Pulling latest change from remote branch to local branch
```
git fetch origin 
git merge origin/<branch_name>
```
### Remove local branches that are deleted from remote 
```
git remote prune origin
```
### Setting up upstream for a fork
```
git remote -v
git remote add upstream <remote_repo> 
git fetch upstream
git checkout <local_Branch>
git rebase upstream/<remote_branch>
```
### Rename local branch 
```
git branch -m old-name new-name
```
### Rename Remote branch
``` 
git push origin --delete old-name
git push origin -u new-name
```
### Discard local commits and pull from remote
```
git reset --hard origin/main
```
### Squash last 3 commits
```
git rebase -i HEAD~3
```