from typing import TYPE_CHECKING, Any
from typing_extensions import override
import dataclasses

from Options import Option
from rule_builder.options import OptionFilter, Operator
from rule_builder.rules import Rule, Has, HasAll, True_, And, Or, CanReachLocation

if TYPE_CHECKING:
    from . import LHP2World

from .Names import LocationName, ItemName, RegionName
from .Options import LHP2Options, EndGoal, HardPurchases
from .Locations import all_location_table

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

# Dark Times Logic
can_get_dt_gc = Has(ItemName.expecto_unlock)
can_get_dt_sc = Has(ItemName.diffindo_unlock)
can_get_dt_rc = Has(ItemName.expecto_unlock)
can_get_dt_hc = Has(ItemName.www_box_unlock)
can_get_dt_sip = can_use_dark_magic
can_get_arthur_suit = HasAll(ItemName.reducto_unlock, ItemName.expecto_unlock) & can_use_dark_magic
can_get_elphias = HasAll(ItemName.agua_unlock, ItemName.expecto_unlock)

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

# Back To School Logic
can_access_bts = HasAll(ItemName.herm_bag_unlock, ItemName.bts_unlock)
can_access_bts_free = HasAll(ItemName.agua_unlock, ItemName.delum_unlock,
                             ItemName.www_box_unlock, ItemName.diffindo_unlock)
can_get_bts_sc = Has(ItemName.reducto_unlock)
can_get_bts_hc = HasAll(ItemName.agua_unlock, ItemName.delum_unlock) & can_use_key
can_get_bts_sip = HasAll(ItemName.agua_unlock, ItemName.delum_unlock)
can_get_aberforth = HasAll(ItemName.agua_unlock, ItemName.delum_unlock) & char_is_strong
can_get_alecto = can_use_dark_magic
can_get_amycus = can_use_dark_magic

# Burning Bridges Logic
can_access_bb = HasAll(ItemName.bb_unlock, ItemName.agua_unlock)
can_access_bb_free = HasAll(ItemName.specs_unlock, ItemName.reducto_unlock)
can_beat_bb = HasAll(ItemName.diffindo_unlock, ItemName.herm_bag_unlock, ItemName.www_box_unlock, ItemName.delum_unlock)
can_get_bb_gc = can_beat_bb & can_use_dark_magic & can_use_key
can_get_bb_sc = can_use_dark_magic
can_get_bb_rc = Has(ItemName.diffindo_unlock)
can_get_bb_hc = Has(ItemName.delum_unlock)
can_get_bb_sip = can_use_dark_magic
can_get_neville_cardigan = HasAll(ItemName.diffindo_unlock, ItemName.herm_bag_unlock) & can_use_dark_magic
can_get_seamus = HasAll(ItemName.delum_unlock, ItemName.www_box_unlock)

# Fiendfyre Frenzy Logic
can_access_fiend = HasAll(ItemName.www_box_unlock, ItemName.reducto_unlock,
                          ItemName.herm_bag_unlock, ItemName.ff_unlock)
can_access_fiend_free = HasAll(ItemName.specs_unlock, ItemName.delum_unlock)
can_beat_fiend = HasAll(ItemName.agua_unlock, ItemName.diffindo_unlock)
can_get_fiend_gc = char_is_strong
can_get_fiend_sc = can_use_dark_magic
can_get_fiend_rc = Has(ItemName.agua_unlock) & can_use_dark_magic
can_get_fiend_hc = char_is_strong
can_get_fiend_sip = Has(ItemName.specs_unlock)
can_get_goyle = Has(ItemName.agua_unlock) & can_use_key
can_get_harry_brown_jacket = HasAll(ItemName.agua_unlock, ItemName.diffindo_unlock) & can_use_spanner
can_get_tom_riddle = HasAll(ItemName.agua_unlock, ItemName.diffindo_unlock)

# Snape's Tears Logic
can_access_st = HasAll(ItemName.agua_unlock, ItemName.www_box_unlock, ItemName.st_unlock)
can_access_st_free = HasAll(ItemName.reducto_unlock, ItemName.herm_bag_unlock)
can_beat_st = HasAll(ItemName.diffindo_unlock, ItemName.delum_unlock, ItemName.focus_unlock)
can_get_st_gc = can_use_dark_magic
can_get_st_sc = can_use_dark_magic
can_get_st_rc = Has(ItemName.diffindo_unlock) & can_use_spanner
can_get_st_hc = Has(ItemName.diffindo_unlock) & char_is_strong
can_get_death_eater = can_use_key
can_get_fenrir = can_use_dark_magic
can_get_prof_snape = Has(ItemName.diffindo_unlock) & can_use_dark_magic

# The Flaw in the Plan Logic
can_access_tfitp_free = HasAll(ItemName.reducto_unlock, ItemName.agua_unlock,
                               ItemName.diffindo_unlock, ItemName.www_box_unlock)
can_beat_tfitp = Has(ItemName.expecto_unlock)
can_get_tfitp_sc = can_use_dark_magic
can_get_tfitp_rc = Has(ItemName.specs_unlock) & char_is_strong
can_get_tfitp_sip = can_use_key
has_all_horcruxes = HasAll(ItemName.tr_diary, ItemName.gaunt_ring, ItemName.locket, ItemName.cup,
                           ItemName.diadem, ItemName.nagini)
defeat_voldemort = Has("Voldemort Defeated")

# Hub Logic
can_access_knockturn = HasAll(ItemName.diffindo_unlock, ItemName.dada_lesson_e_item)
can_access_tent = HasAll(ItemName.herm_bag_unlock, ItemName.apparition_unlock, ItemName.cafe_lesson_e_item)
can_access_train_grounds = HasAll(ItemName.agua_unlock, ItemName.dada_lesson_e_item)
can_access_library = HasAll(ItemName.agua_unlock, ItemName.y6_hogwarts_e_item)
can_access_lake = HasAll(ItemName.herm_bag_unlock, ItemName.cafe_lesson_e_item)
can_access_quid = HasAll(ItemName.delum_unlock, ItemName.cafe_lesson_e_item)
can_access_potions = Has(ItemName.y6_hogwarts_e_item)
can_access_div_court = HasAll(ItemName.diffindo_unlock, ItemName.dada_lesson_e_item)
can_access_astron = HasAll(ItemName.herm_bag_unlock, ItemName.y6_hogwarts_e_item)
can_access_great_hall = Has(ItemName.thestral_lesson_e_item)
can_access_weasley_courtyard = Has(ItemName.focus_lesson_e_item)
can_access_mid_grand_stair = HasAll(ItemName.draught_lesson_e_item, ItemName.diffindo_unlock)
can_access_dumb_office = HasAll(ItemName.draught_lesson_e_item, ItemName.www_box_unlock)
can_access_upper_grand_stair = HasAll(ItemName.draught_lesson_e_item, ItemName.agua_unlock)
can_access_slytherin_common = (HasAll(ItemName.delum_unlock, ItemName.herm_bag_unlock, ItemName.y5_hogwarts_e_item)
                               & can_use_dark_magic)
