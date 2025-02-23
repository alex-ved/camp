<b><p> Printing a shopping list from a text file. </p></b>

# How to Make a Pull Request (PR)

## Steps to Follow

1. **Clone the repository**

   ```sh
   git clone https://github.com/alex-ved/camp.git
   ```

2. **Create a new branch**

   ```sh
   git checkout -b <branch_name>
   ```

3. **Make changes to the desired file(s)**

4. **Add your changes to the staging area**

   ```sh
   git add <file_name>  # Add a specific file
   git add .             # Add all changes
   git add *.txt         # Add all text files
   ```

5. **Commit your changes**

   ```sh
   git commit -m "Your commit message"
   ```

6. **Push your branch to GitHub**

   ```sh
   git push origin <branch_name>
   ```

7. **Create a Pull Request (PR) on GitHub**
   - Go to your repository on GitHub
   - Navigate to the "Pull Requests" tab
   - Click "New Pull Request"
   - Select your branch and compare it with the main branch
   - Add a title and description for your PR
   - Click "Create Pull Request"
