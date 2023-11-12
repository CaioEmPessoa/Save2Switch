# Save2Switch
_A "save manager" that copies your save files from PC to your Switch and vice versa._

## What it does/not?
It acts like a save manager, where you can connect your switch to your PC and keep the same play trought both plataforms.

*I'm not messing with decoding saves yet, but I'll probably put more options to specific games that require more trouble to copy your saves.

<br>

## How it does it?
### Main Window
When you open the app for the first time this it what you'll see:

| White Theme | Dark Theme|
|-------------|-----------|
|![print of the app alone](https://github.com/CaioEmPessoa/Save2Switch/assets/127911795/37c01742-9126-4d52-a3ed-e90f6f4834c4) | ![print of the app alone](https://github.com/CaioEmPessoa/Save2Switch/assets/127911795/7ab5f1d7-4a46-4d26-bc7b-4de5eedfe7be))|

### Config Window
As the message says, you need to configure your switch's IP before adding a game, so this is the config window.
Besides the "IP" option I don't recommend messing with anything, because this things usually don't change, but if you need it, its there. 
The "edizon" save option wasn't fully tested, so as for now the app only works with JKSV.

| White Theme | Dark Theme |
|-------------|------------|
|![config window print](https://github.com/CaioEmPessoa/Save2Switch/assets/127911795/eb4a3a0c-d8ac-4b01-886b-17c75688c733) | ![config window print](https://github.com/CaioEmPessoa/Save2Switch/assets/127911795/271b6b4d-5978-4032-a420-cc433a9a4c0e)|

### Adding a save
So now that you configured your connection, you can add a game with the "+" button, that will open a window asking the following info:
- The name that will be displayed on the app
- The name of the game for JKSV or Title ID for edizon (that will be added later). To get this info simply go to your JKSV or EdiZon foulder's on any file explorer device.
- _Keep in mind that you can't misspell **anything**, even if its just a  capital/lower letter difference._
- The foulder you'll extract the save is the name of the backup foulder on JKSV, the name you choose before doing any backup, that usually are something like "profile - date @ hour", I recommend just for organizational purposes use "save2pc", since this is where you'll get your saves to copy to PC.
- The path to the PC save is simple enough, to know where your game keeps their save you can just search "_game_ save location"
- Then you can optionally add a icon to your games be more recognizable.
- _OBS: you can edit all this info later_

| White Theme | Dark Theme |
|-------------|------------|
|![new save window print](https://github.com/CaioEmPessoa/Save2Switch/assets/127911795/81de1658-4c36-4d4b-80d8-3940ab6e5a61) | ![new save window print](https://github.com/CaioEmPessoa/Save2Switch/assets/127911795/9fe0ba23-c630-4903-8a67-25d35fdbcfac) |


Then it will display your games like this:

| White Theme| Dark Theme |
|------------|-------------|
|![print of the app with games on it, white theme](https://github.com/CaioEmPessoa/Save2Switch/assets/127911795/e040aca3-fa6b-48cd-b188-784b7b13dcf6) | ![image](https://github.com/CaioEmPessoa/Save2Switch/assets/127911795/ed838f5a-88c4-4cb5-9e56-19015cde406f)|

And finally you can just click in "switch" or "pc" when you want to copy your files from one system to another!
- If you copied to switch you can just apply your save on JKSV
- If you copied to PC you can just go and play your game!

**And don't worry about losing saves, before copying the save files to PC, the app copies your save foulder to a "backups" one on the root of the app.**
**And JKSV automatically does a backup before applying your saves on switch**