can_access_hufflepuff_common = (HasAll(ItemName.delum_unlock, ItemName.y5_hogwarts_e_item) & can_use_dark_magic)
can_access_ravenclaw_tower = HasAll(ItemName.y6_hogwarts_e_item, ItemName.agua_unlock)
can_access_hogsmeade = Has(ItemName.y6_story_complete_e_item)

# Shop Logic
has_high_multi = (Has(ItemName.score_x6_unlock) | Has(ItemName.score_x8_unlock) | Has(ItemName.score_x10_unlock) |
                  HasAll(ItemName.score_x2_unlock, ItemName.score_x4_unlock))
has_low_multi = Has(ItemName.score_x2_unlock) | Has(ItemName.score_x4_unlock) | has_high_multi


def from_option(option: type[Option], value: Any, operator: Operator = "eq") -> Rule:
    return True_(options=[OptionFilter(option, value, operator)])


def can_purchase_red_brick(location_name: str) -> Rule:
    red_brick = location_name.replace("sed", "sable")
    return And(Has(red_brick), has_needed_multi(location_name))


def can_purchase_char(location_name: str) -> Rule:
    token = location_name.replace(" Purchased", " Token")
    return And(Has(token), has_needed_multi(location_name))


def has_needed_multi(location_name: str) -> Rule:
    return Or(from_option(HardPurchases, 1), HasMultiplier(location_name))


@dataclasses.dataclass
class HasMultiplier(Rule, game="Lego Harry Potter 5-7"):
    location_name: str

    @override
    def _instantiate(self, world: "LHP2World") -> Rule.Resolved:
        # Look up the price
        data = all_location_table[self.location_name]
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
    set_lesson_logic(world)
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
    # Y8
    set_ttd_logic(world)
    set_bts_logic(world)
    set_bb_logic(world)
    set_fiend_logic(world)
    set_st_logic(world)
    set_tfitp_logic(world)
    # Shop Logic
    set_char_purch_logic(world)
    set_joke_purch_logic(world)
    set_gold_brick_purch_logic(world)
    set_red_brick_purch_logic(world)


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
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.bts), can_access_bts)
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.bb), can_access_bb)
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.fiend), can_access_fiend)
    world.set_rule(world.get_entrance(RegionName.leaky + " -> " + RegionName.st), can_access_st)
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
    world.set_rule(world.get_entrance(RegionName.bts + " -> " + RegionName.btsf), can_access_bts_free)
    world.set_rule(world.get_entrance(RegionName.bb + " -> " + RegionName.bbf), can_access_bb_free)
    world.set_rule(world.get_entrance(RegionName.fiend + " -> " + RegionName.fiendf), can_access_fiend_free)
    world.set_rule(world.get_entrance(RegionName.st + " -> " + RegionName.stf), can_access_st_free)
    world.set_rule(world.get_entrance(RegionName.tfitp + " -> " + RegionName.tfitpf), can_access_tfitp_free)
    # Hub Entrance Rules
    world.set_rule(world.get_entrance(RegionName.diag + " -> " + RegionName.knock), can_access_knockturn)
    world.set_rule(world.get_entrance(RegionName.lond + " -> " + RegionName.tent), can_access_tent)
    world.set_rule(world.get_entrance(RegionName.court + " -> " + RegionName.tg), can_access_train_grounds)
    world.set_rule(world.get_entrance(RegionName.foyer + " -> " + RegionName.lib), can_access_library)
    world.set_rule(world.get_entrance(RegionName.ground + " -> " + RegionName.lake), can_access_lake)
    world.set_rule(world.get_entrance(RegionName.ground + " -> " + RegionName.qp), can_access_quid)
    world.set_rule(world.get_entrance(RegionName.cl + " -> " + RegionName.pot), can_access_potions)
    world.set_rule(world.get_entrance(RegionName.cl + " -> " + RegionName.divc), can_access_div_court)
    world.set_rule(world.get_entrance(RegionName.divc + " -> " + RegionName.ast), can_access_astron)
    world.set_rule(world.get_entrance(RegionName.foyer + " -> " + RegionName.ghl), can_access_great_hall)
    world.set_rule(world.get_entrance(RegionName.ghl + " -> " + RegionName.wc), can_access_weasley_courtyard)
    world.set_rule(world.get_entrance(RegionName.low_stair + " -> " + RegionName.mid_stair), can_access_mid_grand_stair)
    world.set_rule(world.get_entrance(RegionName.mid_stair + " -> " + RegionName.dumble_office), can_access_dumb_office)
    world.set_rule(world.get_entrance(RegionName.dumble_office + " -> " + RegionName.upper_stair),
                   can_access_upper_grand_stair)
    world.set_rule(world.get_entrance(RegionName.upper_stair + " -> " + RegionName.dumble_office),
                   can_access_upper_grand_stair)
    world.set_rule(world.get_entrance(RegionName.house + " -> " + RegionName.slyth), can_access_slytherin_common)
    world.set_rule(world.get_entrance(RegionName.house + " -> " + RegionName.huff), can_access_hufflepuff_common)
    world.set_rule(world.get_entrance(RegionName.house + " -> " + RegionName.raven), can_access_ravenclaw_tower)
    world.set_rule(world.get_entrance(RegionName.hogwpath + " -> " + RegionName.hogspath), can_access_hogsmeade)


def set_lesson_logic(world):
    world.set_rule(world.get_location(LocationName.dada_lesson), Has(ItemName.y5_hogwarts_e_item))
    world.set_rule(world.get_location(LocationName.thestral_lesson), Has(ItemName.dada_lesson_e_item))
    world.set_rule(world.get_location(LocationName.dueling_lesson), Has(ItemName.thestral_lesson_e_item))
    world.set_rule(world.get_location(LocationName.diffindo_lesson), HasAll(ItemName.diffindo_unlock,
                                                                            ItemName.dueling_lesson_e_item))
    world.set_rule(world.get_location(LocationName.patroneous_lesson), HasAll(ItemName.expecto_unlock,
                                                                              ItemName.diffindo_lesson_e_item))
    world.set_rule(world.get_location(LocationName.grawp_lesson), Has(ItemName.patroneous_lesson_e_item))
    world.set_rule(world.get_location(LocationName.focus_lesson), Has(ItemName.grawp_lesson_e_item))
    world.set_rule(world.get_location(LocationName.owls_lesson), HasAll(ItemName.focus_lesson_e_item,
                                                                        ItemName.www_box_unlock))
    world.set_rule(world.get_location(LocationName.y5_story_complete), Has(ItemName.owls_lesson_e_item))
    world.set_rule(world.get_location(LocationName.specs_lesson), HasAll(ItemName.y5_story_complete_e_item,
                                                                         ItemName.specs_unlock))
    world.set_rule(world.get_location(LocationName.y6_hogwarts), Has(ItemName.specs_lesson_e_item))
    world.set_rule(world.get_location(LocationName.draught_lesson), Has(ItemName.y6_hogwarts_e_item))
    world.set_rule(world.get_location(LocationName.vial_lesson), Has(ItemName.draught_lesson_e_item))
    world.set_rule(world.get_location(LocationName.agua_lesson), HasAll(ItemName.vial_lesson_e_item,
                                                                        ItemName.agua_unlock))
    world.set_rule(world.get_location(LocationName.reducto_lesson), HasAll(ItemName.agua_lesson_e_item,
                                                                           ItemName.reducto_unlock))
    world.set_rule(world.get_location(LocationName.dumble_lesson), HasAll(ItemName.reducto_lesson_e_item,
                                                                          ItemName.reducto_unlock))
    world.set_rule(world.get_location(LocationName.y6_story_complete), Has(ItemName.dumble_lesson_e_item))
    world.set_rule(world.get_location(LocationName.cafe_lesson), Has(ItemName.y6_story_complete_e_item))


