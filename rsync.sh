#!/bin/bash
rm app/*.pyc
rm libs/*.pyc
rm dbx/*.pyc
rsync -z --update --delete-before -r --exclude=.* --exclude=*.pyc --exclude=dbx/dbx.* --exclude=*.egg-info -avze ssh /c/Users/work4space/PyStuff/public/pydownloader tamer@138.201.227.75:/storage/PyProjects/public