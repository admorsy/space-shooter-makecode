def on_button_pressed_a():
    player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global playerFire
    playerFire = game.create_sprite(player.get(LedSpriteProperty.X),
        player.get(LedSpriteProperty.Y))
    playerFire.set(LedSpriteProperty.BRIGHTNESS, 50)
    for index in range(4):
        playerFire.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
        if playerFire.is_touching(enemy):
            enemy.set(LedSpriteProperty.BRIGHTNESS, 250)
            for index2 in range(4):
                enemy.change(LedSpriteProperty.BRIGHTNESS, -50)
                basic.pause(50)
            enemy.delete()
            playerFire.delete()
            game.add_score(1)
    playerFire.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

enemyFire: game.LedSprite = None
playerFire: game.LedSprite = None
enemy: game.LedSprite = None
player: game.LedSprite = None
player = game.create_sprite(2, 4)
player.set(LedSpriteProperty.BRIGHTNESS, 150)
enemy = game.create_sprite(randint(0, 4), 0)
enemy.set(LedSpriteProperty.BRIGHTNESS, 150)
health = 3
game.set_life(health)
game.set_score(0)

def on_forever():
    global enemyFire, health, enemy, player
    if not (enemy.is_deleted()):
        enemy.move(1)
        basic.pause(500)
        enemy.if_on_edge_bounce()
        if enemy.get(LedSpriteProperty.X) == randint(0, 4):
            enemyFire = game.create_sprite(enemy.get(LedSpriteProperty.X),
                enemy.get(LedSpriteProperty.Y))
            enemyFire.set(LedSpriteProperty.BRIGHTNESS, 50)
            for index3 in range(4):
                if enemy.is_deleted():
                    enemyFire.set(LedSpriteProperty.Y, 0)
                    enemyFire.delete()
                    break
                enemyFire.change(LedSpriteProperty.Y, 1)
                basic.pause(200)
                if player.is_touching(enemyFire):
                    enemyFire.change(LedSpriteProperty.Y, 0)
                    player.set(LedSpriteProperty.BRIGHTNESS, 250)
                    for index4 in range(4):
                        player.change(LedSpriteProperty.BRIGHTNESS, -50)
                        basic.pause(50)
                    player.delete()
                    enemy.delete()
                    enemyFire.delete()
                    health = health - 1
                    basic.pause(200)
                    game.remove_life(1)
                    basic.pause(1000)
                    enemy = game.create_sprite(randint(0, 4), 0)
                    enemy.set(LedSpriteProperty.BRIGHTNESS, 150)
                    player = game.create_sprite(2, 4)
                    player.set(LedSpriteProperty.BRIGHTNESS, 150)
            enemyFire.delete()
    else:
        enemyFire.delete()
        basic.pause(500)
        enemy = game.create_sprite(randint(0, 4), 0)
        enemy.set(LedSpriteProperty.BRIGHTNESS, 150)
basic.forever(on_forever)