def set_event_logic(world):
    world.set_rule(world.get_location(LocationName.y5_hogwarts_event), CanReachLocation(LocationName.y5_hogwarts))
    world.set_rule(world.get_location(LocationName.dada_lesson_event), CanReachLocation(LocationName.dada_lesson))
    world.set_rule(world.get_location(LocationName.thestral_lesson_event),
                   CanReachLocation(LocationName.thestral_lesson))
    world.set_rule(world.get_location(LocationName.dueling_lesson_event), CanReachLocation(LocationName.dueling_lesson))
    world.set_rule(world.get_location(LocationName.diffindo_lesson_event),
                   CanReachLocation(LocationName.diffindo_lesson))
    world.set_rule(world.get_location(LocationName.patroneous_lesson_event),
                   CanReachLocation(LocationName.patroneous_lesson))
    world.set_rule(world.get_location(LocationName.grawp_lesson_event), CanReachLocation(LocationName.grawp_lesson))
    world.set_rule(world.get_location(LocationName.focus_lesson_event), CanReachLocation(LocationName.focus_lesson))
    world.set_rule(world.get_location(LocationName.owls_lesson_event), CanReachLocation(LocationName.owls_lesson))
    world.set_rule(world.get_location(LocationName.y5_story_complete_event),
                   CanReachLocation(LocationName.y5_story_complete))
    world.set_rule(world.get_location(LocationName.specs_lesson_event), CanReachLocation(LocationName.specs_lesson))
    world.set_rule(world.get_location(LocationName.y6_hogwarts_event), CanReachLocation(LocationName.y6_hogwarts))
    world.set_rule(world.get_location(LocationName.draught_lesson_event), CanReachLocation(LocationName.draught_lesson))
    world.set_rule(world.get_location(LocationName.vial_lesson_event), CanReachLocation(LocationName.vial_lesson))
    world.set_rule(world.get_location(LocationName.agua_lesson_event), CanReachLocation(LocationName.agua_lesson))
    world.set_rule(world.get_location(LocationName.reducto_lesson_event), CanReachLocation(LocationName.reducto_lesson))
    world.set_rule(world.get_location(LocationName.dumble_lesson_event), CanReachLocation(LocationName.dumble_lesson))
    world.set_rule(world.get_location(LocationName.y6_story_complete_event),
                   CanReachLocation(LocationName.y6_story_complete))
    world.set_rule(world.get_location(LocationName.cafe_lesson_event), CanReachLocation(LocationName.cafe_lesson))
    world.set_rule(world.get_location("Defeat Voldemort"), has_all_horcruxes & can_beat_tfitp)


def set_win_con(world):
    if world.options.EndGoal == EndGoal.option_defeat_voldemort:
        world.set_completion_rule(defeat_voldemort)
    # if options.EndGoal == EndGoal.option_the_collector:
    #     world.completion_condition[player] =


def set_dt_logic(world):
    world.set_rule(world.get_location(LocationName.dt_gc), can_get_dt_gc)
    world.set_rule(world.get_location(LocationName.dt_sc), can_get_dt_sc)
    world.set_rule(world.get_location(LocationName.dt_rc), can_get_dt_rc)
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


def set_bts_logic(world):
    world.set_rule(world.get_location(LocationName.bts_sc), can_get_bts_sc)
    world.set_rule(world.get_location(LocationName.bts_hc), can_get_bts_hc)
    world.set_rule(world.get_location(LocationName.bts_sip), can_get_bts_sip)
    world.set_rule(world.get_location(LocationName.aberforth_token), can_get_aberforth)
    world.set_rule(world.get_location(LocationName.alecto_token), can_get_alecto)
    world.set_rule(world.get_location(LocationName.amycus_token), can_get_amycus)


def set_bb_logic(world):
    world.set_rule(world.get_location(LocationName.bb_beat), can_beat_bb)
    world.set_rule(world.get_location(LocationName.bb_tw), can_beat_bb)
    world.set_rule(world.get_location(LocationName.bb_gc), can_get_bb_gc)
    world.set_rule(world.get_location(LocationName.bb_sc), can_get_bb_sc)
    world.set_rule(world.get_location(LocationName.bb_rc), can_get_bb_rc)
    world.set_rule(world.get_location(LocationName.bb_hc), can_get_bb_hc)
    world.set_rule(world.get_location(LocationName.bb_sip), can_get_bb_sip)
    world.set_rule(world.get_location(LocationName.neville_cardigan_token), can_get_neville_cardigan)
    world.set_rule(world.get_location(LocationName.seamus_token), can_get_seamus)


def set_fiend_logic(world):
    world.set_rule(world.get_location(LocationName.fiend_beat), can_beat_fiend)
    world.set_rule(world.get_location(LocationName.fiend_tw), can_beat_fiend)
    world.set_rule(world.get_location(LocationName.fiend_gc), can_get_fiend_gc)
    world.set_rule(world.get_location(LocationName.fiend_sc), can_get_fiend_sc)
    world.set_rule(world.get_location(LocationName.fiend_rc), can_get_fiend_rc)
    world.set_rule(world.get_location(LocationName.fiend_hc), can_get_fiend_hc)
    world.set_rule(world.get_location(LocationName.fiend_sip), can_get_fiend_sip)
    world.set_rule(world.get_location(LocationName.goyle_token), can_get_goyle)
    world.set_rule(world.get_location(LocationName.harry_brown_jacket_token), can_get_harry_brown_jacket)
    world.set_rule(world.get_location(LocationName.tom_riddle_token), can_get_tom_riddle)


