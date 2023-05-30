# Context:
# The Mapping team generates and delivers maps which include sets of indexed tiles to various teams within Cruise. Each map is associated with a unique map version and many different map versions are currently used across the company.

# Problem:
# The data acquisition team generates and publishes only new or updated tiles for each new version.
# However, tiles from previous versions which are unchanged when a tile set is published should still be obtained when requesting the new version.

# These tiles are represented by an index (e.g. tile 0) and a content url.


# Implement a solution which provides the following interface:

#     Add Tiles
#         Input:  Collection of (index, url) pairs which are to be upserted
#         Output: Version
        
#     Get Tiles
#         Input:  Version
#         Output: Collection of (index, url) pairs corresponding to the
#                 Version-th set of tiles provided via "Add Tiles"
import bisect
from collections import defaultdict
# from functools import total_ordering
from typing import List, Tuple


class MapService:
    
    def __init__(self):
        self.tiles = defaultdict(list)
        self.version = 0
    
    def add_tiles(self, tiles: List[Tuple[int, str]]) -> int:
        self.version += 1
        for index, url in tiles:
            self.tiles[index].append((self.version, url))
        return self.version

    def get_tiles(self, version: int) -> List[Tuple[int, str]]:
        tiles = []
        for index, tile_versions in self.tiles.items():
            tiles.append((index, self._query(tile_versions, version)))
        return tiles

    def _query(self, tile_versions, version) -> str:
        versions = [v for v, _ in tile_versions]  # TMP O(N)! use 3.10
        idx = bisect.bisect_right(versions, version)
        if idx:
            version, url = tile_versions[idx - 1]
            return url
        raise AssertionError("url satisfying version not found")
        

def test_1():
    ms = MapService()                                     
    version = ms.add_tiles([(1, "v1")])
    assert version == 1
    assert ms.get_tiles(1) == [(1, "v1")]

def test_2():
    ms = MapService()                                     
    version = ms.add_tiles([(1, "v1"), (2, "v1")])
    assert version == 1
    version = ms.add_tiles([(2, "v2")])
    assert version == 2
    version = ms.add_tiles([(2, "v3")])
    assert version == 3    
    assert ms.get_tiles(1) == [(1, "v1"), (2, "v1")]
    assert ms.get_tiles(2) == [(1, "v1"), (2, "v2")]
    assert ms.get_tiles(3) == [(1, "v1"), (2, "v3")]

    
    
test_1()
test_2()
    