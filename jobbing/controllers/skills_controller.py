from flask import abort

from jobbing.models.skill import Skill  # noqa: E501
from jobbing.DBModels import Skill as DBSkill


def get_skill_by_id(skill_id):  # noqa: E501
    """get_skill_by_id

    Show a Skills by id # noqa: E501

    :param skill_id: Id de Skill
    :type skill_id: int

    :rtype: List[Skill]
    """
    skill = DBSkill.query.filter(DBSkill.id == skill_id).first()

    if skill == None:
        abort(404)

    return Skill(provider_id=skill.provider_id,
            category_id=skill.category_id,
            years_of_experience=skill.years_of_experience,
            price_of_service=skill.price_of_service,
            services_provided=skill.services_provided,
            five_stars=skill.five_stars,
            four_starts=skill.four_starts,
            three_starts=skill.three_starts,
            two_starts=skill.two_starts,
            one_start=skill.one_start)
