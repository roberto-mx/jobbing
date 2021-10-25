from flask import abort

from jobbing.models.user_profile import UserProfile  # noqa: E501
from jobbing.models.service import Service  # noqa: E501
from jobbing.DBModels import Profile as DBProfile
from jobbing.DBModels import Service as DBService
from jobbing.login import token_required


@token_required
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


@token_required
def get_services_by_provider_id(provider_id):  # noqa: E501
    """get_services_by_provider_id

    Show all Services that offers a provider # noqa: E501

    :param provider_id: Id de Provider
    :type provider_id: int

    :rtype: List[Service]
    """
    services = DBService.query.filter(DBService.user_id == provider_id)
    results = [
        Service(
            id = serv.service_id,
            category_id = serv.category_id,
            description = serv.description,
            years_of_experience = serv.years_of_experience,
            price_of_service = serv.price_of_service,
            work_zone = serv.work_zone,
            services_provided = serv.services_provided,
            five_stars = serv.five_stars,
            four_starts = serv.four_starts,
            three_starts = serv.three_starts,
            two_starts = serv.two_starts,
            one_start = serv.one_start,
            read_only = serv.read_only,
            status_id = serv.status_id,
            user_id = serv.user_id
        ) for serv in services]
    return results
