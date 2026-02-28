from typing import TYPE_CHECKING, Any
from typing_extensions import override
import dataclasses

from Options import Option
from rule_builder.options import OptionFilter, Operator
from rule_builder.rules import Rule, Has, HasAll, True_, False_, And, Or, CanReachRegion, CanReachLocation

if TYPE_CHECKING:
    from . import LHP2World

from .Names import LocationName, ItemName, RegionName
from .Options import LHP2Options, EndGoal, HardPurchases
from .Locations import character_location_table, red_brick_purch_table, bb_gb_loc_table

# Helper Rules
can_use_dark_magic = (Has(ItemName.alecto_play) | Has(ItemName.amycus_play) | Has(ItemName.dolohov_play) |
                      Has(ItemName.bellatrix_play) | Has(ItemName.bellatrix_azka_play) | Has(
            ItemName.death_eater_play) |
                      Has(ItemName.fenrir_play) | Has(ItemName.grindel_old_play) | Has(ItemName.grindel_young_play) |
                      Has(ItemName.lord_voldemort_play) | Has(ItemName.lucius_play) | Has(
            ItemName.lucius_death_eater_play) |
                      Has(ItemName.black_play) | Has(ItemName.pius_play) | Has(ItemName.scabior_play) |
                      Has(ItemName.snatcher_play) | Has(ItemName.rowle_play) | Has(ItemName.tom_riddle_play))

can_use_spanner = (Has(ItemName.arthur_play) | Has(ItemName.arthur_suit_play) | Has(ItemName.arthur_cardigan_play) |
                   Has(ItemName.arthur_torn_suit_play))

can_use_key = Has(ItemName.bogrod_play) | Has(ItemName.cole_play) | Has(ItemName.griphook_play)

char_is_strong = (Has(ItemName.dudley_play) | Has(ItemName.dudley_grey_play) | Has(ItemName.dudley_shirt_play) |
                  Has(ItemName.fenrir_play) | Has(ItemName.fang_play) | Has(ItemName.hagrid_play) |
                  Has(ItemName.hagrid_wed_play) | Has(ItemName.remus_lupin_play) | Has(ItemName.sirius_black_play) |
                  Has(ItemName.sirius_azkaban_play) | Has(ItemName.super_strength_unlock))

has_all_horcruxes = HasAll(ItemName.tr_diary, ItemName.gaunt_ring, ItemName.locket, ItemName.cup,
                           ItemName.diadem, ItemName.nagini)
defeat_voldemort = Has("Voldemort Defeated")

# Dark Times Logic
can_get_dt_sc = Has(ItemName.diffindo_unlock)
can_get_dt_hc = Has(ItemName.www_box_unlock)
can_get_dt_sip = can_use_dark_magic
can_get_arthur_suit = can_use_dark_magic
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
                 & can_use_dark_magic)
can_get_kd_hc = HasAll(ItemName.reducto_unlock, ItemName.diffindo_unlock)
can_get_kd_sip = Has(ItemName.reducto_unlock)
can_get_kreacher = can_use_dark_magic
can_get_sirius = Has(ItemName.agua_unlock)

# A Giant Virtuoso
can_get_agv_gc = can_use_key
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
can_get_oor_gc = can_use_spanner
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
can_access_ansmc_free = HasAll(ItemName.reducto_unlock, ItemName.specs_unlock, ItemName.agua_unlock)
can_get_ansmc_gc = Has(ItemName.apparition_unlock) & can_use_key
can_get_ansmc_sc = can_use_dark_magic
can_get_bill_wedding = HasAll(ItemName.reducto_unlock, ItemName.delum_unlock)

# Love Hurts Logic
can_access_lh_free = HasAll(ItemName.reducto_unlock, ItemName.agua_unlock)
can_beat_lh = HasAll(ItemName.diffindo_unlock, ItemName.www_box_unlock)
can_get_lh_gc = Has(ItemName.www_box_unlock) & can_use_spanner
can_get_lh_sc = Has(ItemName.www_box_unlock) & can_use_dark_magic
can_get_lh_rc = Has(ItemName.reducto_unlock) & can_use_key
can_get_lh_hc = char_is_strong
can_get_lh_sip = can_use_dark_magic
can_get_draco_suit = Has(ItemName.delum_unlock) & can_use_dark_magic
can_get_ginny = Has(ItemName.agua_unlock)
can_get_prof_slug = char_is_strong

# Felix Felicis Logic
can_access_ff_free = HasAll(ItemName.reducto_unlock, ItemName.agua_unlock)
can_beat_ff = Has(ItemName.diffindo_unlock)
can_get_ff_sc = can_use_key
can_get_ff_rc = can_use_dark_magic
can_get_ff_hc = can_use_dark_magic
can_get_ff_sip = Has(ItemName.www_box_unlock)
can_get_hagrid = Has(ItemName.herm_bag_unlock) & can_use_dark_magic
can_get_prof_sprout = HasAll(ItemName.reducto_unlock, ItemName.specs_unlock)

