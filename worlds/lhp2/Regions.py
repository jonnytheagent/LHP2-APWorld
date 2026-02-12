from BaseClasses import MultiWorld, Region, Entrance, Location, ItemClassification
from .Locations import LHP2Location
from .Items import LHP2Item
from .Names import RegionName


level_regions = [
    RegionName.dt,
    RegionName.da,
    RegionName.foc,
    RegionName.kd,
    RegionName.agv,
    RegionName.avt,
    RegionName.oor,
    RegionName.jd,
    RegionName.ansmc,
    RegionName.lh,
    RegionName.ff,
    RegionName.thath,
    RegionName.tsh,
    RegionName.mim,
    RegionName.igd,
    RegionName.sal,
    RegionName.ll,
    RegionName.dob,
    RegionName.ttd,
    RegionName.bts,
    RegionName.bb,
    RegionName.fiend,
    RegionName.st,
    RegionName.tfitp
]

hub_regions = [
    RegionName.diag,
    RegionName.knock,
    RegionName.www,
    RegionName.mm,
    RegionName.cust,
    RegionName.leaky,
    RegionName.lond,
    RegionName.cafe,
    RegionName.kcs,
    RegionName.tent,
    RegionName.wild,
    RegionName.hogstat,
    RegionName.hogspath,
    RegionName.hogs,
    RegionName.hogwpath,
    RegionName.court,
    RegionName.tg,
    RegionName.herb,
    RegionName.ground,
    RegionName.qp,
    RegionName.thest,
    RegionName.lake,
    RegionName.foyer,
    RegionName.stair,
    RegionName.house,
    RegionName.slyth,
    RegionName.huff,
    RegionName.gryf,
    RegionName.raven,
    RegionName.lib,
    RegionName.ghl,
    RegionName.wc,
    RegionName.wcs,
    RegionName.gh,
    RegionName.ror,
    RegionName.cl,
    RegionName.y5c,
    RegionName.y6c,
    RegionName.dada,
    RegionName.pot,
    RegionName.divc,
    RegionName.div,
    RegionName.ast,
]


freeplay_regions = [
    RegionName.focf,
    RegionName.oorf,
    RegionName.ansmcf,
    RegionName.lhf,
    RegionName.fff,
    RegionName.thathf,
]


lhp2_all_regions = [
    *level_regions,
    *hub_regions,
    *freeplay_regions,
]


def create_regions(world: MultiWorld, player: int, seed_locs):
    menu = Region("Menu", player, world)
    world.regions.append(menu)

    for region in lhp2_all_regions:
        create_regions_and_locations(region, player, world, seed_locs)

    connect_regions(world, player, "Menu", RegionName.diag)
    connect_regions(world, player, RegionName.diag, RegionName.knock)
    connect_regions(world, player, RegionName.knock, RegionName.ror)
    connect_regions(world, player, RegionName.diag, RegionName.www)
    connect_regions(world, player, RegionName.diag, RegionName.mm)
    connect_regions(world, player, RegionName.mm, RegionName.cust)
    connect_regions(world, player, RegionName.diag, RegionName.leaky)
    connect_regions(world, player, RegionName.leaky, RegionName.lond)
    connect_regions(world, player, RegionName.lond, RegionName.cafe)
    connect_regions(world, player, RegionName.lond, RegionName.tent)
    connect_regions(world, player, RegionName.tent, RegionName.wild)
    connect_regions(world, player, RegionName.lond, RegionName.kcs)
    connect_regions(world, player, RegionName.kcs, RegionName.hogstat)
    connect_regions(world, player, RegionName.hogstat, RegionName.hogwpath)
    connect_regions(world, player, RegionName.hogwpath, RegionName.hogspath)
    connect_regions(world, player, RegionName.hogspath, RegionName.hogs)
    connect_regions(world, player, RegionName.hogwpath, RegionName.court)
    connect_regions(world, player, RegionName.court, RegionName.tg)
    connect_regions(world, player, RegionName.tg, RegionName.herb)
    connect_regions(world, player, RegionName.court, RegionName.foyer)
    connect_regions(world, player, RegionName.foyer, RegionName.ground)
    connect_regions(world, player, RegionName.ground, RegionName.thest)
    connect_regions(world, player, RegionName.ground, RegionName.qp)
    connect_regions(world, player, RegionName.ground, RegionName.lake)
    connect_regions(world, player, RegionName.foyer, RegionName.lib)
    connect_regions(world, player, RegionName.foyer, RegionName.ghl)
    connect_regions(world, player, RegionName.ghl, RegionName.gh)
    connect_regions(world, player, RegionName.ghl, RegionName.wc)
    connect_regions(world, player, RegionName.wc, RegionName.wcs)
    connect_regions(world, player, RegionName.ghl, RegionName.ror)
    connect_regions(world, player, RegionName.ror, RegionName.stair)
    connect_regions(world, player, RegionName.foyer, RegionName.stair)
    connect_regions(world, player, RegionName.stair, RegionName.house)
    connect_regions(world, player, RegionName.house, RegionName.slyth)
    connect_regions(world, player, RegionName.house, RegionName.huff)
    connect_regions(world, player, RegionName.house, RegionName.gryf)
    connect_regions(world, player, RegionName.house, RegionName.raven)
    connect_regions(world, player, RegionName.foyer, RegionName.cl)
    connect_regions(world, player, RegionName.cl, RegionName.dada)
    connect_regions(world, player, RegionName.cl, RegionName.y5c)
    connect_regions(world, player, RegionName.cl, RegionName.y6c)
    connect_regions(world, player, RegionName.cl, RegionName.pot)
    connect_regions(world, player, RegionName.cl, RegionName.divc)
    connect_regions(world, player, RegionName.divc, RegionName.ast)
    connect_regions(world, player, RegionName.divc, RegionName.div)

    for region in level_regions:
        connect_regions(world, player, RegionName.leaky, region)

    connect_regions(world, player, RegionName.foc, RegionName.focf)
    connect_regions(world, player, RegionName.oor, RegionName.oorf)
    connect_regions(world, player, RegionName.ansmc, RegionName.ansmcf)
    connect_regions(world, player, RegionName.lh, RegionName.lhf)
    connect_regions(world, player, RegionName.ff, RegionName.fff)
    connect_regions(world, player, RegionName.thath, RegionName.thathf)

    tfitp_region = world.get_region(RegionName.tfitp, player)
    create_event("Defeat Voldemort", "Voldemort Defeated", tfitp_region, player)


def connect_regions(world: MultiWorld, player: int, source: str, target: str) -> Entrance:
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)
    return source_region.connect(target_region)


def create_regions_and_locations(name: str, player: int, world: MultiWorld, seed_locations) -> Region:
    region = Region(name, player, world)

    for (key, data) in seed_locations.items():
        if data.region == name:
            location = LHP2Location(player, key, data.id, region)
            region.locations.append(location)

    world.regions.append(region)
    return region


# def create_events(world: MultiWorld, player: int) -> int:
#     count = 0
#
#     for (name, data) in level_beaten_event_location_table.items():
#         item_name = "Level Beaten Token"
#         event: Location = create_event(name, item_name, world.get_region(data.region, player), player)
#         event.show_in_spoiler = True
#         count += 1
#
#     return count
#
#
def create_event(name: str, item_name: str, region: Region, player: int) -> Location:
    event = LHP2Location(player, name, None, region)
    region.locations.append(event)
    event.place_locked_item(LHP2Item(item_name, ItemClassification.progression, None, player))
    return event
