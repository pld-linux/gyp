#!/bin/sh
p=gyp
svn=http://$p.googlecode.com/svn/trunk
revno=$1

svn co $svn${revno:+@$revno} $p
tar -cjf $p-$(svnversion $p).tar.bz2 --exclude-vcs $p
../dropin $p-$(svnversion $p).tar.bz2
../md5 $p.spec
