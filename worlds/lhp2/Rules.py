from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from . import LHP2World

from .Names import LocationName, ItemName, RegionName
from .Options import LHP2Options, EndGoal


#Helper Rules
can_use_dark_magic = (Has(ItemName.alecto_play) | Has(ItemName.amycus_play) | Has(ItemName.dolohov_play) |
        Has(ItemName.bellatrix_play) | Has(ItemName.bellatrix_azka_play) | Has(ItemName.death_eater_play) |
        Has(ItemName.fenrir_play) | Has(ItemName.grindel_old_play) | Has(ItemName.grindel_young_play) |
        Has(ItemName.lord_voldemort_play) | Has(ItemName.lucius_play) | Has(ItemName.lucius_death_eater_play) |
        Has(ItemName.black_play) | Has(ItemName.pius_play) | Has(ItemName.scabior_play) |
        Has(ItemName.snatcher_play) | Has(ItemName.rowle_play) | Has(ItemName.tom_riddle_play))


can_use_spanner = (Has(ItemName.arthur_play) | Has(ItemName.arthur_suit_play) | Has(ItemName.arthur_cardigan_play) |
                   Has(ItemName.arthur_torn_suit_play))


can_use_key = Has(ItemName.bogrod_play) | Has(ItemName.cole_play) | Has(ItemName.griphook_play)


char_is_strong = (Has(ItemName.dudley_play) | Has(ItemName.dudley_grey_play) | Has(ItemName.dudley_shirt_play) |
                  Has(ItemName.fenrir_play) | Has(ItemName.fang_play) | Has(ItemName.hagrid_play) |
                  Has(ItemName.hagrid_wed_play) | Has(ItemName.remus_lupin_play) | Has(ItemName.sirius_black_play) |
                  Has(ItemName.sirius_azkaban_play) | Has(ItemName.super_strength_unlock))


# Dark Times Logic
can_get_dt_sc = Has(ItemName.diffindo_unlock)
can_get_dt_hc = Has(ItemName.www_box_unlock)
can_get_dt_sip = can_use_dark_magic
can_get_arthur_suit = can_use_spanner
can_get_elphias = Has(ItemName.agua_unlock)


# Dumbledore's Army Logic
can_beat_da = Has(ItemName.expecto_unlock)
can_get_da_gc = HasAll(ItemName.reducto_unlock, ItemName.specs_unlock) & char_is_strong
can_get_da_sc = Has(ItemName.focus_unlock)
can_get_da_rc = Has(ItemName.apparition_unlock)
can_get_da_hc = (HasAll(ItemName.reducto_unlock, ItemName.www_box_unlock, ItemName.specs_unlock) 
                 & char_is_strong)
can_get_da_sip = Has(ItemName.reducto_unlock) & can_use_dark_magic
can_get_cho_winter = HasAll(ItemName.reducto_unlock, ItemName.specs_unlock) & char_is_strong
can_get_herm_scarf = Has(ItemName.www_box_unlock)
can_get_neville_winter = Has(ItemName.specs_unlock)


# Focus!
can_get_foc_gc = Has(ItemName.reducto_unlock)
can_get_foc_hc = can_use_dark_magic
can_get_foc_sip = Has(ItemName.agua_unlock)
can_get_molly_apron = Has(ItemName.reducto_unlock) & char_is_strong
can_get_snape_under = Has(ItemName.www_box_unlock)


# Kreacher Discomforts
can_get_kd_gc = Has(ItemName.apparition_unlock) & char_is_strong
can_get_kd_sc = (HasAll(ItemName.reducto_unlock, ItemName.delum_unlock, ItemName.diffindo_unlock)
                 & char_is_strong)
can_get_kd_hc = HasAll(ItemName.reducto_unlock, ItemName.diffindo_unlock)
can_get_kd_sip = Has(ItemName.reducto_unlock)
can_get_kreacher = can_use_dark_magic
can_get_sirius = Has(ItemName.agua_unlock)


# A Giant Virtuoso
can_get_agv_gc = can_use_dark_magic
can_get_agv_sc = Has(ItemName.herm_bag_unlock)
can_get_agv_rc = Has(ItemName.agua_unlock)
can_get_agv_hc = Has(ItemName.reducto_unlock)
can_get_agv_sip = Has(ItemName.www_box_unlock)
can_get_emmeline = Has(ItemName.agua_unlock)
can_get_neville = char_is_strong
can_get_prof_umbridge = can_use_dark_magic


