from collections import OrderedDict


SUBSPELL_POINTS = OrderedDict([('dai', 5), ('aine', 4), ('ain', 3), ('ai', 2), ('ne', 2), ('jee', 3), ('je', 2),
                               ('fe', 1)])


def _subspell_damage(spell, subspell):
    """
    Calculate damage of all appearances of given subspell in spell, return spell with 
    removed subspells and damage points done by subspells

    :param str spell: string with spell
    :param str subspell: string with subspell

    :rtype: str, int
    :return: spell with removed subspells, damage points done by subspells
    """
    subspell_damage_points = 0
    while spell.find(subspell) != -1:
        subspell_damage_points += SUBSPELL_POINTS[subspell]
        spell = spell.replace(subspell, '')

    return spell, subspell_damage_points


def damage(spell):
    """
    Function calculating damage

    :param str spell: string with spell

    :rtype: int
    :return: points of damage
    """

    try:
        spell_start = spell.index('fe')
        spell_end = spell.rindex('ai')
    except ValueError:
        return 0

    spell = spell[spell_start + 2:spell_end]  # spell without 'fe' and last 'ai'
    damage_points = SUBSPELL_POINTS['fe'] + SUBSPELL_POINTS['ai']

    if spell_start >= spell_end or 'fe' in spell:
        return 0

    for subspell in SUBSPELL_POINTS.keys():
        spell, subspell_damage_points = _subspell_damage(spell, subspell)
        # use defined function to calculate damage points done by subspell
        damage_points += subspell_damage_points

    damage_points -= len(spell)  # decreasing damage for all letters which are not subspells

    return damage_points if damage_points >= 0 else 0