# The Horcrux and the Hand Logic
can_access_thath_free = HasAll(ItemName.apparition_unlock, ItemName.diffindo_unlock)
can_beat_thath = HasAll(ItemName.reducto_unlock, ItemName.agua_unlock)
can_get_thath_sc = char_is_strong
can_get_thath_rc = HasAll(ItemName.apparition_unlock, ItemName.herm_bag_unlock)
can_get_thath_hc = HasAll(ItemName.reducto_unlock, ItemName.delum_unlock)
can_get_thath_sip = HasAll(ItemName.reducto_unlock, ItemName.agua_unlock)
can_get_hagrid_wed = HasAll(ItemName.reducto_unlock, ItemName.agua_unlock) & char_is_strong
can_get_prof_dumble = can_use_dark_magic
can_get_tr_orphan = can_use_dark_magic

# The Seven Harry's Logic
can_access_tsh_free = HasAll(ItemName.reducto_unlock, ItemName.agua_unlock,
                             ItemName.herm_bag_unlock, ItemName.delum_unlock)
can_get_tsh_gc = Has(ItemName.reducto_unlock)
can_get_mad_eye = HasAll(ItemName.reducto_unlock, ItemName.agua_unlock) & can_use_dark_magic
can_get_ron_wed = HasAll(ItemName.apparition_unlock, ItemName.specs_unlock)

# Magic is Might Logic
can_access_mim_free = HasAll(ItemName.reducto_unlock, ItemName.diffindo_unlock, ItemName.delum_unlock,
                             ItemName.agua_unlock)
can_get_mim_rc = (HasAll(ItemName.reducto_unlock, ItemName.diffindo_unlock, ItemName.delum_unlock) &
                  can_use_key)
can_get_mim_hc = can_use_dark_magic
can_get_mim_sip = can_use_dark_magic
can_get_ron_reg = HasAll(ItemName.reducto_unlock, ItemName.diffindo_unlock)

# In Grave Danger Logic
can_access_igd_free = HasAll(ItemName.diffindo_unlock, ItemName.reducto_unlock, ItemName.herm_bag_unlock)
can_beat_igd = Has(ItemName.agua_unlock)
can_get_igd_gc = HasAll(ItemName.www_box_unlock, ItemName.specs_unlock)
can_get_igd_sc = can_use_dark_magic
can_get_igd_rc = HasAll(ItemName.www_box_unlock, ItemName.delum_unlock, ItemName.herm_bag_unlock)
can_get_igd_sip = can_use_dark_magic
can_get_bathilda_snake = can_use_dark_magic
can_get_harry_god_hollow = Has(ItemName.agua_unlock) & can_use_dark_magic
can_get_lily = Has(ItemName.www_box_unlock)

# Sword and Locket Logic
can_beat_sal = HasAll(ItemName.apparition_unlock, ItemName.diffindo_unlock)
can_get_sal_gc = can_use_dark_magic
can_get_sal_sc = Has(ItemName.herm_bag_unlock)
can_get_sal_rc = Has(ItemName.www_box_unlock)
can_get_sal_sip = Has(ItemName.herm_bag_unlock) & can_use_dark_magic
can_get_herm_gray_coat = HasAll(ItemName.herm_bag_unlock, ItemName.specs_unlock)


# Lovegood's Lunacy Logic
can_access_ll_free = HasAll(ItemName.agua_unlock, ItemName.herm_bag_unlock)
can_access_lunas_room = Or(char_is_strong,
                           HasAll(ItemName.specs_unlock, ItemName.diffindo_unlock, ItemName.reducto_unlock))
can_beat_ll = can_access_lunas_room & Has(ItemName.reducto_unlock)
can_get_ll_rc = can_access_lunas_room & Has(ItemName.delum_unlock)
can_get_ll_hc = can_use_spanner
can_get_skeleton = can_use_dark_magic
can_get_xeno_luna = HasAll(ItemName.www_box_unlock, ItemName.specs_unlock) & can_use_dark_magic

# Dobby! Logic
can_access_dob_free = Has(ItemName.specs_unlock)
can_get_dob_gc = Has(ItemName.diffindo_unlock)
can_get_dob_rc = can_use_dark_magic
can_get_dob_sip = Has(ItemName.reducto_unlock)
can_get_dobby = can_use_dark_magic
can_get_wormtail = can_use_dark_magic

# The Thief's Downfall Logic
can_access_ttd_free = Has(ItemName.herm_bag_unlock)
can_beat_ttd = HasAll(ItemName.reducto_unlock, ItemName.agua_unlock, ItemName.delum_unlock)
can_get_ttd_gc = Has(ItemName.diffindo_unlock)
can_get_ttd_sc = can_use_dark_magic
can_get_ttd_rc = Has(ItemName.specs_unlock) & char_is_strong
can_get_ttd_hc = (HasAll(ItemName.reducto_unlock, ItemName.agua_unlock, ItemName.delum_unlock, ItemName.specs_unlock)
                  & char_is_strong)
