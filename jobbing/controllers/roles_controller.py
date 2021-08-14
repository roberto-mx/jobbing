from jobbing.DBModels import Role as DBRole
from jobbing.models.role import Role  # noqa: E501
from jobbing.login import token_required


@token_required
def get_roles():  # noqa: E501
    """Lists all user roles

    Show a listing of roles to accesing the API # noqa: E501


    :rtype: List[Role]
    """

    roles = DBRole.query.all()
    results = [
        Role(role.id, role.name, role.status) for role in roles]
    return results
