#!/bin/bash
export JAVA_HOME=$(/usr/libexec/java_home -v 11)
export PATH=$JAVA_HOME/bin:$PATH

cd "$(dirname "$0")"
exec java -Xms2G -Xmx2G -jar spigot-1.14.4.jar nogui