def set_st_logic(world):
    world.set_rule(world.get_location(LocationName.st_beat), can_beat_st)
    world.set_rule(world.get_location(LocationName.st_tw), can_beat_st)
    world.set_rule(world.get_location(LocationName.st_gc), can_get_st_gc)
    world.set_rule(world.get_location(LocationName.st_sc), can_get_st_sc)
    world.set_rule(world.get_location(LocationName.st_rc), can_get_st_rc)
    world.set_rule(world.get_location(LocationName.st_hc), can_get_st_hc)
    world.set_rule(world.get_location(LocationName.death_eater_token), can_get_death_eater)
    world.set_rule(world.get_location(LocationName.fenrir_token), can_get_fenrir)
    world.set_rule(world.get_location(LocationName.prof_snape_token), can_get_prof_snape)


def set_tfitp_logic(world):
    world.set_rule(world.get_location(LocationName.tfitp_beat), can_beat_tfitp)
    world.set_rule(world.get_location(LocationName.tfitp_tw), can_beat_tfitp)
    world.set_rule(world.get_location(LocationName.tfitp_sc), can_get_tfitp_sc)
    world.set_rule(world.get_location(LocationName.tfitp_rc), can_get_tfitp_rc)
    world.set_rule(world.get_location(LocationName.tfitp_sip), can_get_tfitp_sip)


