# SETUP GUIDE FOR LEGO HARRY POTTER 5-7
- --
## Required software
- An unmodified copy of the Steam or GOG release of Lego Harry Potter 5-7
  - Note this must be the original version, not the remastered version
- A copy of the APWorld (requires Archipelago version 0.6.7 or higher)
- Reloaded II Mod Loader [Link](https://reloaded-project.github.io/Reloaded-II/QuickStart)

## Optional Software
- DXWnd [Link](https://sourceforge.net/projects/dxwnd/)
- --
## First Time Setup 
- Install Reloaded II Mod Loader
- Add Lego Harry Potter 5-7 to Reloaded II either through setup or by clicking the + on the left.
  - Must use the exe found in the Steam or GOG Lego Harry Potter folder
- If you are using the Steam version, we will need to use the ASI loader (optional for GOG version) 
  - Under Lego Harry Potter 5-7, click Edit Application
  - Under "Advanced Tools & Options", make sure that "Don't Inject Loader" is enabled
    - Indicated by the red +
  - Click "Deploy ASI Loader" and then "Okay"
- Navigate to the "Mods" folder in wherever you installed Reloaded II
- Move the LHP2.Archi.Mod folder into the Reloaded II Mods folder
- --
## Connecting to a Multiworld
- In Reloaded II, select the LHP2 Archipelago Mod and click "Configure Mod"
- Fill out the Host IP, Port Number, Slot Name, and Password as applicable
- Ensure that the Archipelago Mod is enabled
  - Indicated by the red +
- Launch the game either in Reloaded II
  - If you are using ASI Loader, launching in DXWnd, Steam, or GOG will also work
- The game will attempt to connect to the server once the menu is loaded
- IT IS IMPORTANT THAT YOU WAIT ON THE MENU UNTIL IT IS CONNECTED
- Start a new game and enjoy
- --
## Shuffled Locations/Items
- Spells & Abilities
- Level Unlocks - except the bonus level
- Gold Bricks
- Students in Peril
- Red Bricks
- House Crest Pieces
- True Wizard
- Character Tokens
- Shop Purchases
- --
## Important Notes (Please Read)
- Known Bugs are included in our Logic File
- This APWorld is compatible with Universal Tracker and its /explain command
- The game has a different map for each year (i.e. there are 4 diagon alley maps).
  - As such, certain maps do not exist in certain years (i.e. the library does not have a Year 5 Map)
  - See the pinned logic spreadsheet in the discord channel for the complete listing of maps that do not exist
  - Logic does not expect you to enter these maps until you can logically reach that year
  - If you try to enter these maps early, you will be transported to Y8 and need to time travel back (see below)
- Time travelling is an important part of this archipelago. 
  - You can go forward or backwards in time to any year, but it requires you to reload your save file
  - You must complete DADA banned before being able to time travel
  - Logic currently expects you to be able to complete the previous year before going forward
  - To time travel, go to the Character Customization Room in Madam Malkins 
    - Walk through the loading zone behind the gold brick to get there
  - In this room, pause the game, and open up the Extras Menu
  - In the Extras Menu, open up the "Enter Code" Menu
  - Type in YEAR5, YEAR6, YEAR7, OR YEAR8 and hit A (or whatever your select button is)
  - Now, while still in the Character Customization Room, save the game
    - To do so, go into options and change any of the options (like volume)
  - Then quit to menu and reload your save file
  - The loading screen or pause menu will indicate if it worked properly
  - Please note that loading zones are not updated in the save file until after you visit that map in the new year
    - If you are going to quit the game in the new year, to avoid inadvertently time traveling, manually save the game before quitting
- As you may remember from the vanilla game, the tent in the wilderness changes locations after each level
  - I have removed the invisible walls preventing you from going over or around the barriers
  - However, you have to have visited the wilderness at least once before this works
  - After your first visit to the wilderness, return to the Character Customization Room and initiate a time travel
    - You don't actually have to reload your save file, just make sure the game is saved
  - Then you can return to the wilderness and the invisible walls should be gone