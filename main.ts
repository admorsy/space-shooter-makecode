input.onButtonPressed(Button.A, function () {
    player.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    playerFire = game.createSprite(player.get(LedSpriteProperty.X), player.get(LedSpriteProperty.Y))
    playerFire.set(LedSpriteProperty.Brightness, 50)
    for (let index = 0; index < 4; index++) {
        playerFire.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
        if (playerFire.isTouching(enemy)) {
            enemy.set(LedSpriteProperty.Brightness, 250)
            for (let index = 0; index < 4; index++) {
                enemy.change(LedSpriteProperty.Brightness, -50)
                basic.pause(50)
            }
            enemy.delete()
            playerFire.delete()
            game.addScore(1)
        }
    }
    playerFire.delete()
})
input.onButtonPressed(Button.B, function () {
    player.change(LedSpriteProperty.X, 1)
})
let enemyFire: game.LedSprite = null
let playerFire: game.LedSprite = null
let enemy: game.LedSprite = null
let player: game.LedSprite = null
player = game.createSprite(2, 4)
player.set(LedSpriteProperty.Brightness, 150)
enemy = game.createSprite(randint(0, 4), 0)
enemy.set(LedSpriteProperty.Brightness, 150)
let health = 3
game.setLife(health)
game.setScore(0)
basic.forever(function () {
    if (!(enemy.isDeleted())) {
        enemy.move(1)
        basic.pause(500)
        enemy.ifOnEdgeBounce()
        if (enemy.get(LedSpriteProperty.X) == randint(0, 4)) {
            enemyFire = game.createSprite(enemy.get(LedSpriteProperty.X), enemy.get(LedSpriteProperty.Y))
            enemyFire.set(LedSpriteProperty.Brightness, 50)
            for (let index = 0; index < 4; index++) {
                if (enemy.isDeleted()) {
                    enemyFire.set(LedSpriteProperty.Y, 0)
                    enemyFire.delete()
                    break;
                }
                enemyFire.change(LedSpriteProperty.Y, 1)
                basic.pause(200)
                if (player.isTouching(enemyFire)) {
                    enemyFire.change(LedSpriteProperty.Y, 0)
                    player.set(LedSpriteProperty.Brightness, 250)
                    for (let index = 0; index < 4; index++) {
                        player.change(LedSpriteProperty.Brightness, -50)
                        basic.pause(50)
                    }
                    player.delete()
                    enemy.delete()
                    enemyFire.delete()
                    health = health - 1
                    basic.pause(200)
                    game.removeLife(1)
                    basic.pause(1000)
                    enemy = game.createSprite(randint(0, 4), 0)
                    enemy.set(LedSpriteProperty.Brightness, 150)
                    player = game.createSprite(2, 4)
                    player.set(LedSpriteProperty.Brightness, 150)
                }
            }
            enemyFire.delete()
        }
    } else {
        enemyFire.delete()
        basic.pause(500)
        enemy = game.createSprite(randint(0, 4), 0)
        enemy.set(LedSpriteProperty.Brightness, 150)
    }
})