def set_char_purch_logic(world):
    world.set_rule(world.get_location(LocationName.hagrid_purch), can_purchase_char(LocationName.hagrid_purch))
    world.set_rule(world.get_location(LocationName.fang_purch), can_purchase_char(LocationName.fang_purch))
    world.set_rule(world.get_location(LocationName.hagrid_wed_purch), can_purchase_char(LocationName.hagrid_wed_purch))
    world.set_rule(world.get_location(LocationName.prof_flit_purch), can_purchase_char(LocationName.prof_flit_purch))
    world.set_rule(world.get_location(LocationName.madam_malk_purch), can_purchase_char(LocationName.madam_malk_purch))
    world.set_rule(world.get_location(LocationName.dobby_purch), can_purchase_char(LocationName.dobby_purch))
    world.set_rule(world.get_location(LocationName.kreacher_purch), can_purchase_char(LocationName.kreacher_purch))
    world.set_rule(world.get_location(LocationName.tr_orphanage_purch),
                   can_purchase_char(LocationName.tr_orphanage_purch))
    world.set_rule(world.get_location(LocationName.bogrod_purch), can_purchase_char(LocationName.bogrod_purch))
    world.set_rule(world.get_location(LocationName.mund_fletch_purch),
                   can_purchase_char(LocationName.mund_fletch_purch))
    world.set_rule(world.get_location(LocationName.griphook_purch), can_purchase_char(LocationName.griphook_purch))
    world.set_rule(world.get_location(LocationName.prof_mcgon_purch), can_purchase_char(LocationName.prof_mcgon_purch))
    world.set_rule(world.get_location(LocationName.madam_pince_purch),
                   can_purchase_char(LocationName.madam_pince_purch))
    world.set_rule(world.get_location(LocationName.prof_sprout_purch),
                   can_purchase_char(LocationName.prof_sprout_purch))
    world.set_rule(world.get_location(LocationName.madam_pomfrey_purch),
                   can_purchase_char(LocationName.madam_pomfrey_purch))
    world.set_rule(world.get_location(LocationName.prof_trelawney_purch),
                   can_purchase_char(LocationName.prof_trelawney_purch))
    world.set_rule(world.get_location(LocationName.madam_rosmerta_purch),
                   can_purchase_char(LocationName.madam_rosmerta_purch))
    world.set_rule(world.get_location(LocationName.fat_friar_purch), can_purchase_char(LocationName.fat_friar_purch))
    world.set_rule(world.get_location(LocationName.grey_lady_purch), can_purchase_char(LocationName.grey_lady_purch))
    world.set_rule(world.get_location(LocationName.fat_lady_purch), can_purchase_char(LocationName.fat_lady_purch))
    world.set_rule(world.get_location(LocationName.herm_ball_purch), can_purchase_char(LocationName.herm_ball_purch))
    world.set_rule(world.get_location(LocationName.bellatrix_purch), can_purchase_char(LocationName.bellatrix_purch))
    world.set_rule(world.get_location(LocationName.emmeline_purch), can_purchase_char(LocationName.emmeline_purch))
    world.set_rule(world.get_location(LocationName.narcissa_purch), can_purchase_char(LocationName.narcissa_purch))
    world.set_rule(world.get_location(LocationName.mcgon_pyjamas_purch),
                   can_purchase_char(LocationName.mcgon_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.mary_cattermole_purch),
                   can_purchase_char(LocationName.mary_cattermole_purch))
    world.set_rule(world.get_location(LocationName.mcgon_black_purch),
                   can_purchase_char(LocationName.mcgon_black_purch))
    world.set_rule(world.get_location(LocationName.herm_gringotts_purch),
                   can_purchase_char(LocationName.herm_gringotts_purch))
    world.set_rule(world.get_location(LocationName.prof_grubbly_purch),
                   can_purchase_char(LocationName.prof_grubbly_purch))
    world.set_rule(world.get_location(LocationName.bellatrix_azka_purch),
                   can_purchase_char(LocationName.bellatrix_azka_purch))
    world.set_rule(world.get_location(LocationName.death_eater_purch),
                   can_purchase_char(LocationName.death_eater_purch))
    world.set_rule(world.get_location(LocationName.dudley_grey_purch),
                   can_purchase_char(LocationName.dudley_grey_purch))
    world.set_rule(world.get_location(LocationName.prof_dumble_purch),
                   can_purchase_char(LocationName.prof_dumble_purch))
    world.set_rule(world.get_location(LocationName.argus_purch), can_purchase_char(LocationName.argus_purch))
    world.set_rule(world.get_location(LocationName.madam_hooch_purch),
                   can_purchase_char(LocationName.madam_hooch_purch))
    world.set_rule(world.get_location(LocationName.crabbe_purch), can_purchase_char(LocationName.crabbe_purch))
    world.set_rule(world.get_location(LocationName.goyle_purch), can_purchase_char(LocationName.goyle_purch))
    world.set_rule(world.get_location(LocationName.ginny_purch), can_purchase_char(LocationName.ginny_purch))
    world.set_rule(world.get_location(LocationName.arthur_purch), can_purchase_char(LocationName.arthur_purch))
    world.set_rule(world.get_location(LocationName.katie_purch), can_purchase_char(LocationName.katie_purch))
    world.set_rule(world.get_location(LocationName.lily_purch), can_purchase_char(LocationName.lily_purch))
    world.set_rule(world.get_location(LocationName.bloody_baron_purch),
                   can_purchase_char(LocationName.bloody_baron_purch))
    world.set_rule(world.get_location(LocationName.fudge_purch), can_purchase_char(LocationName.fudge_purch))
    world.set_rule(world.get_location(LocationName.justin_purch), can_purchase_char(LocationName.justin_purch))
    world.set_rule(world.get_location(LocationName.cho_purch), can_purchase_char(LocationName.cho_purch))
    world.set_rule(world.get_location(LocationName.dean_purch), can_purchase_char(LocationName.dean_purch))
    world.set_rule(world.get_location(LocationName.draco_purch), can_purchase_char(LocationName.draco_purch))
    world.set_rule(world.get_location(LocationName.lucius_purch), can_purchase_char(LocationName.lucius_purch))
    world.set_rule(world.get_location(LocationName.draco_suit_purch), can_purchase_char(LocationName.draco_suit_purch))
    world.set_rule(world.get_location(LocationName.harry_pyjamas_purch),
                   can_purchase_char(LocationName.harry_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.myrtle_purch), can_purchase_char(LocationName.myrtle_purch))
    world.set_rule(world.get_location(LocationName.james_ghost_purch),
                   can_purchase_char(LocationName.james_ghost_purch))
    world.set_rule(world.get_location(LocationName.madeye_purch), can_purchase_char(LocationName.madeye_purch))
    world.set_rule(world.get_location(LocationName.hannah_purch), can_purchase_char(LocationName.hannah_purch))
    world.set_rule(world.get_location(LocationName.kingsley_purch), can_purchase_char(LocationName.kingsley_purch))
    world.set_rule(world.get_location(LocationName.aberforth_purch), can_purchase_char(LocationName.aberforth_purch))
    world.set_rule(world.get_location(LocationName.runcorn_purch), can_purchase_char(LocationName.runcorn_purch))
    world.set_rule(world.get_location(LocationName.alecto_purch), can_purchase_char(LocationName.alecto_purch))
    world.set_rule(world.get_location(LocationName.amycus_purch), can_purchase_char(LocationName.amycus_purch))
    world.set_rule(world.get_location(LocationName.anthony_purch), can_purchase_char(LocationName.anthony_purch))
    world.set_rule(world.get_location(LocationName.bathilda_snake_purch),
                   can_purchase_char(LocationName.bathilda_snake_purch))
    world.set_rule(world.get_location(LocationName.blaise_purch), can_purchase_char(LocationName.blaise_purch))
    world.set_rule(world.get_location(LocationName.charity_purch), can_purchase_char(LocationName.charity_purch))
    world.set_rule(world.get_location(LocationName.charlie_purch), can_purchase_char(LocationName.charlie_purch))
    world.set_rule(world.get_location(LocationName.cormac_purch), can_purchase_char(LocationName.cormac_purch))
    world.set_rule(world.get_location(LocationName.dedalus_purch), can_purchase_char(LocationName.dedalus_purch))
    world.set_rule(world.get_location(LocationName.dirk_purch), can_purchase_char(LocationName.dirk_purch))
    world.set_rule(world.get_location(LocationName.dolohov_purch), can_purchase_char(LocationName.dolohov_purch))
    world.set_rule(world.get_location(LocationName.dragomir_purch), can_purchase_char(LocationName.dragomir_purch))
    world.set_rule(world.get_location(LocationName.elphias_purch), can_purchase_char(LocationName.elphias_purch))
    world.set_rule(world.get_location(LocationName.fenrir_purch), can_purchase_char(LocationName.fenrir_purch))
    world.set_rule(world.get_location(LocationName.grindel_young_purch),
                   can_purchase_char(LocationName.grindel_young_purch))
    world.set_rule(world.get_location(LocationName.grindel_old_purch),
                   can_purchase_char(LocationName.grindel_old_purch))
    world.set_rule(world.get_location(LocationName.gregorovitch_purch),
                   can_purchase_char(LocationName.gregorovitch_purch))
    world.set_rule(world.get_location(LocationName.hestia_purch), can_purchase_char(LocationName.hestia_purch))
    world.set_rule(world.get_location(LocationName.prof_slughorn_purch),
                   can_purchase_char(LocationName.prof_slughorn_purch))
    world.set_rule(world.get_location(LocationName.james_young_purch),
                   can_purchase_char(LocationName.james_young_purch))
    world.set_rule(world.get_location(LocationName.lavender_purch), can_purchase_char(LocationName.lavender_purch))
    world.set_rule(world.get_location(LocationName.mafalda_purch), can_purchase_char(LocationName.mafalda_purch))
    world.set_rule(world.get_location(LocationName.belby_purch), can_purchase_char(LocationName.belby_purch))
    world.set_rule(world.get_location(LocationName.luna_purple_coat_purch),
                   can_purchase_char(LocationName.luna_purple_coat_purch))
    world.set_rule(world.get_location(LocationName.herm_grey_coat_purch),
                   can_purchase_char(LocationName.herm_grey_coat_purch))
    world.set_rule(world.get_location(LocationName.harry_godric_purch),
                   can_purchase_char(LocationName.harry_godric_purch))
    world.set_rule(world.get_location(LocationName.prof_umbridge_purch),
                   can_purchase_char(LocationName.prof_umbridge_purch))
    world.set_rule(world.get_location(LocationName.fred_purch), can_purchase_char(LocationName.fred_purch))
    world.set_rule(world.get_location(LocationName.george_purch), can_purchase_char(LocationName.george_purch))
    world.set_rule(world.get_location(LocationName.molly_apron_purch),
                   can_purchase_char(LocationName.molly_apron_purch))
    world.set_rule(world.get_location(LocationName.crabbe_jumper_purch),
                   can_purchase_char(LocationName.crabbe_jumper_purch))
    world.set_rule(world.get_location(LocationName.draco_sweater_purch),
                   can_purchase_char(LocationName.draco_sweater_purch))
    world.set_rule(world.get_location(LocationName.goyle_jumper_purch),
                   can_purchase_char(LocationName.goyle_jumper_purch))
    world.set_rule(world.get_location(LocationName.milk_man_purch), can_purchase_char(LocationName.milk_man_purch))
    world.set_rule(world.get_location(LocationName.twin_2_purch), can_purchase_char(LocationName.twin_2_purch))
    world.set_rule(world.get_location(LocationName.herm_mafalda_purch),
                   can_purchase_char(LocationName.herm_mafalda_purch))
    world.set_rule(world.get_location(LocationName.ministry_guard_purch),
                   can_purchase_char(LocationName.ministry_guard_purch))
    world.set_rule(world.get_location(LocationName.harry_winter_purch),
                   can_purchase_char(LocationName.harry_winter_purch))
    world.set_rule(world.get_location(LocationName.arthur_torn_suit_purch),
                   can_purchase_char(LocationName.arthur_torn_suit_purch))
    world.set_rule(world.get_location(LocationName.fred_winter_purch),
                   can_purchase_char(LocationName.fred_winter_purch))
    world.set_rule(world.get_location(LocationName.cho_winter_purch), can_purchase_char(LocationName.cho_winter_purch))
    world.set_rule(world.get_location(LocationName.george_winter_purch),
                   can_purchase_char(LocationName.george_winter_purch))
    world.set_rule(world.get_location(LocationName.herm_scarf_purch), can_purchase_char(LocationName.herm_scarf_purch))
    world.set_rule(world.get_location(LocationName.luna_blue_jumper_purch),
                   can_purchase_char(LocationName.luna_blue_jumper_purch))
    world.set_rule(world.get_location(LocationName.fred_owls_purch), can_purchase_char(LocationName.fred_owls_purch))
    world.set_rule(world.get_location(LocationName.fred_pyjamas_purch),
                   can_purchase_char(LocationName.fred_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.george_owls_purch),
                   can_purchase_char(LocationName.george_owls_purch))
    world.set_rule(world.get_location(LocationName.george_pyjamas_purch),
                   can_purchase_char(LocationName.george_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.herm_jumper_purch),
                   can_purchase_char(LocationName.herm_jumper_purch))
    world.set_rule(world.get_location(LocationName.fudge_wizengamot_purch),
                   can_purchase_char(LocationName.fudge_wizengamot_purch))
    world.set_rule(world.get_location(LocationName.dudley_purch), can_purchase_char(LocationName.dudley_purch))
    world.set_rule(world.get_location(LocationName.gang_mem_purch), can_purchase_char(LocationName.gang_mem_purch))
    world.set_rule(world.get_location(LocationName.harry_albert_runcorn_purch),
                   can_purchase_char(LocationName.harry_albert_runcorn_purch))
    world.set_rule(world.get_location(LocationName.harry_brown_jacket_purch),
                   can_purchase_char(LocationName.harry_brown_jacket_purch))
    world.set_rule(world.get_location(LocationName.dumble_cursed_purch),
                   can_purchase_char(LocationName.dumble_cursed_purch))
    world.set_rule(world.get_location(LocationName.lucius_death_eater_purch),
                   can_purchase_char(LocationName.lucius_death_eater_purch))
    world.set_rule(world.get_location(LocationName.luna_purch), can_purchase_char(LocationName.luna_purch))
    world.set_rule(world.get_location(LocationName.umbridge_wizengamot_purch),
                   can_purchase_char(LocationName.umbridge_wizengamot_purch))
    world.set_rule(world.get_location(LocationName.dolohov_workman_purch),
                   can_purchase_char(LocationName.dolohov_workman_purch))
    world.set_rule(world.get_location(LocationName.michael_purch), can_purchase_char(LocationName.michael_purch))
    world.set_rule(world.get_location(LocationName.dean_winter_purch),
                   can_purchase_char(LocationName.dean_winter_purch))
    world.set_rule(world.get_location(LocationName.arthur_cardigan_purch),
                   can_purchase_char(LocationName.arthur_cardigan_purch))
    world.set_rule(world.get_location(LocationName.luna_pink_dress_purch),
                   can_purchase_char(LocationName.luna_pink_dress_purch))
    world.set_rule(world.get_location(LocationName.marietta_purch), can_purchase_char(LocationName.marietta_purch))
    world.set_rule(world.get_location(LocationName.dumble_young_purch),
                   can_purchase_char(LocationName.dumble_young_purch))
    world.set_rule(world.get_location(LocationName.slughorn_young_purch),
                   can_purchase_char(LocationName.slughorn_young_purch))
    world.set_rule(world.get_location(LocationName.slughorn_pajamas_purch),
                   can_purchase_char(LocationName.slughorn_pajamas_purch))
    world.set_rule(world.get_location(LocationName.lily_young_casual_purch),
                   can_purchase_char(LocationName.lily_young_casual_purch))
    world.set_rule(world.get_location(LocationName.ginny_dress_purch),
                   can_purchase_char(LocationName.ginny_dress_purch))
    world.set_rule(world.get_location(LocationName.ginny_pyjamas_purch),
                   can_purchase_char(LocationName.ginny_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.blaise_black_shirt_purch),
                   can_purchase_char(LocationName.blaise_black_shirt_purch))
    world.set_rule(world.get_location(LocationName.cormac_suit_purch),
                   can_purchase_char(LocationName.cormac_suit_purch))
    world.set_rule(world.get_location(LocationName.muggle_orphan_purch),
                   can_purchase_char(LocationName.muggle_orphan_purch))
    world.set_rule(world.get_location(LocationName.luna_overalls_purch),
                   can_purchase_char(LocationName.luna_overalls_purch))
    world.set_rule(world.get_location(LocationName.molly_purch), can_purchase_char(LocationName.molly_purch))
    world.set_rule(world.get_location(LocationName.herm_cardigan_purch),
                   can_purchase_char(LocationName.herm_cardigan_purch))
    world.set_rule(world.get_location(LocationName.luna_yellow_dress_purch),
                   can_purchase_char(LocationName.luna_yellow_dress_purch))
    world.set_rule(world.get_location(LocationName.dudley_shirt_purch),
                   can_purchase_char(LocationName.dudley_shirt_purch))
    world.set_rule(world.get_location(LocationName.bill_wedding_purch),
                   can_purchase_char(LocationName.bill_wedding_purch))
    world.set_rule(world.get_location(LocationName.fleur_purch), can_purchase_char(LocationName.fleur_purch))
    world.set_rule(world.get_location(LocationName.herm_red_dress_purch),
                   can_purchase_char(LocationName.herm_red_dress_purch))
    world.set_rule(world.get_location(LocationName.figg_purch), can_purchase_char(LocationName.figg_purch))
    world.set_rule(world.get_location(LocationName.harry_locket_purch),
                   can_purchase_char(LocationName.harry_locket_purch))
    world.set_rule(world.get_location(LocationName.twin_1_purch), can_purchase_char(LocationName.twin_1_purch))
    world.set_rule(world.get_location(LocationName.cole_purch), can_purchase_char(LocationName.cole_purch))
    world.set_rule(world.get_location(LocationName.herm_ministry_purch),
                   can_purchase_char(LocationName.herm_ministry_purch))
    world.set_rule(world.get_location(LocationName.arthur_suit_purch),
                   can_purchase_char(LocationName.arthur_suit_purch))
    world.set_rule(world.get_location(LocationName.harry_christmas_purch),
                   can_purchase_char(LocationName.harry_christmas_purch))
    world.set_rule(world.get_location(LocationName.ernie_purch), can_purchase_char(LocationName.ernie_purch))
    world.set_rule(world.get_location(LocationName.prof_snape_purch), can_purchase_char(LocationName.prof_snape_purch))
    world.set_rule(world.get_location(LocationName.neville_purch), can_purchase_char(LocationName.neville_purch))
    world.set_rule(world.get_location(LocationName.ron_quidditch_purch),
                   can_purchase_char(LocationName.ron_quidditch_purch))
    world.set_rule(world.get_location(LocationName.vernon_purch), can_purchase_char(LocationName.vernon_purch))
    world.set_rule(world.get_location(LocationName.tom_riddle_purch), can_purchase_char(LocationName.tom_riddle_purch))
    world.set_rule(world.get_location(LocationName.sirius_black_purch),
                   can_purchase_char(LocationName.sirius_black_purch))
    world.set_rule(world.get_location(LocationName.remus_lupin_purch),
                   can_purchase_char(LocationName.remus_lupin_purch))
    world.set_rule(world.get_location(LocationName.wormtail_purch), can_purchase_char(LocationName.wormtail_purch))
    world.set_rule(world.get_location(LocationName.rita_skeeter_purch),
                   can_purchase_char(LocationName.rita_skeeter_purch))
    world.set_rule(world.get_location(LocationName.padma_patil_purch),
                   can_purchase_char(LocationName.padma_patil_purch))
    world.set_rule(world.get_location(LocationName.station_guard_purch),
                   can_purchase_char(LocationName.station_guard_purch))
    world.set_rule(world.get_location(LocationName.prof_binns_purch), can_purchase_char(LocationName.prof_binns_purch))
    world.set_rule(world.get_location(LocationName.penelope_purch), can_purchase_char(LocationName.penelope_purch))
    world.set_rule(world.get_location(LocationName.susan_purch), can_purchase_char(LocationName.susan_purch))
    world.set_rule(world.get_location(LocationName.tonks_purch), can_purchase_char(LocationName.tonks_purch))
    world.set_rule(world.get_location(LocationName.pius_purch), can_purchase_char(LocationName.pius_purch))
    world.set_rule(world.get_location(LocationName.reg_purch), can_purchase_char(LocationName.reg_purch))
    world.set_rule(world.get_location(LocationName.regulus_purch), can_purchase_char(LocationName.regulus_purch))
    world.set_rule(world.get_location(LocationName.scrimgeour_purch), can_purchase_char(LocationName.scrimgeour_purch))
    world.set_rule(world.get_location(LocationName.scabior_purch), can_purchase_char(LocationName.scabior_purch))
    world.set_rule(world.get_location(LocationName.xeno_purch), can_purchase_char(LocationName.xeno_purch))
    world.set_rule(world.get_location(LocationName.yaxley_purch), can_purchase_char(LocationName.yaxley_purch))
    world.set_rule(world.get_location(LocationName.zacharias_purch), can_purchase_char(LocationName.zacharias_purch))
    world.set_rule(world.get_location(LocationName.waitress_treats_purch),
                   can_purchase_char(LocationName.waitress_treats_purch))
    world.set_rule(world.get_location(LocationName.lord_voldemort_purch),
                   can_purchase_char(LocationName.lord_voldemort_purch))
    world.set_rule(world.get_location(LocationName.ron_blue_pyjamas_purch),
                   can_purchase_char(LocationName.ron_blue_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.neville_cardigan_purch),
                   can_purchase_char(LocationName.neville_cardigan_purch))
    world.set_rule(world.get_location(LocationName.neville_pyjamas_purch),
                   can_purchase_char(LocationName.neville_pyjamas_purch))
    world.set_rule(world.get_location(LocationName.percy_purch), can_purchase_char(LocationName.percy_purch))
    world.set_rule(world.get_location(LocationName.sirius_azkaban_purch),
                   can_purchase_char(LocationName.sirius_azkaban_purch))
    world.set_rule(world.get_location(LocationName.black_purch), can_purchase_char(LocationName.black_purch))
    world.set_rule(world.get_location(LocationName.xeno_luna_purch), can_purchase_char(LocationName.xeno_luna_purch))
    world.set_rule(world.get_location(LocationName.ron_reg_cattermole_purch),
                   can_purchase_char(LocationName.ron_reg_cattermole_purch))
    world.set_rule(world.get_location(LocationName.tonks_pink_coat_purch),
                   can_purchase_char(LocationName.tonks_pink_coat_purch))
    world.set_rule(world.get_location(LocationName.ron_winter_clothes_purch),
                   can_purchase_char(LocationName.ron_winter_clothes_purch))
    world.set_rule(world.get_location(LocationName.snape_underwear_purch),
                   can_purchase_char(LocationName.snape_underwear_purch))
    world.set_rule(world.get_location(LocationName.rowle_purch), can_purchase_char(LocationName.rowle_purch))
    world.set_rule(world.get_location(LocationName.petunia_purch), can_purchase_char(LocationName.petunia_purch))
    world.set_rule(world.get_location(LocationName.neville_tank_top_purch),
                   can_purchase_char(LocationName.neville_tank_top_purch))
    world.set_rule(world.get_location(LocationName.neville_winter_purch),
                   can_purchase_char(LocationName.neville_winter_purch))
    world.set_rule(world.get_location(LocationName.parvati_purch), can_purchase_char(LocationName.parvati_purch))
    world.set_rule(world.get_location(LocationName.ron_red_sweater_purch),
                   can_purchase_char(LocationName.ron_red_sweater_purch))
    world.set_rule(world.get_location(LocationName.olivander_purch), can_purchase_char(LocationName.olivander_purch))
    world.set_rule(world.get_location(LocationName.seamus_winter_purch),
                   can_purchase_char(LocationName.seamus_winter_purch))
    world.set_rule(world.get_location(LocationName.ron_underwear_purch),
                   can_purchase_char(LocationName.ron_underwear_purch))
    world.set_rule(world.get_location(LocationName.ron_wedding_purch),
                   can_purchase_char(LocationName.ron_wedding_purch))
    world.set_rule(world.get_location(LocationName.waitress_luchino_purch),
                   can_purchase_char(LocationName.waitress_luchino_purch))
    world.set_rule(world.get_location(LocationName.petunia_green_coat_purch),
                   can_purchase_char(LocationName.petunia_green_coat_purch))
    world.set_rule(world.get_location(LocationName.seamus_purch), can_purchase_char(LocationName.seamus_purch))
    world.set_rule(world.get_location(LocationName.snatcher_purch), can_purchase_char(LocationName.snatcher_purch))
    world.set_rule(world.get_location(LocationName.ron_green_shirt_purch),
                   can_purchase_char(LocationName.ron_green_shirt_purch))
    world.set_rule(world.get_location(LocationName.neville_waiter_purch),
                   can_purchase_char(LocationName.neville_waiter_purch))
    world.set_rule(world.get_location(LocationName.xeno_wedding_purch),
                   can_purchase_char(LocationName.xeno_wedding_purch))
    world.set_rule(world.get_location(LocationName.skeleton_purch), can_purchase_char(LocationName.skeleton_purch))