can_get_ttd_sip = can_use_dark_magic
can_get_bogrod = can_use_dark_magic
can_get_griphook = can_use_dark_magic & Has(ItemName.www_box_unlock)
can_get_herm_gringotts = can_use_dark_magic

# Shop Logic
has_high_multi = (Has(ItemName.score_x6_unlock) | Has(ItemName.score_x8_unlock) | Has(ItemName.score_x10_unlock) |
                  HasAll(ItemName.score_x2_unlock, ItemName.score_x4_unlock))
has_low_multi = Has(ItemName.score_x2_unlock) | Has(ItemName.score_x4_unlock) | has_high_multi


def from_option(option: type[Option], value: Any, operator: Operator = "eq") -> Rule:
    return True_(options=[OptionFilter(option, value, operator)])


def has_multi_for_shop(location_name: str) -> Rule:
    return Or(from_option(HardPurchases, 1), HasMultiplier(location_name))


@dataclasses.dataclass
class HasMultiplier(Rule, game="Lego Harry Potter 5-7"):
    location_name: str

    @override
    def _instantiate(self, world: "LHP2World") -> Rule.Resolved:
        # Look up the price
        data = character_location_table[self.location_name]
        price = data.price

        # Get Multiplier Requirements
        low = world.options.LowMultiplierPriceMinimum
        high = world.options.HighMultiplierMinimum

        # Compare and Return
        if price < low:
            return True_().resolve(world)
        elif price < high:
            return has_low_multi.resolve(world)
        else:
            return has_high_multi.resolve(world)


def set_rules(world: "LHP2World"):
    set_entrance_rules(world)
    set_event_logic(world)
    set_win_con(world)
    # Y5
    set_dt_logic(world)
    set_da_logic(world)
    set_foc_logic(world)
    set_kd_logic(world)
    set_agv_logic(world)
    set_avt_logic(world)
    # Y6
    set_oor_logic(world)
    set_jd_logic(world)
    set_ansmc_logic(world)
    set_lh_logic(world)
    set_ff_logic(world)
    set_thath_logic(world)
    # Y7
    set_tsh_logic(world)
    set_mim_logic(world)
    set_igd_logic(world)
    set_sal_logic(world)
    set_ll_logic(world)
    set_dob_logic(world)
    #Y8
    set_ttd_logic(world)
    # Shop Logic
    set_shop_rules(world)


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
    world.set_rule(world.get_entrance(RegionName.ansmc + " -> " + RegionName.ansmcf), can_access_ansmc_free)
    world.set_rule(world.get_entrance(RegionName.lh + " -> " + RegionName.lhf), can_access_lh_free)
    world.set_rule(world.get_entrance(RegionName.ff + " -> " + RegionName.fff), can_access_ff_free)
    world.set_rule(world.get_entrance(RegionName.thath + " -> " + RegionName.thathf), can_access_thath_free)
    world.set_rule(world.get_entrance(RegionName.tsh + " -> " + RegionName.tshf), can_access_tsh_free)
    world.set_rule(world.get_entrance(RegionName.mim + " -> " + RegionName.mimf), can_access_mim_free)
    world.set_rule(world.get_entrance(RegionName.igd + " -> " + RegionName.igdf), can_access_igd_free)
    world.set_rule(world.get_entrance(RegionName.ll + " -> " + RegionName.llf), can_access_ll_free)
    world.set_rule(world.get_entrance(RegionName.dob + " -> " + RegionName.dobf), can_access_dob_free)
    world.set_rule(world.get_entrance(RegionName.ttd + " -> " + RegionName.ttdf), can_access_ttd_free)


def set_event_logic(world):
    world.set_rule(world.get_location("Defeat Voldemort"), has_all_horcruxes)


def set_win_con(world):
    if world.options.EndGoal == EndGoal.option_defeat_voldemort:
        world.set_completion_rule(defeat_voldemort)
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


def set_ansmc_logic(world):
    world.set_rule(world.get_location(LocationName.ansmc_gc), can_get_ansmc_gc)
    world.set_rule(world.get_location(LocationName.ansmc_sc), can_get_ansmc_sc)
    world.set_rule(world.get_location(LocationName.bill_wedding_token), can_get_bill_wedding)


def set_lh_logic(world):
    world.set_rule(world.get_location(LocationName.lh_beat), can_beat_lh)
    world.set_rule(world.get_location(LocationName.lh_tw), can_beat_lh)
    world.set_rule(world.get_location(LocationName.lh_gc), can_get_lh_gc)
    world.set_rule(world.get_location(LocationName.lh_sc), can_get_lh_sc)
    world.set_rule(world.get_location(LocationName.lh_rc), can_get_lh_rc)
    world.set_rule(world.get_location(LocationName.lh_hc), can_get_lh_hc)
    world.set_rule(world.get_location(LocationName.lh_sip), can_get_lh_sip)
    world.set_rule(world.get_location(LocationName.draco_suit_token), can_get_draco_suit)
    world.set_rule(world.get_location(LocationName.ginny_token), can_get_ginny)
    world.set_rule(world.get_location(LocationName.prof_slughorn_token), can_get_prof_slug)


