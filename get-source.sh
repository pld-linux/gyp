#!/bin/sh
p=gyp
svn=http://$p.googlecode.com/svn/trunk
revno=$1
specfile=$p.spec

set -e
svn co $svn${revno:+@$revno} $p
svnrev=$(svnversion $p)
tar -cjf $p-$svnrev.tar.bz2 --exclude-vcs --exclude=gyp/test/* $p
../dropin $p-$svnrev.tar.bz2

sed -i -e "
	s/^\(%define[ \t]\+svnrev[ \t]\+\)[0-9]\+\$/\1$svnrev/
" $specfile
../md5 $p.spec