def set_joke_purch_logic(world):
    world.set_rule(world.get_location(LocationName.slug_purch), has_needed_multi(LocationName.slug_purch))
    world.set_rule(world.get_location(LocationName.rictu_purch), has_needed_multi(LocationName.rictu_purch))
    world.set_rule(world.get_location(LocationName.entomo_purch), has_needed_multi(LocationName.entomo_purch))
    world.set_rule(world.get_location(LocationName.taranta_purch), has_needed_multi(LocationName.taranta_purch))
    world.set_rule(world.get_location(LocationName.loco_purch), has_needed_multi(LocationName.loco_purch))
    world.set_rule(world.get_location(LocationName.redact_purch), has_needed_multi(LocationName.redact_purch))
    world.set_rule(world.get_location(LocationName.colo_purch), has_needed_multi(LocationName.colo_purch))
    world.set_rule(world.get_location(LocationName.calvo_purch), has_needed_multi(LocationName.calvo_purch))
    world.set_rule(world.get_location(LocationName.anteo_purch), has_needed_multi(LocationName.anteo_purch))
    world.set_rule(world.get_location(LocationName.herbi_purch), has_needed_multi(LocationName.herbi_purch))
    world.set_rule(world.get_location(LocationName.glaci_purch), has_needed_multi(LocationName.glaci_purch))
    world.set_rule(world.get_location(LocationName.incarc_purch), has_needed_multi(LocationName.incarc_purch))
    world.set_rule(world.get_location(LocationName.expel_purch), has_needed_multi(LocationName.expel_purch))
    world.set_rule(world.get_location(LocationName.flip_purch), has_needed_multi(LocationName.flip_purch))
    world.set_rule(world.get_location(LocationName.trip_purch), has_needed_multi(LocationName.trip_purch))
    world.set_rule(world.get_location(LocationName.stup_purch), has_needed_multi(LocationName.stup_purch))
    world.set_rule(world.get_location(LocationName.transfig_purch), has_needed_multi(LocationName.transfig_purch))
    world.set_rule(world.get_location(LocationName.engorg_purch), has_needed_multi(LocationName.engorg_purch))
    world.set_rule(world.get_location(LocationName.immob_purch), has_needed_multi(LocationName.immob_purch))