def set_ff_logic(world):
    world.set_rule(world.get_location(LocationName.ff_beat), can_beat_ff)
    world.set_rule(world.get_location(LocationName.ff_tw), can_beat_ff)
    world.set_rule(world.get_location(LocationName.ff_sc), can_get_ff_sc)
    world.set_rule(world.get_location(LocationName.ff_rc), can_get_ff_rc)
    world.set_rule(world.get_location(LocationName.ff_hc), can_get_ff_hc)
    world.set_rule(world.get_location(LocationName.ff_sip), can_get_ff_sip)
    world.set_rule(world.get_location(LocationName.hagrid_token), can_get_hagrid)
    world.set_rule(world.get_location(LocationName.prof_sprout_token), can_get_prof_sprout)


def set_thath_logic(world):
    world.set_rule(world.get_location(LocationName.thath_beat), can_beat_thath)
    world.set_rule(world.get_location(LocationName.thath_tw), can_beat_thath)
    world.set_rule(world.get_location(LocationName.thath_sc), can_get_thath_sc)
    world.set_rule(world.get_location(LocationName.thath_rc), can_get_thath_rc)
    world.set_rule(world.get_location(LocationName.thath_hc), can_get_thath_hc)
    world.set_rule(world.get_location(LocationName.thath_sip), can_get_thath_sip)
    world.set_rule(world.get_location(LocationName.hagrid_wed_token), can_get_hagrid_wed)
    world.set_rule(world.get_location(LocationName.prof_dumble_token), can_get_prof_dumble)
    world.set_rule(world.get_location(LocationName.tr_orphanage_token), can_get_tr_orphan)


def set_tsh_logic(world):
    world.set_rule(world.get_location(LocationName.tsh_gc), can_get_tsh_gc)
    world.set_rule(world.get_location(LocationName.madeye_token), can_get_mad_eye)
    world.set_rule(world.get_location(LocationName.ron_wedding_token), can_get_ron_wed)


def set_mim_logic(world):
    world.set_rule(world.get_location(LocationName.mim_rc), can_get_mim_rc)
    world.set_rule(world.get_location(LocationName.mim_hc), can_get_mim_hc)
    world.set_rule(world.get_location(LocationName.mim_sip), can_get_mim_sip)
    world.set_rule(world.get_location(LocationName.ron_reg_cattermole_token), can_get_ron_reg)


def set_igd_logic(world):
    world.set_rule(world.get_location(LocationName.igd_beat), can_beat_igd)
    world.set_rule(world.get_location(LocationName.igd_tw), can_beat_igd)
    world.set_rule(world.get_location(LocationName.igd_gc), can_get_igd_gc)
    world.set_rule(world.get_location(LocationName.igd_sc), can_get_igd_sc)
    world.set_rule(world.get_location(LocationName.igd_rc), can_get_igd_rc)
    world.set_rule(world.get_location(LocationName.igd_sip), can_get_igd_sip)
    world.set_rule(world.get_location(LocationName.bathilda_snake_token), can_get_bathilda_snake)
    world.set_rule(world.get_location(LocationName.harry_godric_token), can_get_harry_god_hollow)
    world.set_rule(world.get_location(LocationName.lily_token), can_get_lily)


def set_sal_logic(world):
    world.set_rule(world.get_location(LocationName.sal_beat), can_beat_sal)
    world.set_rule(world.get_location(LocationName.sal_tw), can_beat_sal)
    world.set_rule(world.get_location(LocationName.sal_gc), can_get_sal_gc)
    world.set_rule(world.get_location(LocationName.sal_sc), can_get_sal_sc)
    world.set_rule(world.get_location(LocationName.sal_rc), can_get_sal_rc)
    world.set_rule(world.get_location(LocationName.sal_sip), can_get_sal_sip)
    world.set_rule(world.get_location(LocationName.herm_grey_coat_token), can_get_herm_gray_coat)


def set_ll_logic(world):
    world.set_rule(world.get_location(LocationName.ll_beat), can_beat_ll)
    world.set_rule(world.get_location(LocationName.ll_tw), can_beat_ll)
    world.set_rule(world.get_location(LocationName.ll_rc), can_get_ll_rc)
    world.set_rule(world.get_location(LocationName.ll_hc), can_get_ll_hc)
    world.set_rule(world.get_location(LocationName.skeleton_token), can_get_skeleton)
    world.set_rule(world.get_location(LocationName.xeno_luna_token), can_get_xeno_luna)


