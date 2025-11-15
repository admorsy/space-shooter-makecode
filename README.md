
> Open this page at [https://admorsy.github.io/space-shooter-makecode/](https://admorsy.github.io/space-shooter-makecode/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/admorsy/space-shooter-makecode** and import

## Edit this project

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/admorsy/space-shooter-makecode** and click import

### Game Objects

The game uses six main variables/objects:

-   player

-   playerFire (projectile fired upward from the player)

-   enemy

-   enemyFire (projectile fired downward from enemy)

-   score

-   life

### Game Mechanics (Algorithm)

### Player Behavior

-   player remains at y=4.

-   Press A → move player left (x--1, limited to 0).

-   Press B → move player right (x+1, limited to 4).

-   player can fire a projectile:

-   Create playerFire at the same x as player, y=4.

-   playerFire moves upward (y=4→0).

-   If playerFire hits enemy → destroy playerFire, score += 1.

-   If playerFire reaches y=0 without hit → delete.

### Enemy Behavior

-   enemy stays at y=0.

-   Moves automatically left/right:

-   Reverse direction when x reaches 0 or 4.

-   enemy fires enemyFire at random intervals:

-   Created at the same x as enemy, y=0.

-   Moves downward (y=0→4).

-   If enemyFire hits player → life -= 1.

-   If enemyFire reaches y=4 without hit → delete.

### Game Over Logic

-   When life = 0:

-   Stop all game loops.

-   Scroll "GAME OVER" letter-by-letter.

-   Scroll "SCORE", followed by numeric score.

### Project Setup

Note: the instructions or steps in italic are optional and only added for better visuals. Students can skip them without affecting the function of the code.

Ask students to create a new project with a unique name they choose.

#### Initializing the game variables (except playFire, and enemyFire):

-   Create a player sprite (variable) at (x=2, y=4)
-   Set brightness to 150
```blocks
let player = game.createSprite(2, 4);
player.set(LedSpriteProperty.Brightness, 150)
```

-   Create an enemy sprite (variable) at a random x on the top row (y=0)
-   Set brightness to 150

```blocks
let enemy = game.createSprite(randint(0, 4), 0)
enemy.set(LedSpriteProperty.Brightness, 150)
```

-   Create a variable called health
-   initialize its value to 3
-   Store that variable inside the built-in life variable

```blocks
let health = 3
game.setLife(health)
```
-   Finally set the score built-in variable to 0

```blocks
game.setScore(0)
```
- When you're done with this part, your onStart loop should look like this:

```blocks
let player = game.createSprite(2, 4);
player.set(LedSpriteProperty.Brightness, 150)
let enemy = game.createSprite(randint(0, 4), 0)
enemy.set(LedSpriteProperty.Brightness, 150)
let health = 3
game.setLife(health)
game.setScore(0)
```

Part 3: Player movement + shooting behavior
-------------------------------------------

### Button A → Move Left

-   On button A pressed:

-   Change player's x by --1 (move left)

### Button B → Move Right

-   On button B pressed:

-   Change player's x by +1 (move right)

(Use conditional blocks if you want to prevent going off-grid.)

### When A+B is pressed:

1.  Create playerFire sprite at:

-   x = player's x

-   y = player's y (4)

3.  Dim the projectile brightness to 50

4.  Repeat 4 times:

-   Move playerFire up (change y by --1)

-   Pause 100 ms

-   If playerFire touches enemy:

-   Flash enemy by increasing then decreasing brightness

-   Delete enemy

-   Delete playerFire

-   Add 1 to score

6.  After the loop, delete any remaining playerFire

Part 4: Enemy movement + shooting behavior
------------------------------------------

### Inside a forever block:

-   If enemy is not deleted (i.e. if it exists):

-   Move enemy by 1 step

-   Pause 500 ms

-   Bounce enemy when reaching LED grid edge

### Random Enemy Firing:

-   If enemy's current x equals a random number (0--4):

-   Create enemyFire at enemy's x and y

-   Dim brightness to 50

-   Repeat 4 times:

-   Move enemyFire downward (change y by +1)

-   Pause 200 ms

-   If enemyFire touches player:

-   Flash player

-   Delete player, enemy, and enemyFire

-   Decrease life by 1

-   Respawn both player and enemy in their starting positions

-   Delete enemyFire after loop ends

### If Enemy Was Deleted Earlier (doesn't exist):

-   Pause 500 ms

-   Respawn enemy at random x and brightness 150

Part 5: Score and health system + game over

### Score:

-   Increases by +1 when playerFire hits enemy.

### Life:

-   Starts at 3.

-   Decreases by --1 when enemyFire hits player.

-   When life reaches 0:

-   Stop gameplay

-   Scroll "GAME OVER"

-   Scroll "SCORE", then the final number




#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