def set_gold_brick_purch_logic(world):
    world.set_rule(world.get_location(LocationName.bb_gb2), has_needed_multi(LocationName.bb_gb2))
    world.set_rule(world.get_location(LocationName.bb_gb3), has_needed_multi(LocationName.bb_gb3))
    world.set_rule(world.get_location(LocationName.bb_gb4), has_needed_multi(LocationName.bb_gb4))
    world.set_rule(world.get_location(LocationName.bb_gb5), has_needed_multi(LocationName.bb_gb5))
    world.set_rule(world.get_location(LocationName.bb_gb6), has_needed_multi(LocationName.bb_gb6))
    world.set_rule(world.get_location(LocationName.bb_gb7), has_needed_multi(LocationName.bb_gb7))
    world.set_rule(world.get_location(LocationName.bb_gb8), has_needed_multi(LocationName.bb_gb8))
    world.set_rule(world.get_location(LocationName.bb_gb9), has_needed_multi(LocationName.bb_gb9))
    world.set_rule(world.get_location(LocationName.bb_gb10), has_needed_multi(LocationName.bb_gb10))
    world.set_rule(world.get_location(LocationName.bb_gb11), has_needed_multi(LocationName.bb_gb11))
    world.set_rule(world.get_location(LocationName.bb_gb12), has_needed_multi(LocationName.bb_gb12))
    world.set_rule(world.get_location(LocationName.bb_gb13), has_needed_multi(LocationName.bb_gb13))
    world.set_rule(world.get_location(LocationName.bb_gb14), has_needed_multi(LocationName.bb_gb14))
    world.set_rule(world.get_location(LocationName.bb_gb15), has_needed_multi(LocationName.bb_gb15))
    world.set_rule(world.get_location(LocationName.bb_gb16), has_needed_multi(LocationName.bb_gb16))


