#! /usr/bin/env sh
wget https://gist.github.com/3099130ea46ae2367c9e307a78c3c71a.git
mv pre-commit-raw pre-commit
git init
mv pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
