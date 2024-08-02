## After setup you need to clone any new repo with ssh key 

```md
## for example I cloned a new repo with my key referenced 
git clone git@sheyidev:sheyidev/Intro_to_DB.git

## How my key looks like on my computer 

```
```powershell
cd ssh/
ls

## content
config			id_ed25519_sheyidev	known_hosts.old
id_ed25519		id_ed25519_sheyidev.pub
id_ed25519.pub		known_hosts

```

```sh
//config file
# sheyijojo
Host sheyijojo
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519

# sheyidev
Host sheyidev
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_sheyidev


```

### Steps to Troubleshoot:

1. **Verify the SSH Agent is Running:**
   Ensure the SSH agent is running:
   ```sh
   eval "$(ssh-agent -s)"
   ```

2. **Add the New SSH Key to the SSH Agent:**
   Add your new SSH key to the SSH agent:
   ```sh
   ssh-add ~/.ssh/id_ed25519_another
   ```

3. **Check the SSH Key Configuration:**
   Make sure your `~/.ssh/config` file is correctly configured. It should look something like this:
   ```sh
   Host github-another
     HostName github.com
     User git
     IdentityFile ~/.ssh/id_ed25519_another
   ```

4. **Verify Your SSH Key is Added to GitHub:**
   Ensure the new SSH key has been added to your GitHub account:

   - Copy the contents of the new SSH key to the clipboard:
     ```sh
     cat ~/.ssh/id_ed25519_another.pub | clip
     ```
     (Use `pbcopy` on macOS or `xclip` on Linux if necessary.)

   - Go to **GitHub > Settings > SSH and GPG keys > New SSH key**, add the new key, and give it a title.

5. **Test the SSH Connection:**
   Test the SSH connection to GitHub using the new key:
   ```sh
   ssh -T git@github-another
   ```

   You should see a message like:
   ```sh
   Hi username! You've successfully authenticated, but GitHub does not provide shell access.
   ```

6. **Set the Correct Remote URL:**
   Ensure your repository is using the correct remote URL. For an existing repository, set the remote URL to use the `github-another` alias:
   ```sh
   git remote set-url origin git@github-another:username/repository.git
   ```

7. **Clone a Repository Using the New Key:**
   When cloning a new repository, use the `github-another` alias:
   ```sh
   git clone git@github-another:username/repository.git
   ```

### Summary
By following these steps, you should be able to troubleshoot and resolve the "Permission denied (publickey)" error. The key points are to ensure your SSH key is correctly added to the SSH agent, configured in your `~/.ssh/config` file, and added to your GitHub account. If the issue persists, double-check the spelling of file names and the configuration details.