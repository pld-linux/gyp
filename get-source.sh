#!/bin/sh

set -e

git clone https://chromium.googlesource.com/external/gyp
cd gyp
version=$(grep version= setup.py|cut -d\' -f2)
revision=$(git log --oneline|head -1|cut -d' ' -f1)
tar -a --exclude-vcs -cf ../gyp-$version-git$revision.tar.xz *
cd ..

../dropin gyp-$version-git$revision.tar.xz

sed -i -e "
	s/^\(%define[ \t]\+gitrev[ \t]\+\)[0-9]\+\$/\1$revision/
" gyp.spec
../md5 gyp.spec