# A Veiled Threat Logic
can_beat_avt = Has(ItemName.diffindo_unlock)
can_get_avt_rc = Has(ItemName.agua_unlock)
can_get_avt_hc = can_use_dark_magic
can_get_fudge_wizen = Has(ItemName.diffindo_unlock)
can_get_herm_jumper = Has(ItemName.agua_unlock)
can_get_lucius_death = can_use_dark_magic


# Out of Retirement Logic
can_access_oor_free = HasAll(ItemName.reducto_unlock, ItemName.apparition_unlock)
can_beat_oor = Has(ItemName.www_box_unlock)
can_get_oor_gc = can_use_dark_magic
can_get_oor_sc = Has(ItemName.agua_unlock) & can_use_dark_magic
can_get_oor_rc = HasAll(ItemName.apparition_unlock, ItemName.specs_unlock) & can_use_dark_magic
can_get_oor_hc = HasAll(ItemName.www_box_unlock, ItemName.diffindo_unlock) & can_use_dark_magic
can_get_oor_sip = HasAll(ItemName.www_box_unlock, ItemName.diffindo_unlock) & can_use_dark_magic
can_get_dumble_cursed = can_use_dark_magic
can_get_milk_man = Has(ItemName.herm_bag_unlock)
can_get_slug_pajamas = HasAll(ItemName.apparition_unlock) & can_use_dark_magic & can_use_key


# Just Desserts Logic
can_get_jd_sc = char_is_strong
can_get_jd_rc = HasAll(ItemName.delum_unlock, ItemName.herm_bag_unlock) & can_use_dark_magic
can_get_jd_hc = can_use_dark_magic
can_get_jd_sip = can_use_dark_magic
can_get_cormac_suit = Has(ItemName.agua_unlock)
can_get_harry_christ = HasAll(ItemName.herm_bag_unlock, ItemName.specs_unlock) & can_use_dark_magic
can_get_madam_rosmerta = can_use_dark_magic


# A Not So Merry Christmas Logic



def set_rules(world: "LHP2World"):
    set_entrance_rules(world)
    set_win_con(world)
    set_dt_logic(world)
    set_da_logic(world)
    set_foc_logic(world)
    set_kd_logic(world)
    set_agv_logic(world)
    set_avt_logic(world)
    set_jd_logic(world)


def set_entrance_rules(world):
    # Level Entrance Rules
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.dt), Has(ItemName.dt_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.da), Has(ItemName.da_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.foc), Has(ItemName.foc_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.kd), Has(ItemName.kd_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.agv), Has(ItemName.agv_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.avt), Has(ItemName.avt_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.oor), Has(ItemName.oor_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.jd), Has(ItemName.jd_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.ansmc), Has(ItemName.ansmc_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.lh), Has(ItemName.lh_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.ff), Has(ItemName.ff_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.thath), Has(ItemName.thath_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.tsh), Has(ItemName.tsh_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.mim), Has(ItemName.mim_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.igd), Has(ItemName.igd_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.sal), Has(ItemName.sal_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.ll), Has(ItemName.ll_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.dob), Has(ItemName.dob_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.ttd), Has(ItemName.ttd_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.bts), Has(ItemName.bts_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.bb), Has(ItemName.bb_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.fiend), Has(ItemName.fiend_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.st), Has(ItemName.st_unlock))
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.tfitp), Has(ItemName.tfitp_unlock))
    # Freeplay Entrance Rules
    world.set_rule(world.get_entrance(RegionName.foc + " -> " + RegionName.focf), Has(ItemName.focus_unlock))
    world.set_rule(world.get_entrance(RegionName.oor + " -> " + RegionName.oorf), can_access_oor_free)


def set_win_con(world):
    if world.options.EndGoal == EndGoal.option_defeat_voldemort:
        world.set_completion_rule(Has("Voldemort Defeated"))
    # if options.EndGoal == EndGoal.option_the_collector:
    #     world.completion_condition[player] =



def set_dt_logic(world):
    world.set_rule(world.get_location(LocationName.dt_sc), can_get_dt_sc)
    world.set_rule(world.get_location(LocationName.dt_hc), can_get_dt_hc)
    world.set_rule(world.get_location(LocationName.dt_sip), can_get_dt_sip)
    world.set_rule(world.get_location(LocationName.arthur_suit_token), can_get_arthur_suit)
    world.set_rule(world.get_location(LocationName.elphias_token), can_get_elphias)


