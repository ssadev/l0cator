git status
echo "Uploading To GitHub"
git add .
echo -n "Write Commit For Push: "
read commitForGit
git commit -m $commitForGit
git push

echo "### - Your Code Uploaded To GitHub Successfully - ####"

echo "==== Upload To Heroku ====="

git add .
echo -n "Write Commit For Push: "
read commitForGit
git commit -m $commitForGit
git push heroku master