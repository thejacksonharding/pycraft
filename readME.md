# Hackathon Setup Guide

## Prerequisites

Before you start, make sure you have the following:

- **Java 11 (Adoptium OpenJDK version 11)**: This will only work if you set your default java version to java 11!
- **Minecraft: Java Edition**
- **Minecraft Pi (mcpi) and RaspberryJuice Plugin + Spigot Server jar file (located in github repository)**
- **pip install mcpi**

## Steps to Set Up the Server and Python Integration

### 1. Install Java 11 (Adoptium OpenJDK version 11)
- Download and install Java 11 from [Adoptium](https://adoptium.net/temurin/releases/?version=11/).

### 2. Extract Minecraft Pi (mcpi)
- Download Zip Files from GitHub Repository or Clone Repository to your Desktop
- Extract the **mcpi** folder from the download package.

### 3. Set Up the Spigot Server
- Extract the **JAR** files from the Spigot server package.
- Move `spigot.jar` to the **server folder**.

### 4. Run the Server
- **Windows**:
  - Double-click `start.bat` to run the server.
  - If prompted, click *See More* and then *Run Anyway*.
- **Mac**:
  - Double-click `start.command` to run the server.
  - If prompted, go to *System Settings → Privacy → Open Anyway* at the bottom of the settings.

### 5. Accept the EULA
- Open the `Eula.txt` file in a text editor.
- Change `eula=false` to `eula=true`, then save the file.

### 6. Restart the Server
- Rerun the `start.command` file and let it run fully.

### 7. Stop the Server
- Once the server starts, type `stop` in the terminal and wait for the server to shut down completely.

### 8. Install RaspberryJuice Plugin
- Move the `raspberryjuice.jar` file into the **server → plugins** folder.

### 9. Restart the Server Again
- Rerun the `start.command` or `start.bat` to restart the server with the RaspberryJuice plugin.

### 10. Set Up Minecraft Java Edition
- Open **Minecraft: Java Edition** and select **version 1.14.4**.
- Go to *Installations → New Installation → Version 1.14.4 → Play*.

### 11. Connect to the Server
- In Minecraft, go to *Multiplayer → Add Server*.
- Set the server name as **Python Craft** and the server address as `localhost`.
- Click *Join Server*.

### 12. Run a Python Script in Minecraft
- Open the `helloworld.py` script in your code editor.
- Run the Python module.
- Verify that the script runs successfully in Minecraft!
- Try out the Example python file (give @a stone_sword in terminal) then run program
- Move on to working on your escaperoom.py!

---

**Enjoy the hackathon, and have fun!**

