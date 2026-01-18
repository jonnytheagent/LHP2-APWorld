from typing import List, Callable

from BaseClasses import MultiWorld, Location
from worlds.generic.Rules import set_rule
from worlds.AutoWorld import CollectionState

from .Names import LocationName, ItemName, RegionName
from .Options import LHP2Options, EndGoal


# Helper Functions
def can_use_dark_magic(state: CollectionState, player: int) -> bool:
    return (
            state.has(ItemName.alecto_play, player)
            or state.has(ItemName.amycus_play, player)
            or state.has(ItemName.dolohov_play, player)
            or state.has(ItemName.dolohov_play, player)
            or state.has(ItemName.bellatrix_azka_play, player)
            or state.has(ItemName.bellatrix_play, player)
            or state.has(ItemName.death_eater_play, player)
            or state.has(ItemName.fenrir_play, player)
            or state.has(ItemName.grindel_old_play, player)
            or state.has(ItemName.grindel_young_play, player)
            or state.has(ItemName.lord_voldemort_play, player)
            or state.has(ItemName.lucius_play, player)
            or state.has(ItemName.lucius_death_eater_play, player)
            or state.has(ItemName.black_play, player)
            or state.has(ItemName.pius_play, player)
            or state.has(ItemName.scabior_play, player)
            or state.has(ItemName.snatcher_play, player)
            or state.has(ItemName.rowle_play, player)
            or state.has(ItemName.tom_riddle_play, player)
            or state.has(ItemName.tr_orphanage_play, player) # TODO: to check
    )


def can_use_spanner(state: CollectionState, player: int) -> bool:
    return(
            state.has(ItemName.arthur_play, player)
            or state.has(ItemName.arthur_suit_play, player)
            or state.has(ItemName.arthur_play, player)
            or state.has(ItemName.arthur_torn_suit_play, player)
    )


def can_use_key(state: CollectionState, player: int) -> bool:
    return(
            state.has(ItemName.bogrod_play, player)
            or state.has(ItemName.cole_play, player)
            or state.has(ItemName.griphook_play, player)
    )


def char_is_strong(state: CollectionState, player: int) -> bool:
    return(
            state.has(ItemName.dudley_play, player)
            or state.has(ItemName.dudley_shirt_play, player)
            or state.has(ItemName.dudley_grey_play, player)
            or state.has(ItemName.fenrir_play, player)
            or state.has(ItemName.fang_play, player)
            or state.has(ItemName.hagrid_play, player)
            or state.has(ItemName.hagrid_wed_play, player)
            or state.has(ItemName.remus_lupin_play, player)
            or state.has(ItemName.sirius_black_play, player)
            or state.has(ItemName.sirius_azkaban_play, player) # TODO: to verify
            or state.has(ItemName.super_strength_unlock, player)
    )


# Dark Times Logic
def can_get_dt_sc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.diffindo_unlock, player)


def can_get_dt_hc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.www_box_unlock, player)


def can_get_dt_sip(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player)


def can_collect_arthur_suit_tok(state: CollectionState, player: int) -> bool:
    return can_use_spanner(state, player)


def can_collect_doge_token(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.agua_unlock, player)


# Dumbledore's Army Logic
def can_beat_da(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.expecto_unlock, player)


def can_get_da_gc(state: CollectionState, player: int) -> bool:
    return (
            state.has(ItemName.reducto_unlock, player)
            and char_is_strong(state, player)
            and state.has(ItemName.specs_unlock, player)
    )


def can_get_da_sc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.focus_unlock, player)


def can_get_da_rc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.apparition_unlock, player)


def can_get_da_hc(state: CollectionState, player: int) -> bool:
    return (
            state.has(ItemName.reducto_unlock, player)
            and state.has(ItemName.www_box_unlock, player)
            and char_is_strong(state, player)
            and state.has(ItemName.specs_unlock, player)
    )


def can_get_da_sip(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.reducto_unlock, player) and can_use_dark_magic(state, player)


def can_collect_cho_winter(state: CollectionState, player: int) -> bool:
    return(
            state.has(ItemName.reducto_unlock, player)
            and char_is_strong(state, player)
            and state.has(ItemName.specs_unlock, player)
    )


def can_collect_herm_scarf(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.www_box_unlock, player)


def can_collect_neville_winter(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.specs_unlock, player)