def set_dob_logic(world):
    world.set_rule(world.get_location(LocationName.dob_gc), can_get_dob_gc)
    world.set_rule(world.get_location(LocationName.dob_rc), can_get_dob_rc)
    world.set_rule(world.get_location(LocationName.dob_sip), can_get_dob_sip)
    world.set_rule(world.get_location(LocationName.dobby_token), can_get_dobby)
    world.set_rule(world.get_location(LocationName.wormtail_token), can_get_wormtail)


def set_ttd_logic(world):
    world.set_rule(world.get_location(LocationName.ttd_beat), can_beat_ttd)
    world.set_rule(world.get_location(LocationName.ttd_tw), can_beat_ttd)
    world.set_rule(world.get_location(LocationName.ttd_gc), can_get_ttd_gc)
    world.set_rule(world.get_location(LocationName.ttd_sc), can_get_ttd_sc)
    world.set_rule(world.get_location(LocationName.ttd_rc), can_get_ttd_rc)
    world.set_rule(world.get_location(LocationName.ttd_hc), can_get_ttd_hc)
    world.set_rule(world.get_location(LocationName.ttd_sip), can_get_ttd_sip)
    world.set_rule(world.get_location(LocationName.bogrod_token), can_get_bogrod)
    world.set_rule(world.get_location(LocationName.griphook_token), can_get_griphook)
    world.set_rule(world.get_location(LocationName.herm_gringotts_token), can_get_herm_gringotts)


