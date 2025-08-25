@namespace
class SpriteKind:
    Storage = SpriteKind.create()

def on_up_pressed():
    mySprite.set_image(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f e e e e f f . . . .
        . . . f e e e f f e e e f . . .
        . . f f f f f 2 2 f f f f f . .
        . . f f e 2 e 2 2 e 2 e f f . .
        . . f e 2 f 2 f f 2 f 2 e f . .
        . . f f f 2 2 e e 2 2 f f f . .
        . f f e f 2 f e e f 2 f e f f .
        . f e e f f e e e e f e e e f .
        . . f e e e e e e e e e e f . .
        . . . f e e e e e e e e f . . .
        . . e 4 f f f f f f f f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_left_pressed():
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . .
        . . . . . f f f f f f . . . . .
        . . . . f 2 f e e e e f f . . .
        . . . f 2 2 2 f e e e e f f . .
        . . . f e e e e f f e e e f . .
        . . f e 2 2 2 2 e e f f f f . .
        . . f 2 e f f f f 2 2 2 e f . .
        . . f f f e e e f f f f f f f .
        . . f e e 4 4 f b e 4 4 e f f .
        . . . f e d d f 1 4 d 4 e e f .
        . . . . f d d d e e e e e f . .
        . . . . f e 4 e d d 4 f . . . .
        . . . . f 2 2 e d d e f . . . .
        . . . f f 5 5 f e e f f f . . .
        . . . f f f f f f f f f f . . .
        . . . . f f f . . . f f . . . .
        """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def level2():
    global level
    tiles.set_current_tilemap(tilemap("""
        level2
        """))
    level = 2
    mySprite.set_position(31, 22)

def on_right_pressed():
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . .
        . . . . . f f f f f f . . . . .
        . . . f f e e e e f 2 f . . . .
        . . f f e e e e f 2 2 2 f . . .
        . . f e e e f f e e e e f . . .
        . . f f f f e e 2 2 2 2 e f . .
        . . f e 2 2 2 f f f f e 2 f . .
        . f f f f f f f e e e f f f . .
        . f f e 4 4 e b f 4 4 e e f . .
        . f e e 4 d 4 1 f d d e f . . .
        . . f e e e e e d d d f . . . .
        . . . . f 4 d d e 4 e f . . . .
        . . . . f e d d e 2 2 f . . . .
        . . . f f f e e f 5 5 f f . . .
        . . . f f f f f f f f f f . . .
        . . . . f f . . . f f f . . . .
        """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    mySprite.set_image(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f e e d d d d d d e e f . .
        . . . f e e 4 4 4 4 e e f . . .
        . . e 4 f 2 2 2 2 2 2 f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

level = 0
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f e e d d d d d d e e f . .
        . . . f e e 4 4 4 4 e e f . . .
        . . e 4 f 2 2 2 2 2 2 f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """),
    SpriteKind.player)
chest = sprites.create(img("""
        . . b b b b b b b b b b b b . .
        . b e 4 4 4 4 4 4 4 4 4 4 e b .
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
        b e e 4 4 4 4 4 4 4 4 4 4 e e b
        b e e e e e e e e e e e e e e b
        b e e e e e e e e e e e e e e b
        b b b b b b b d d b b b b b b b
        c b b b b b b c c b b b b b b c
        c c c c c c b c c b c c c c c c
        b e e e e e c b b c e e e e e b
        b e e e e e e e e e e e e e e b
        b c e e e e e e e e e e e e c b
        b b b b b b b b b b b b b b b b
        . b b . . . . . . . . . . b b .
        """),
    SpriteKind.Storage)
chest.set_position(71, 29)
tiles.set_current_tilemap(tilemap("""
    level1
    """))
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
keys = 0
game.show_long_text("You have been tasked with saving Sky from <no name yet>",
    DialogLayout.CENTER)
game.show_long_text("Find keys in each room to unlock the doors",
    DialogLayout.CENTER)
game.show_long_text("Good luck!", DialogLayout.CENTER)
level = 1

def on_forever():
    global keys, chest
    if mySprite.overlaps_with(chest):
        chest.set_image(img("""
            . b b b b b b b b b b b b b b .
            b e 4 4 4 4 4 4 4 4 4 4 4 4 4 b
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
            b e e 4 4 4 4 4 4 4 4 4 4 e e b
            b b b b b b b d d b b b b b b b
            . b b b b b b c c b b b b b b .
            b c c c c c b c c b c c c c c b
            b c c c c c c b b c c c c c c b
            b c c c c c c c c c c c c c c b
            b c c c c c c c c c c c c c c b
            b b b b b b b b b b b b b b b b
            b e e e e e e e e e e e e e e b
            b e e e e e e e e e e e e e e b
            b c e e e e e e e e e e e e c b
            b b b b b b b b b b b b b b b b
            . b b . . . . . . . . . . b b .
            """))
        keys += 1
        game.show_long_text(keys, DialogLayout.BOTTOM)
        sprites.destroy(chest)
        chest = sprites.create(img("""
                . . b b b b b b b b b b b b . .
                . b e 4 4 4 4 4 4 4 4 4 4 e b .
                b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
                b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
                b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
                b e e 4 4 4 4 4 4 4 4 4 4 e e b
                b e e e e e e e e e e e e e e b
                b e e e e e e e e e e e e e e b
                b b b b b b b d d b b b b b b b
                c b b b b b b c c b b b b b b c
                c c c c c c b c c b c c c c c c
                b e e e e e c b b c e e e e e b
                b e e e e e e e e e e e e e e b
                b c e e e e e e e e e e e e c b
                b b b b b b b b b b b b b b b b
                . b b . . . . . . . . . . b b .
                """),
            SpriteKind.Storage)
        chest.set_position(randint(15, 130), randint(6, 100))
forever(on_forever)

def on_forever2():
    if mySprite.is_hitting_tile(CollisionDirection.TOP):
        if keys >= 1:
            if level == 1:
                level2()
            else:
                if level == 2:
                    if keys >= 5:
                        game.show_long_text("YOU SAVED SKY (idk anymore)", DialogLayout.FULL)
                        game.game_over(True)
                    else:
                        game.show_long_text("you need 5 keys!", DialogLayout.CENTER)
                else:
                    pass
        else:
            game.show_long_text("You need 1 key!", DialogLayout.BOTTOM)
forever(on_forever2)