# Focus!
def can_get_foc_gc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.reducto_unlock, player)


def can_get_foc_hc(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player)


def can_get_foc_sip(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.agua_unlock, player)

def can_collect_molly_apron(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.reducto_unlock, player) and char_is_strong(state, player)


def can_collect_snape_under(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.www_box_unlock, player)


# Kreacher Discomforts
def can_get_kd_gc(state: CollectionState, player: int) -> bool:
    return char_is_strong(state, player) and state.has(ItemName.apparition_unlock, player)


def can_get_kd_sc(state: CollectionState, player: int) -> bool:
    return (
            state.has(ItemName.reducto_unlock, player)
            and state.has(ItemName.delum_unlock, player)
            and can_use_dark_magic(state, player)
            and state.has(ItemName.diffindo_unlock, player)
    )


def can_get_kd_hc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.reducto_unlock, player) and state.has(ItemName.diffindo_unlock, player)


def can_get_kd_sip(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.reducto_unlock, player)


def can_collect_kreacher(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player)


def can_collect_sirius(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.agua_unlock, player)


# A Giant Virtuoso
def can_get_agv_gc(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player)


def can_get_agv_sc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.herm_bag_unlock, player)


def can_get_agv_rc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.agua_unlock, player)


def can_get_agv_hc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.reducto_unlock, player)


def can_get_agv_sip(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.www_box_unlock, player)


def can_collect_emmeline(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.agua_unlock, player)


def can_collect_neville(state: CollectionState, player: int) -> bool:
    return char_is_strong(state, player)


def can_collect_prof_umbridge(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player)


# A Veiled Threat Logic
def can_beat_avt(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.diffindo_unlock, player)


def can_get_avt_rc(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.agua_unlock, player)


def can_get_avt_hc(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player)


def can_collect_fudge_wizen(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.diffindo_unlock, player)


def can_collect_herm_jumper(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.agua_unlock, player)


def can_collect_lucius_death(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player)


# Out of Retirement Logic
def can_access_oor_freeplay(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.apparition_unlock, player) and state.has(ItemName.reducto_unlock, player)


def can_beat_oor(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.www_box_unlock, player)


def can_get_oor_gc(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player)


def can_get_oor_sc(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player) and state.has(ItemName.agua_unlock, player)


def can_get_oor_rc(state: CollectionState, player: int) -> bool:
    return (
            state.has(ItemName.apparition_unlock, player)
            and state.has(ItemName.specs_unlock, player)
            and can_use_dark_magic(state, player)
    )


def can_get_oor_hc(state: CollectionState, player: int) -> bool:
    return (
            can_use_dark_magic(state, player)
            and state.has(ItemName.www_box_unlock, player)
            and state.has(ItemName.diffindo_unlock, player)
    )


def can_get_oor_sip(state: CollectionState, player: int) -> bool:
    return (
            can_use_dark_magic(state, player)
            and state.has(ItemName.www_box_unlock, player)
            and state.has(ItemName.diffindo_unlock, player)
    )


def can_collect_dumble_cursed(state: CollectionState, player: int) -> bool:
    return can_use_dark_magic(state, player)


def can_collect_milk_man(state: CollectionState, player: int) -> bool:
    return state.has(ItemName.herm_bag_unlock, player)


def can_collect_slug_pajamas(state: CollectionState, player: int) -> bool:
    return(
            state.has(ItemName.apparition_unlock, player)
            and can_use_dark_magic(state, player)
            and can_use_key(state, player)
    )


def set_rules(world: MultiWorld, options: LHP2Options, player: int):
    set_entrance_rules(world, options, player)
    set_win_con(world, options, player)
    set_dt_logic(world, options, player)
    set_da_logic(world, options, player)
    set_foc_logic(world, options, player)
    set_kd_logic(world, options, player)
    set_agv_logic(world, options, player)
    set_avt_logic(world, options, player)


