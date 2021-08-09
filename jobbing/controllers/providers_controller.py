from flask import abort
from flask_login import login_required
import connexion
import six

from jobbing.models.user_profile import UserProfile  # noqa: E501
from jobbing.DBModels import Profile as DBProfile


@login_required
def get_provider_by_id(provider_id):  # noqa: E501
    """get_provider_by_id

    Shows a provider identified by id # noqa: E501

    :param provider_id: id del proveedor de servicios
    :type provider_id: int

    :rtype: UserProfile
    """
    profile = DBProfile.query.filter(DBProfile.provider_id == provider_id).first()

    if profile == None:
        abort(404)

    return UserProfile(userprofile_id=profile.userprofile_id,
                first_name=profile.first_name,
                second_name=profile.second_name,
                first_surname=profile.first_surname,
                second_surname=profile.second_surname,
                birthdate=profile.birthdate,
                curp=profile.curp,
                mobile_number=profile.mobile_number,
                home_number=profile.home_number,
                office_number=profile.office_number,
                facebook_profile=profile.facebook_profile,
                linkedin_profile=profile.linkedin_profile,
                twitter_profile=profile.twitter_profile,
                id_image=profile.id_image,
                status=profile.status,
                created=profile.created,
                updated=profile.updated,
                credentials_id=profile.credentials_id,
                org_id=profile.org_id,
                address=profile.address)


@login_required
def get_skills_by_provider_id(provider_id):  # noqa: E501
    """get_skills_by_provider_id

    Show all Service Providers according to their skills # noqa: E501

    :param provider_id: Id de Provider
    :type provider_id: int

    :rtype: List[UserProfile]
    """
    providers = DBProfile.query.filter(DBProfile.provider_id == provider_id)
    results = [
        UserProfile(userprofile_id=p.userprofile_id,
                first_name=p.first_name,
                second_name=p.second_name,
                first_surname=p.first_surname,
                second_surname=p.second_surname,
                birthdate=p.birthdate,
                curp=p.curp,
                mobile_number=p.mobile_number,
                home_number=p.home_number,
                office_number=p.office_number,
                facebook_profile=p.facebook_profile,
                linkedin_profile=p.linkedin_profile,
                twitter_profile=p.twitter_profile,
                id_image=p.id_image,
                status=p.status,
                created=p.created,
                updated=p.updated,
                credentials_id=p.credentials_id,
                org_id=p.org_id,
                address=p.address) for p in providers]
    return results
