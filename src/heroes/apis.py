import services


def get_hero(hero_id: int) -> dict:
    return {
        'id': hero_id,
        'name': 'Hero {}'.format(hero_id)
    }
