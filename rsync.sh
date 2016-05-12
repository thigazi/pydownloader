#!/bin/bash
#rsync -z --update --delete-before -r --exclude=.* --exclude=*.pyc --exclude=dbx.fs --exclude=dbx.fs.* -avze ssh $PWD [2a02:d40:3:14::2]:/storage/PyProjects/bprojekte/
rsync -z --update --delete-before -r --exclude=.* --exclude=*.pyc -avze ssh $PWD [2a02:d40:3:14::2]:/storage/PyProjects/bprojekte/
