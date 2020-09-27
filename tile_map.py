from pytmx import TiledMap

TILE_WIDTH = 256
TILE_HEIGHT = 149


def read_sprite_list(grid, sprite_list):
    for row in grid:
        for grid_location in row:
            if grid_location.tile is not None:
                tile_sprite = arcade.Sprite(os.getcwd() + '/' + grid_location.tile.source, SPRITE_SCALING)
                tile_sprite.center_x = grid_location.center_x * SPRITE_SCALING
                tile_sprite.center_y = grid_location.center_y * SPRITE_SCALING
                sprite_list.append(tile_sprite)


class MyMap:
    def __init__(self):
        self.tmxdata = TiledMap("data/maps/first.tmx")
        self.map_width = self.tmxdata.width
        self.map_height = self.tmxdata.height
        self.tile_width = self.tmxdata.tilewidth
        self.tile_height = self.tmxdata.tileheight
        self.floor_list = self.get_tile_info('floor')
        self.items_list = self.get_tile_info('items')
        self.city_list = self.get_tile_info('city')
        self.layers = [self.floor_list, self.items_list, self.city_list]

    def get_tile_info(self, name):
        tiles_list = []
        layer = self.tmxdata.get_layer_by_name(name)
        for column_index, row_index, image in layer.tiles():
            tile = Tile()
            tile.column_index = column_index
            tile.row_index = row_index
            if row_index % 2 == 0:
                tile.center_x = column_index * TILE_WIDTH + TILE_WIDTH / 2
                tile.center_y = (self.map_height - row_index -1) * (TILE_HEIGHT/2)
            else:
                tile.center_x = column_index * TILE_WIDTH
                tile.center_y = (self.map_height - row_index-1) * (TILE_HEIGHT/2)
            tile.width = self.tile_width
            tile.height = self.tile_height+10
            tile.image = f"'{image[0]}'"
            tiles_list.append(tile)
        return tiles_list


class Tile:
    def __init__(self):
        self.column_index = None
        self.row_index = None
        self.center_x = None
        self.center_y = None
        self.height = None
        self.width = None
        self.image = None


#mymap = MyMap()