def set_shop_rules(world):
    world.set_rule(world.get_location(LocationName.hagrid_purch), has_multi_for_shop(LocationName.hagrid_purch))
    world.set_rule(world.get_location(LocationName.fang_purch), has_multi_for_shop(LocationName.fang_purch))
    world.set_rule(world.get_location(LocationName.hagrid_wed_purch), has_multi_for_shop(LocationName.hagrid_wed_purch))
    world.set_rule(world.get_location(LocationName.prof_flit_purch), has_multi_for_shop(LocationName.prof_flit_purch))
    world.set_rule(world.get_location(LocationName.madam_malk_purch), has_multi_for_shop(LocationName.madam_malk_purch))
    world.set_rule(world.get_location(LocationName.dobby_purch), has_multi_for_shop(LocationName.dobby_purch))
    world.set_rule(world.get_location(LocationName.kreacher_purch), has_multi_for_shop(LocationName.kreacher_purch))
    world.set_rule(world.get_location(LocationName.tr_orphanage_purch),
                   has_multi_for_shop(LocationName.tr_orphanage_purch))
    world.set_rule(world.get_location(LocationName.bogrod_purch), has_multi_for_shop(LocationName.bogrod_purch))
    world.set_rule(world.get_location(LocationName.mund_fletch_purch),
                   has_multi_for_shop(LocationName.mund_fletch_purch))
    world.set_rule(world.get_location(LocationName.griphook_purch), has_multi_for_shop(LocationName.griphook_purch))
    world.set_rule(world.get_location(LocationName.prof_mcgon_purch), has_multi_for_shop(LocationName.prof_mcgon_purch))
    world.set_rule(world.get_location(LocationName.madam_pince_purch),
                   has_multi_for_shop(LocationName.madam_pince_purch))
    world.set_rule(world.get_location(LocationName.prof_sprout_purch),
                   has_multi_for_shop(LocationName.prof_sprout_purch))
    world.set_rule(world.get_location(LocationName.madam_pomfrey_purch),
                   has_multi_for_shop(LocationName.madam_pomfrey_purch))
    world.set_rule(world.get_location(LocationName.prof_trelawney_purch),
                   has_multi_for_shop(LocationName.prof_trelawney_purch))
    world.set_rule(world.get_location(LocationName.madam_rosmerta_purch),
                   has_multi_for_shop(LocationName.madam_rosmerta_purch))
    world.set_rule(world.get_location(LocationName.fat_friar_purch), has_multi_for_shop(LocationName.fat_friar_purch))
    world.set_rule(world.get_location(LocationName.grey_lady_purch), has_multi_for_shop(LocationName.grey_lady_purch))
    world.set_rule(world.get_location(LocationName.fat_lady_purch), has_multi_for_shop(LocationName.fat_lady_purch))
    world.set_rule(world.get_location(LocationName.herm_ball_purch), has_multi_for_shop(LocationName.herm_ball_purch))
    world.set_rule(world.get_location(LocationName.bellatrix_purch), has_multi_for_shop(LocationName.bellatrix_purch))
    world.set_rule(world.get_location(LocationName.emmeline_purch), has_multi_for_shop(LocationName.emmeline_purch))
    world.set_rule(world.get_location(LocationName.narcissa_purch), has_multi_for_shop(LocationName.narcissa_purch))
    world.set_rule(world.get_location(LocationName.mcgon_pyjamas_purch),
                   has_multi_for_shop(LocationName.mcgon_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.mary_cattermole_purch),
                   has_multi_for_shop(LocationName.mary_cattermole_purch))
    world.set_rule(world.get_location(LocationName.mcgon_black_purch),
                   has_multi_for_shop(LocationName.mcgon_black_purch))
    world.set_rule(world.get_location(LocationName.herm_gringotts_purch),
                   has_multi_for_shop(LocationName.herm_gringotts_purch))
    world.set_rule(world.get_location(LocationName.prof_grubbly_purch),
                   has_multi_for_shop(LocationName.prof_grubbly_purch))
    world.set_rule(world.get_location(LocationName.bellatrix_azka_purch),
                   has_multi_for_shop(LocationName.bellatrix_azka_purch))
    world.set_rule(world.get_location(LocationName.death_eater_purch),
                   has_multi_for_shop(LocationName.death_eater_purch))
    world.set_rule(world.get_location(LocationName.dudley_grey_purch),
                   has_multi_for_shop(LocationName.dudley_grey_purch))
    world.set_rule(world.get_location(LocationName.prof_dumble_purch),
                   has_multi_for_shop(LocationName.prof_dumble_purch))
    world.set_rule(world.get_location(LocationName.argus_purch), has_multi_for_shop(LocationName.argus_purch))
    world.set_rule(world.get_location(LocationName.madam_hooch_purch),
                   has_multi_for_shop(LocationName.madam_hooch_purch))
    world.set_rule(world.get_location(LocationName.crabbe_purch), has_multi_for_shop(LocationName.crabbe_purch))
    world.set_rule(world.get_location(LocationName.goyle_purch), has_multi_for_shop(LocationName.goyle_purch))
    world.set_rule(world.get_location(LocationName.ginny_purch), has_multi_for_shop(LocationName.ginny_purch))
    world.set_rule(world.get_location(LocationName.arthur_purch), has_multi_for_shop(LocationName.arthur_purch))
    world.set_rule(world.get_location(LocationName.katie_purch), has_multi_for_shop(LocationName.katie_purch))
    world.set_rule(world.get_location(LocationName.lily_purch), has_multi_for_shop(LocationName.lily_purch))
    world.set_rule(world.get_location(LocationName.bloody_baron_purch),
                   has_multi_for_shop(LocationName.bloody_baron_purch))
    world.set_rule(world.get_location(LocationName.fudge_purch), has_multi_for_shop(LocationName.fudge_purch))
    world.set_rule(world.get_location(LocationName.justin_purch), has_multi_for_shop(LocationName.justin_purch))
    world.set_rule(world.get_location(LocationName.cho_purch), has_multi_for_shop(LocationName.cho_purch))
    world.set_rule(world.get_location(LocationName.dean_purch), has_multi_for_shop(LocationName.dean_purch))
    world.set_rule(world.get_location(LocationName.draco_purch), has_multi_for_shop(LocationName.draco_purch))
    world.set_rule(world.get_location(LocationName.lucius_purch), has_multi_for_shop(LocationName.lucius_purch))
    world.set_rule(world.get_location(LocationName.draco_suit_purch), has_multi_for_shop(LocationName.draco_suit_purch))
    world.set_rule(world.get_location(LocationName.harry_pyjamas_purch),
                   has_multi_for_shop(LocationName.harry_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.myrtle_purch), has_multi_for_shop(LocationName.myrtle_purch))
    world.set_rule(world.get_location(LocationName.james_ghost_purch),
                   has_multi_for_shop(LocationName.james_ghost_purch))
    world.set_rule(world.get_location(LocationName.madeye_purch), has_multi_for_shop(LocationName.madeye_purch))
    world.set_rule(world.get_location(LocationName.hannah_purch), has_multi_for_shop(LocationName.hannah_purch))
    world.set_rule(world.get_location(LocationName.kingsley_purch), has_multi_for_shop(LocationName.kingsley_purch))
    world.set_rule(world.get_location(LocationName.aberforth_purch), has_multi_for_shop(LocationName.aberforth_purch))
    world.set_rule(world.get_location(LocationName.runcorn_purch), has_multi_for_shop(LocationName.runcorn_purch))
    world.set_rule(world.get_location(LocationName.alecto_purch), has_multi_for_shop(LocationName.alecto_purch))
    world.set_rule(world.get_location(LocationName.amycus_purch), has_multi_for_shop(LocationName.amycus_purch))
    world.set_rule(world.get_location(LocationName.anthony_purch), has_multi_for_shop(LocationName.anthony_purch))
    world.set_rule(world.get_location(LocationName.bathilda_snake_purch),
                   has_multi_for_shop(LocationName.bathilda_snake_purch))
    world.set_rule(world.get_location(LocationName.blaise_purch), has_multi_for_shop(LocationName.blaise_purch))
    world.set_rule(world.get_location(LocationName.charity_purch), has_multi_for_shop(LocationName.charity_purch))
    world.set_rule(world.get_location(LocationName.charlie_purch), has_multi_for_shop(LocationName.charlie_purch))
    world.set_rule(world.get_location(LocationName.cormac_purch), has_multi_for_shop(LocationName.cormac_purch))
    world.set_rule(world.get_location(LocationName.dedalus_purch), has_multi_for_shop(LocationName.dedalus_purch))
    world.set_rule(world.get_location(LocationName.dirk_purch), has_multi_for_shop(LocationName.dirk_purch))
    world.set_rule(world.get_location(LocationName.dolohov_purch), has_multi_for_shop(LocationName.dolohov_purch))
    world.set_rule(world.get_location(LocationName.dragomir_purch), has_multi_for_shop(LocationName.dragomir_purch))
    world.set_rule(world.get_location(LocationName.elphias_purch), has_multi_for_shop(LocationName.elphias_purch))
    world.set_rule(world.get_location(LocationName.fenrir_purch), has_multi_for_shop(LocationName.fenrir_purch))
    world.set_rule(world.get_location(LocationName.grindel_young_purch),
                   has_multi_for_shop(LocationName.grindel_young_purch))
    world.set_rule(world.get_location(LocationName.grindel_old_purch),
                   has_multi_for_shop(LocationName.grindel_old_purch))
    world.set_rule(world.get_location(LocationName.gregorovitch_purch),
                   has_multi_for_shop(LocationName.gregorovitch_purch))
    world.set_rule(world.get_location(LocationName.hestia_purch), has_multi_for_shop(LocationName.hestia_purch))
    world.set_rule(world.get_location(LocationName.prof_slughorn_purch),
                   has_multi_for_shop(LocationName.prof_slughorn_purch))
    world.set_rule(world.get_location(LocationName.james_young_purch),
                   has_multi_for_shop(LocationName.james_young_purch))
    world.set_rule(world.get_location(LocationName.lavender_purch), has_multi_for_shop(LocationName.lavender_purch))
    world.set_rule(world.get_location(LocationName.mafalda_purch), has_multi_for_shop(LocationName.mafalda_purch))
    world.set_rule(world.get_location(LocationName.belby_purch), has_multi_for_shop(LocationName.belby_purch))
    world.set_rule(world.get_location(LocationName.luna_purple_coat_purch),
                   has_multi_for_shop(LocationName.luna_purple_coat_purch))
    world.set_rule(world.get_location(LocationName.herm_grey_coat_purch),
                   has_multi_for_shop(LocationName.herm_grey_coat_purch))
    world.set_rule(world.get_location(LocationName.harry_godric_purch),
                   has_multi_for_shop(LocationName.harry_godric_purch))
    world.set_rule(world.get_location(LocationName.prof_umbridge_purch),
                   has_multi_for_shop(LocationName.prof_umbridge_purch))
    world.set_rule(world.get_location(LocationName.fred_purch), has_multi_for_shop(LocationName.fred_purch))
    world.set_rule(world.get_location(LocationName.george_purch), has_multi_for_shop(LocationName.george_purch))
    world.set_rule(world.get_location(LocationName.molly_apron_purch),
                   has_multi_for_shop(LocationName.molly_apron_purch))
    world.set_rule(world.get_location(LocationName.crabbe_jumper_purch),
                   has_multi_for_shop(LocationName.crabbe_jumper_purch))
    world.set_rule(world.get_location(LocationName.draco_sweater_purch),
                   has_multi_for_shop(LocationName.draco_sweater_purch))
    world.set_rule(world.get_location(LocationName.goyle_jumper_purch),
                   has_multi_for_shop(LocationName.goyle_jumper_purch))
    world.set_rule(world.get_location(LocationName.milk_man_purch), has_multi_for_shop(LocationName.milk_man_purch))
    world.set_rule(world.get_location(LocationName.twin_2_purch), has_multi_for_shop(LocationName.twin_2_purch))
    world.set_rule(world.get_location(LocationName.herm_mafalda_purch),
                   has_multi_for_shop(LocationName.herm_mafalda_purch))
    world.set_rule(world.get_location(LocationName.ministry_guard_purch),
                   has_multi_for_shop(LocationName.ministry_guard_purch))
    world.set_rule(world.get_location(LocationName.harry_winter_purch),
                   has_multi_for_shop(LocationName.harry_winter_purch))
    world.set_rule(world.get_location(LocationName.arthur_torn_suit_purch),
                   has_multi_for_shop(LocationName.arthur_torn_suit_purch))
    world.set_rule(world.get_location(LocationName.fred_winter_purch),
                   has_multi_for_shop(LocationName.fred_winter_purch))
    world.set_rule(world.get_location(LocationName.cho_winter_purch), has_multi_for_shop(LocationName.cho_winter_purch))
    world.set_rule(world.get_location(LocationName.george_winter_purch),
                   has_multi_for_shop(LocationName.george_winter_purch))
    world.set_rule(world.get_location(LocationName.herm_scarf_purch), has_multi_for_shop(LocationName.herm_scarf_purch))
    world.set_rule(world.get_location(LocationName.luna_blue_jumper_purch),
                   has_multi_for_shop(LocationName.luna_blue_jumper_purch))
    world.set_rule(world.get_location(LocationName.fred_owls_purch), has_multi_for_shop(LocationName.fred_owls_purch))
    world.set_rule(world.get_location(LocationName.fred_pyjamas_purch),
                   has_multi_for_shop(LocationName.fred_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.george_owls_purch),
                   has_multi_for_shop(LocationName.george_owls_purch))
    world.set_rule(world.get_location(LocationName.george_pyjamas_purch),
                   has_multi_for_shop(LocationName.george_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.herm_jumper_purch),
                   has_multi_for_shop(LocationName.herm_jumper_purch))
    world.set_rule(world.get_location(LocationName.fudge_wizengamot_purch),
                   has_multi_for_shop(LocationName.fudge_wizengamot_purch))
    world.set_rule(world.get_location(LocationName.dudley_purch), has_multi_for_shop(LocationName.dudley_purch))
    world.set_rule(world.get_location(LocationName.gang_mem_purch), has_multi_for_shop(LocationName.gang_mem_purch))
    world.set_rule(world.get_location(LocationName.harry_albert_runcorn_purch),
                   has_multi_for_shop(LocationName.harry_albert_runcorn_purch))
    world.set_rule(world.get_location(LocationName.harry_brown_jacket_purch),
                   has_multi_for_shop(LocationName.harry_brown_jacket_purch))
    world.set_rule(world.get_location(LocationName.dumble_cursed_purch),
                   has_multi_for_shop(LocationName.dumble_cursed_purch))
    world.set_rule(world.get_location(LocationName.lucius_death_eater_purch),
                   has_multi_for_shop(LocationName.lucius_death_eater_purch))
    world.set_rule(world.get_location(LocationName.luna_purch), has_multi_for_shop(LocationName.luna_purch))
    world.set_rule(world.get_location(LocationName.umbridge_wizengamot_purch),
                   has_multi_for_shop(LocationName.umbridge_wizengamot_purch))
    world.set_rule(world.get_location(LocationName.dolohov_workman_purch),
                   has_multi_for_shop(LocationName.dolohov_workman_purch))
    world.set_rule(world.get_location(LocationName.michael_purch), has_multi_for_shop(LocationName.michael_purch))
    world.set_rule(world.get_location(LocationName.dean_winter_purch),
                   has_multi_for_shop(LocationName.dean_winter_purch))
    world.set_rule(world.get_location(LocationName.arthur_cardigan_purch),
                   has_multi_for_shop(LocationName.arthur_cardigan_purch))
    world.set_rule(world.get_location(LocationName.luna_pink_dress_purch),
                   has_multi_for_shop(LocationName.luna_pink_dress_purch))
    world.set_rule(world.get_location(LocationName.marietta_purch), has_multi_for_shop(LocationName.marietta_purch))
    world.set_rule(world.get_location(LocationName.dumble_young_purch),
                   has_multi_for_shop(LocationName.dumble_young_purch))
    world.set_rule(world.get_location(LocationName.slughorn_young_purch),
                   has_multi_for_shop(LocationName.slughorn_young_purch))
    world.set_rule(world.get_location(LocationName.slughorn_pajamas_purch),
                   has_multi_for_shop(LocationName.slughorn_pajamas_purch))
    world.set_rule(world.get_location(LocationName.lily_young_casual_purch),
                   has_multi_for_shop(LocationName.lily_young_casual_purch))
    world.set_rule(world.get_location(LocationName.ginny_dress_purch),
                   has_multi_for_shop(LocationName.ginny_dress_purch))
    world.set_rule(world.get_location(LocationName.ginny_pyjamas_purch),
                   has_multi_for_shop(LocationName.ginny_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.blaise_black_shirt_purch),
                   has_multi_for_shop(LocationName.blaise_black_shirt_purch))
    world.set_rule(world.get_location(LocationName.cormac_suit_purch),
                   has_multi_for_shop(LocationName.cormac_suit_purch))
    world.set_rule(world.get_location(LocationName.muggle_orphan_purch),
                   has_multi_for_shop(LocationName.muggle_orphan_purch))
    world.set_rule(world.get_location(LocationName.luna_overalls_purch),
                   has_multi_for_shop(LocationName.luna_overalls_purch))
    world.set_rule(world.get_location(LocationName.molly_purch), has_multi_for_shop(LocationName.molly_purch))
    world.set_rule(world.get_location(LocationName.herm_cardigan_purch),
                   has_multi_for_shop(LocationName.herm_cardigan_purch))
    world.set_rule(world.get_location(LocationName.luna_yellow_dress_purch),
                   has_multi_for_shop(LocationName.luna_yellow_dress_purch))

