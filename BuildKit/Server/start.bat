@echo off
REM Set JAVA_HOME to Java 11 if not already set
SET "JAVA_HOME=C:\Program Files\Java\jdk-11"
SET "PATH=%JAVA_HOME%\bin;%PATH%"

REM Print Java version for verification
java -version

REM Navigate to the script's directory
cd "%~dp0"

REM Start the Spigot server
java -Xms2G -Xmx2G -jar spigot-1.14.4.jar nogui
pause