def set_red_brick_purch_logic(world):
    world.set_rule(world.get_location(LocationName.com_spec_purch), HasMultiplier(LocationName.com_spec_purch))
    world.set_rule(world.get_location(LocationName.adv_guide_purch),
                   HasMultiplier(LocationName.adv_guide_purch))
    world.set_rule(world.get_location(LocationName.disguise_purch), HasMultiplier(LocationName.disguise_purch))
    world.set_rule(world.get_location(LocationName.carrot_wand_purch),
                   HasMultiplier(LocationName.carrot_wand_purch))
    world.set_rule(world.get_location(LocationName.super_strength_purch),
                   can_purchase_red_brick(LocationName.super_strength_purch))
    world.set_rule(world.get_location(LocationName.char_token_detect_purch),
                   can_purchase_red_brick(LocationName.char_token_detect_purch))
    world.set_rule(world.get_location(LocationName.fall_rescue_purch),
                   can_purchase_red_brick(LocationName.fall_rescue_purch))
    world.set_rule(world.get_location(LocationName.char_studs_purch),
                   can_purchase_red_brick(LocationName.char_studs_purch))
    world.set_rule(world.get_location(LocationName.score_x2_purch), can_purchase_red_brick(LocationName.score_x2_purch))
    world.set_rule(world.get_location(LocationName.score_x4_purch), can_purchase_red_brick(LocationName.score_x4_purch))
    world.set_rule(world.get_location(LocationName.score_x6_purch), can_purchase_red_brick(LocationName.score_x6_purch))
    world.set_rule(world.get_location(LocationName.score_x8_purch), can_purchase_red_brick(LocationName.score_x8_purch))
    world.set_rule(world.get_location(LocationName.score_x10_purch),
                   can_purchase_red_brick(LocationName.score_x10_purch))
    world.set_rule(world.get_location(LocationName.stud_mag_purch), can_purchase_red_brick(LocationName.stud_mag_purch))
    world.set_rule(world.get_location(LocationName.regen_hearts_purch),
                   can_purchase_red_brick(LocationName.regen_hearts_purch))
    world.set_rule(world.get_location(LocationName.extra_hears_purch),
                   can_purchase_red_brick(LocationName.extra_hears_purch))
    world.set_rule(world.get_location(LocationName.invincibility_purch),
                   can_purchase_red_brick(LocationName.invincibility_purch))
    world.set_rule(world.get_location(LocationName.red_brick_detect_purch),
                   can_purchase_red_brick(LocationName.red_brick_detect_purch))
    world.set_rule(world.get_location(LocationName.crest_detect_purch),
                   can_purchase_red_brick(LocationName.crest_detect_purch))
    world.set_rule(world.get_location(LocationName.gb_detect_purch),
                   can_purchase_red_brick(LocationName.gb_detect_purch))
    world.set_rule(world.get_location(LocationName.christmas_purch),
                   can_purchase_red_brick(LocationName.christmas_purch))
    world.set_rule(world.get_location(LocationName.ghost_studs_purch),
                   can_purchase_red_brick(LocationName.ghost_studs_purch))
    world.set_rule(world.get_location(LocationName.fast_magic_purch),
                   can_purchase_red_brick(LocationName.fast_magic_purch))
    world.set_rule(world.get_location(LocationName.fast_dig_purch), can_purchase_red_brick(LocationName.fast_dig_purch))
