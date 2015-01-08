#!/bin/bash

function usage()
{
	myname=`basename $0`
	cat <<-RTFM

	USAGE:
	  $myname <spec_file>
	
	$myname executes rpmbuild using a working directory one level up from
	the location of the .spec file, assuming the .spec files properly lives
	in a SPECS directory in a traditional rpmbuild directory structure.

	RTFM
}

if [ $# -ne 1 ]; then
	usage
	exit
elif [ ! -f $1 ]; then
	echo "ERROR: $1 not a regular file" >&2
	usage
	exit 1
fi

pushd "`dirname $1`/../" >/dev/null
wd="`pwd`"
popd >/dev/null

# Alternatively, you could define _topdir in ~/.rpmmacros
rpmbuild -bb --define "_topdir" "$wd" $1