def set_entrance_rules(world: MultiWorld, options: LHP2Options, player: int):
    # Level Entrance Rules
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.dt, player),
             lambda state: state.has(ItemName.dt_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.da, player),
             lambda state: state.has(ItemName.da_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.foc, player),
             lambda state: state.has(ItemName.foc_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.kd, player),
             lambda state: state.has(ItemName.kd_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.agv, player),
             lambda state: state.has(ItemName.agv_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.avt, player),
             lambda state: state.has(ItemName.avt_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.oor, player),
             lambda state: state.has(ItemName.oor_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.jd, player),
             lambda state: state.has(ItemName.jd_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.ansmc, player),
             lambda state: state.has(ItemName.ansmc_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.lh, player),
             lambda state: state.has(ItemName.lh_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.ff, player),
             lambda state: state.has(ItemName.ff_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.thath, player),
             lambda state: state.has(ItemName.thath_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.tsh, player),
             lambda state: state.has(ItemName.tsh_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.mim, player),
             lambda state: state.has(ItemName.mim_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.igd, player),
             lambda state: state.has(ItemName.igd_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.sal, player),
             lambda state: state.has(ItemName.sal_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.ll, player),
             lambda state: state.has(ItemName.ll_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.dob, player),
             lambda state: state.has(ItemName.dob_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.ttd, player),
             lambda state: state.has(ItemName.ttd_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.bts, player),
             lambda state: state.has(ItemName.bts_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.bb, player),
             lambda state: state.has(ItemName.bb_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.fiend, player),
             lambda state: state.has(ItemName.fiend_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.st, player),
             lambda state: state.has(ItemName.st_unlock, player))
    set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.tfitp, player),
             lambda state: state.has(ItemName.tfitp_unlock, player))
    # Freeplay Entrance Rules
    set_rule(world.get_entrance(RegionName.foc + " -> " + RegionName.focf, player),
             lambda state: state.has(ItemName.focus_unlock, player))
    set_rule(world.get_entrance(RegionName.oor + " -> " + RegionName.oorf, player),
             lambda state: can_access_oor_freeplay(state, player))

def set_win_con(world: MultiWorld, options: LHP2Options, player: int):
    if options.EndGoal == EndGoal.option_defeat_voldemort:
        world.completion_condition[player] = lambda state: state.can_reach_location(LocationName.tfitp_beat, player)
    # if options.EndGoal == EndGoal.option_the_collector:
    #     world.completion_condition[player] =


def set_dt_logic(world: MultiWorld, options: LHP2Options, player: int):
    set_rule(world.get_location(LocationName.dt_sc, player), lambda state: can_get_dt_sc(state, player))
    set_rule(world.get_location(LocationName.dt_hc, player), lambda state: can_get_dt_hc(state, player))
    set_rule(world.get_location(LocationName.dt_sip, player), lambda state: can_get_dt_sip(state, player))
    set_rule(world.get_location(LocationName.arthur_suit_token, player),
             lambda state: can_collect_arthur_suit_tok(state, player))
    set_rule(world.get_location(LocationName.elphias_token, player),
             lambda state: can_collect_doge_token(state, player))


def set_da_logic(world: MultiWorld, options: LHP2Options, player: int):
    set_rule(world.get_location(LocationName.da_beat, player), lambda state: can_beat_da(state, player))
    set_rule(world.get_location(LocationName.da_tw, player), lambda state: can_beat_da(state, player))
    set_rule(world.get_location(LocationName.da_gc, player), lambda state: can_get_da_gc(state, player))
    set_rule(world.get_location(LocationName.da_sc, player), lambda state: can_get_da_sc(state, player))
    set_rule(world.get_location(LocationName.da_rc, player), lambda state: can_get_da_rc(state, player))
    set_rule(world.get_location(LocationName.da_hc, player), lambda state: can_get_da_hc(state, player))
    set_rule(world.get_location(LocationName.da_sip, player), lambda state: can_get_da_sip(state, player))
    set_rule(world.get_location(LocationName.cho_winter_token, player),
             lambda state: can_collect_cho_winter(state, player))
    set_rule(world.get_location(LocationName.herm_scarf_token, player),
             lambda state: can_collect_herm_scarf(state, player))
    set_rule(world.get_location(LocationName.neville_winter_token, player),
             lambda state: can_collect_neville_winter(state, player))


def set_foc_logic(world: MultiWorld, options: LHP2Options, player: int):
    set_rule(world.get_location(LocationName.foc_gc, player), lambda state: can_get_foc_gc(state, player))
    set_rule(world.get_location(LocationName.foc_hc, player), lambda state: can_get_foc_hc(state, player))
    set_rule(world.get_location(LocationName.foc_sip, player), lambda state: can_get_foc_sip(state, player))
    set_rule(world.get_location(LocationName.molly_apron_token, player),
             lambda state: can_collect_molly_apron(state, player))
    set_rule(world.get_location(LocationName.snape_underwear_token, player),
             lambda state: can_collect_snape_under(state, player))


