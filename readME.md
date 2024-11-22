# Minecraft Hackathon Setup Guide

Welcome to the Minecraft Hackathon! This guide will help you set up Python to work with Minecraft. Follow these instructions carefully to ensure a smooth experience.

---

## Prerequisites: What You Need
1. **Minecraft PC Edition (Java or Bedrock)** installed on your computer.
2. **Java 11** installed to communicate with the Minecraft server.
   - Download here: [Adoptium Temurin Java 11](https://adoptium.net/temurin/releases/?version=11)
     - **x64**: 64-bit Windows
     - **arch64**: Mac M series
3. **GitHub Repository** to set up the Python server: [Pycraft Repository](https://github.com/thejacksonharding/pycraft)

**Note:** Everyone must set up a local server to test their code, but only the **team leader** will run the main server.

---

## Step 1: Install Minecraft Java Edition (Version 1.14.4)
1. Open the Minecraft Launcher.
2. Go to **Java Edition → Installations**.
   - Click **New Installation**.
   - Set the version to **1.14.4**.
   - Click **Create**.
3. In the **Play** tab, select **Version 1.14.4** in the bottom-left dropdown.
4. Click **PLAY** to start Minecraft.

---

## Step 2: Install Java 11
1. Check your current Java version:
   - Open a terminal and type: `java -version`
   - If not **11.x.x**, proceed to the next step.
2. Download Java 11: [Adoptium Temurin Java 11](https://adoptium.net/temurin/releases/?version=11).
3. Follow the installation instructions for your operating system.

---

## Step 3: Set Up the Minecraft Server
1. Download the GitHub repository: [Pycraft Repository](https://github.com/thejacksonharding/pycraft).
2. Extract the contents:
   - Extract **mcpi-main.zip**.
   - Extract **Jar files.zip**.
3. **Spigot Server Setup**:
   - Move `spigot-1.14.4.jar` to the `server` folder.

### Running the Server
**Windows**:
- Double-click `start.bat` in the `server` folder.
- If prompted, click **See More → Run Anyway**.

**Mac**:
- Double-click `start.command` in the `server` folder.
- If prompted, go to **System Settings → Privacy → Open Anyway**.

### Accept the EULA
1. Open `eula.txt` in the server folder.
2. Change `eula=false` to `eula=true`.
3. Save and close the file.

### Restart the Server
1. Run the server again:
   - **Windows**: Double-click `start.bat`.
   - **Mac**: Double-click `start.command`.
2. Let the server fully start.
3. Stop the server by typing `stop` into the terminal.

---

## Step 4: Install the Raspberry Juice Plugin
1. Move `raspberryjuice-1.12.1.jar` to the `plugins` folder in the `server`.
2. Restart the server again.

---

## Step 5: Connect to the Server
1. Open Minecraft.
2. Go to **Multiplayer → Add Server**.
   - Set the server name to **Python Craft**.
   - Set the server address to **localhost**.
3. Click **Join Server**.

---

## Step 6: Test Python Scripts
1. Open the `helloworld.py` script in your code editor.
2. Install the required Python library:
   ```bash
   pip install mcpi


Resources for Participants:
Github Repository: https://github.com/thejacksonharding/pycraft
VS code liveshare: https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare
Other Resources:
Template: https://ohsnapcoders.wixsite.com/mysite/escaperoom 
Building an escape room: https://www.youtube.com/watch?v=CAoEMV75H7c&ab_channel=Wato1876
API reference: https://www.stuffaboutcode.com/p/minecraft-api-reference.html
Ideas: https://mcpipy.wordpress.com/
Java MC edition help: https://help.minecraft.net/hc/en-us/articles/6657208607501-I-Own-Minecraft-Java-or-Bedrock-Edition-for-PC-How-Do-I-Get-the-Other
https://answers.microsoft.com/en-us/xbox/forum/all/how-do-i-get-minecraft-java-edition-on-pc-if-i/f77f03d8-da2d-4fb7-bffe-0f0e0bf5ca24
https://github.com/martinohanlon/minecraft-stuff -turtle
https://www.stuffaboutcode.com/2013/06/raspberry-pi-minecraft-sounds-effects.html - sound
Cheatsheet: https://arghbox.wordpress.com/wp-content/uploads/2013/06/table.pdf
https://arghbox.wordpress.com/wp-content/uploads/2013/06/teacheredition.pdf
https://arghbox.wordpress.com/wp-content/uploads/2013/06/minecraftbook.pdf
https://arghbox.wordpress.com/
COOL: https://www.stuffaboutcode.com/2013/11/minecraft-coding-traffic-jam.html
https://www.stuffaboutcode.com/2014/02/minecraft-music-visualiser.html
https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md - template!!
Other: https://nostarch.com/minecrafthelp
https://mrcote.info/blog/2024/06/10/how-to-get-started-with-learn-to-program-with-minecraft-in-2024/
https://github.com/martinohanlon/making-a-game-with-minecraft-pi/blob/master/worksheet.md
https://github.com/martinohanlon/minecraft-lavatrap/blob/master/lavatrap.png
https://github.com/martinohanlon/minecraft-demos
https://github.com/martinohanlon/minecraft-starwars
https://github.com/martinohanlon/minecraft-bridge
https://www.youtube.com/watch?v=-BP7DhHTU-I&ab_channel=sammyuri