def set_da_logic(world):
    world.set_rule(world.get_location(LocationName.da_beat), can_beat_da)
    world.set_rule(world.get_location(LocationName.da_tw), can_beat_da)
    world.set_rule(world.get_location(LocationName.da_gc), can_get_da_gc)
    world.set_rule(world.get_location(LocationName.da_sc), can_get_da_sc)
    world.set_rule(world.get_location(LocationName.da_rc), can_get_da_rc)
    world.set_rule(world.get_location(LocationName.da_hc), can_get_da_hc)
    world.set_rule(world.get_location(LocationName.da_sip), can_get_da_sip)
    world.set_rule(world.get_location(LocationName.cho_winter_token), can_get_cho_winter)
    world.set_rule(world.get_location(LocationName.herm_scarf_token), can_get_herm_scarf)
    world.set_rule(world.get_location(LocationName.neville_winter_token), can_get_neville_winter)


def set_foc_logic(world):
    world.set_rule(world.get_location(LocationName.foc_gc), can_get_foc_gc)
    world.set_rule(world.get_location(LocationName.foc_hc), can_get_foc_hc)
    world.set_rule(world.get_location(LocationName.foc_sip), can_get_foc_sip)
    world.set_rule(world.get_location(LocationName.molly_apron_token), can_get_molly_apron)
    world.set_rule(world.get_location(LocationName.snape_underwear_token), can_get_snape_under)


def set_kd_logic(world):
    world.set_rule(world.get_location(LocationName.kd_gc), can_get_kd_gc)
    world.set_rule(world.get_location(LocationName.kd_sc), can_get_kd_sc)
    world.set_rule(world.get_location(LocationName.kd_hc), can_get_kd_hc)
    world.set_rule(world.get_location(LocationName.kd_sip), can_get_kd_sip)
    world.set_rule(world.get_location(LocationName.kreacher_token), can_get_kreacher)
    world.set_rule(world.get_location(LocationName.sirius_black_token), can_get_sirius)


def set_agv_logic(world):
    world.set_rule(world.get_location(LocationName.agv_gc), can_get_agv_gc)
    world.set_rule(world.get_location(LocationName.agv_sc), can_get_agv_sc)
    world.set_rule(world.get_location(LocationName.agv_rc), can_get_agv_rc)
    world.set_rule(world.get_location(LocationName.agv_hc), can_get_agv_hc)
    world.set_rule(world.get_location(LocationName.agv_sip), can_get_agv_sip)
    world.set_rule(world.get_location(LocationName.emmeline_token), can_get_emmeline)
    world.set_rule(world.get_location(LocationName.neville_token), can_get_neville)
    world.set_rule(world.get_location(LocationName.prof_umbridge_token), can_get_prof_umbridge)


def set_avt_logic(world):
    world.set_rule(world.get_location(LocationName.avt_beat), can_beat_avt)
    world.set_rule(world.get_location(LocationName.avt_tw), can_beat_avt)
    world.set_rule(world.get_location(LocationName.avt_rc), can_get_avt_rc)
    world.set_rule(world.get_location(LocationName.avt_hc), can_get_avt_hc)
    world.set_rule(world.get_location(LocationName.fudge_wizengamot_token), can_get_fudge_wizen)
    world.set_rule(world.get_location(LocationName.herm_jumper_token), can_get_herm_jumper)
    world.set_rule(world.get_location(LocationName.lucius_death_eater_token), can_get_lucius_death)


def set_oor_logic(world):
    world.set_rule(world.get_location(LocationName.oor_beat), can_beat_oor)
    world.set_rule(world.get_location(LocationName.oor_tw), can_beat_oor)
    world.set_rule(world.get_location(LocationName.oor_gc), can_get_oor_gc)
    world.set_rule(world.get_location(LocationName.oor_sc), can_get_oor_sc)
    world.set_rule(world.get_location(LocationName.oor_rc), can_get_oor_rc)
    world.set_rule(world.get_location(LocationName.oor_hc), can_get_oor_hc)
    world.set_rule(world.get_location(LocationName.oor_sip), can_get_oor_sip)
    world.set_rule(world.get_location(LocationName.dumble_cursed_token), can_get_dumble_cursed)
    world.set_rule(world.get_location(LocationName.milk_man_token), can_get_milk_man)
    world.set_rule(world.get_location(LocationName.slughorn_pajamas_token), can_get_slug_pajamas)


def set_jd_logic(world):
    world.set_rule(world.get_location(LocationName.jd_sc), can_get_jd_sc)
    world.set_rule(world.get_location(LocationName.jd_rc), can_get_jd_rc)
    world.set_rule(world.get_location(LocationName.jd_hc), can_get_jd_hc)
    world.set_rule(world.get_location(LocationName.cormac_suit_token), can_get_cormac_suit)
    world.set_rule(world.get_location(LocationName.harry_christmas_token), can_get_harry_christ)
    world.set_rule(world.get_location(LocationName.madam_rosmerta_token), can_get_madam_rosmerta)
