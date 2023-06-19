# Run the command "bash gitpush.sh" to execute the script

git add .

echo 'Enter the commit message:'
read commitMessage

git commit -m "$commitMessage"

git push origin main

