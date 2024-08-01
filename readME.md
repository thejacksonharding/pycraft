1. Install java 11 (< java 13) openjdk adoptium version 11
2. Launch java 11 Copy code
* export JAVA_HOME=$(/usr/libexec/java_home -v 11) export PATH=$JAVA_HOME/bin:$PATH
3. Verify java -version
3a. (Only if not java 11) Edit start.command file in text edit and change v11 to vXX. Finally in terminal run chmod +x "file" 
4. naviagate to mcpi_server directory and execute mkdir spigot-build
5. cd spigot-build
6. curl -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
7. java -jar BuildTools.jar --rev 1.14.4
8. Move spigot-1.14.4.jar to server folder
9. Run start.command in the same terminal 
10. Agree to EUla (set false to true) and edit server.properties to the settings you want
11. Rerun start.command (let run fully)
12. type "stop"
13. Wait for terminal to stop
14. Download latest raspberryjuice file. "google raspberry juice github" -> jars -> download raspberryjuice-1.12.1.jar 
15. Move raspberryjuice jar into plugins folder
16. Move mcpi folder into Buildkit folder
17. Move helloworld.py into Buildkit folder
18. rerun start.command in the same terminal
19. Open Minecraft java edition
20. Open installation 1.14.4 -> Installations/new installation/ version 1.14.4/ play
21. Multiplayer
22. server name: Python Craft server address: localhost 
23. Join server
24. open helloworld.py 
25. run module 
26. Verify that helloworld ran in minecraft!
27. Have fun!


Make sure to brew install git 
and brew install openjdk

FOR WINDOWS
Make sure to click on the start.bat file. insetad of mac start.command.
Make
