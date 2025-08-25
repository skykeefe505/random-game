// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level1":
            case "level1":return tiles.createTilemap(hex`1000100001050505050505050505050505050504080909090909090909090909090909060809090909090909090909090909090608090909090909090909090909090906020707090909090909090909090909060a0a0a080909090909090909090909060a0a0a080909090909090909090909060a0a0a080909090909090909090909060a0a0a080909090909090909090909060a0a0a080909090909090909090909060a0a0a080909090909090909090909060a0a0a080909090909090909090909060a0a0a08090909090909090909090906010505090909090909090909090909060809090909090909090909090909090602070707070707070707070707070703`, img`
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
`, [myTiles.transparency16,sprites.castle.tilePath1,sprites.castle.tilePath7,sprites.castle.tilePath9,sprites.castle.tilePath3,sprites.castle.tilePath2,sprites.castle.tilePath6,sprites.castle.tilePath8,sprites.castle.tilePath4,sprites.castle.tilePath5,sprites.castle.tileGrass1], TileScale.Sixteen);
            case "level2":
            case "level2":return tiles.createTilemap(hex`1000100001060606060606060606060606060602050909090909090909090909090909070509090909090909090909090909090705090909090909090909090909090907050909090909090909090909090909070509090909090909090909090909090705090909090909090909090909090907050909090909090909090909090909070509090909090909090909090909090705090909090909090909090909090907050909090909090909090909090909070509090909090909090909090909090705090909090909090909090909090907050909090909090909090909090909070509090909090909090909090909090704080808080808080808080808080803`, img`
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
`, [myTiles.transparency16,sprites.dungeon.darkGroundNorthWest0,sprites.dungeon.darkGroundNorthEast0,sprites.dungeon.darkGroundSouthEast0,sprites.dungeon.darkGroundSouthWest0,sprites.dungeon.darkGroundWest,sprites.dungeon.darkGroundNorth,sprites.dungeon.darkGroundEast,sprites.dungeon.darkGroundSouth,sprites.dungeon.darkGroundCenter], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