def set_kd_logic(world: MultiWorld, options: LHP2Options, player: int):
    set_rule(world.get_location(LocationName.kd_gc, player), lambda state: can_get_kd_gc(state, player))
    set_rule(world.get_location(LocationName.kd_sc, player), lambda state: can_get_kd_sc(state, player))
    set_rule(world.get_location(LocationName.kd_hc, player), lambda state: can_get_kd_hc(state, player))
    set_rule(world.get_location(LocationName.kd_sip, player), lambda state: can_get_kd_sip(state, player))
    set_rule(world.get_location(LocationName.kreacher_token, player),
             lambda state: can_collect_kreacher(state, player))
    set_rule(world.get_location(LocationName.sirius_black_token, player),
             lambda state: can_collect_sirius(state, player))


def set_agv_logic(world: MultiWorld, options: LHP2Options, player: int):
    set_rule(world.get_location(LocationName.agv_gc, player), lambda state: can_get_agv_gc(state, player))
    set_rule(world.get_location(LocationName.agv_sc, player), lambda state: can_get_agv_sc(state, player))
    set_rule(world.get_location(LocationName.agv_rc, player), lambda state: can_get_agv_rc(state, player))
    set_rule(world.get_location(LocationName.agv_hc, player), lambda state: can_get_agv_hc(state, player))
    set_rule(world.get_location(LocationName.agv_sip, player), lambda state: can_get_agv_sip(state, player))
    set_rule(world.get_location(LocationName.emmeline_token, player),
             lambda state: can_collect_emmeline(state, player))
    set_rule(world.get_location(LocationName.neville_token, player),
             lambda state: can_collect_neville(state, player))
    set_rule(world.get_location(LocationName.prof_umbridge_token, player),
             lambda state: can_collect_prof_umbridge(state, player))


def set_avt_logic(world: MultiWorld, options: LHP2Options, player: int):
    set_rule(world.get_location(LocationName.avt_beat, player), lambda state: can_beat_avt(state, player))
    set_rule(world.get_location(LocationName.avt_tw, player), lambda state: can_beat_avt(state, player))
    set_rule(world.get_location(LocationName.avt_rc, player), lambda state: can_get_avt_rc(state, player))
    set_rule(world.get_location(LocationName.avt_hc, player), lambda state: can_get_avt_hc(state, player))
    set_rule(world.get_location(LocationName.fudge_wizengamot_token, player),
             lambda state: can_collect_fudge_wizen(state, player))
    set_rule(world.get_location(LocationName.herm_jumper_token, player),
             lambda state: can_collect_herm_jumper(state, player))
    set_rule(world.get_location(LocationName.lucius_death_eater_token, player),
             lambda state: can_collect_lucius_death(state, player))


def set_oor_logic(world: MultiWorld, options: LHP2Options, player: int):
    set_rule(world.get_location(LocationName.oor_beat, player), lambda state: can_beat_oor(state, player))
    set_rule(world.get_location(LocationName.oor_tw, player), lambda state: can_beat_oor(state, player))
    set_rule(world.get_location(LocationName.oor_gc, player), lambda state: can_get_oor_gc(state, player))
    set_rule(world.get_location(LocationName.oor_sc, player), lambda state: can_get_oor_sc(state, player))
    set_rule(world.get_location(LocationName.oor_rc, player), lambda state: can_get_oor_rc(state, player))
    set_rule(world.get_location(LocationName.oor_hc, player), lambda state: can_get_oor_hc(state, player))
    set_rule(world.get_location(LocationName.oor_sip, player), lambda state: can_get_oor_sip(state, player))
    set_rule(world.get_location(LocationName.dumble_cursed_token, player),
             lambda state: can_collect_dumble_cursed(state, player))
    set_rule(world.get_location(LocationName.milk_man_token, player),
             lambda state: can_collect_milk_man(state, player))
    set_rule(world.get_location(LocationName.slughorn_pajamas_token, player),
             lambda state: can_collect_slug_pajamas(state, player))
