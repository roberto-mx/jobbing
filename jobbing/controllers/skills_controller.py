import connexion
import six

from jobbing.models.skill import Skill  # noqa: E501
from jobbing import util


def get_skill_by_id(skill_id):  # noqa: E501
    """get_skill_by_id

    Show a Skills by id # noqa: E501

    :param skill_id: Id de Skill
    :type skill_id: int

    :rtype: List[Skill]
    """
    return 'do some magic!'
