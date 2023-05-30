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
        for index, urls in self.tiles.items():
            url = self._query(urls, version)
            tiles.append((index, url))
        return tiles

    def _query(self, urls, version):
        versions = [v for v, url in urls]  # TMP O(N)! use 3.10
        idx = bisect.bisect_left(versions, version)        
        # urls[i][0] <= version for all i in {0, 1, ..., idx-1}
        # urls[i][0] > version for all i in {idx, ...}
        # therefore urls[idx][0] > version
        
        # versions = [1]
        # bisect([1], 3)
        
        
        print("version", version)
        print("versions", versions)
        print("urls", urls)
        print("idx", idx)        
        while idx > 0:
            _version, url = urls[idx - 1]
            if _version <= version:
                return url
            idx -= 1
        raise AssertionError("url satisfying version not found")


def test_1():
    ms = MapService()                                     
    version = ms.add_tiles([(1, "a")])
    assert version == 1
    assert ms.get_tiles(1) == [(1, "a")]

def test_2():
    ms = MapService()                                     
    version = ms.add_tiles([(1, "a")])
    assert version == 1
    print(1)
    version = ms.add_tiles([(2, "b")])
    assert version == 2
    print(2)
    version = ms.add_tiles([(2, "c")])
    assert version == 3    
    print(3)
    # assert ms.get_tiles(1) == [(1, "a")]
    # assert ms.get_tiles(2) == [(1, "a"), (2, "b")]
    print(ms.get_tiles(3), [(1, "a"), (2, "c")])

    
    
# test_1()
test_2()
