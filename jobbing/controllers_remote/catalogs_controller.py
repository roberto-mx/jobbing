"""
Catalogs are read only tables
"""

from flask import abort

# DB Models
from jobbing.DBModelsRemote import Colony as DBColony
from jobbing.DBModelsRemote import CountryCode as DBCountryCode
from jobbing.DBModelsRemote import Municipality as DBMunicipality
from jobbing.DBModelsRemote import Skills as DBSkills
from jobbing.DBModelsRemote import StateCode as DBStateCode
from jobbing.DBModelsRemote import Status as DBStatus
from jobbing.DBModelsRemote import UserRole as DBUserRole
from jobbing.DBModelsRemote import ZipCode as DBZipCode
from jobbing.DBModelsRemote import Org as DBOrg

# Swagger Models
from jobbing.models_remote.colony import Colony # noqa: E501
from jobbing.models_remote.country_code import CountryCode # noqa: E501
from jobbing.models_remote.municipality import Municipality # noqa: E501
from jobbing.models_remote.skills import Skills # noqa: E501
from jobbing.models_remote.state_code import StateCode # noqa: E501
from jobbing.models_remote.status import Status # noqa: E501
from jobbing.models_remote.user_role import UserRole # noqa: E501 
from jobbing.models_remote.zip_code import ZipCode # noqa: E501
from jobbing.models_remote.org import Org # noqa: E501

from jobbing.login import token_required

@token_required
def get_colonies(): # noqa: E501
    """get_colonies

    Show a listing of colonies # noqa: E501

    :rtype: List[Colony]
    """

    colonies = DBColony.query.all()
    if colonies == None:
        abort(404)
    return [Colony(c.id_colony_code, c.colony_name, c.id_municipality, c.id_zip_code) for c in colonies]

@token_required
def get_colony_by_id(id_colony_code): # noqa: E501
    """get_colony_by_id

    Get colony by id # noqa: E501

    :rtype: Colony
    """

    colony = DBColony.query.filter(DBColony.id_colony_code == id_colony_code).first()
    if colony == None:
        abort(404)
    return Colony(colony.id_colony_code, colony.colony_name, colony.id_municipality, colony.id_zip_code)

@token_required
def get_colonies_with_filter(id_zip_code=None, id_municipality=None): # noqa: E501
    """get_colonies_with_filter

    Get colonies with filter # noqa: E501

    :rtype: List[Colony]
    """

    if id_zip_code is not None:
        if id_municipality is not None:
            colonies = filter(lambda c: c.id_municipality==id_municipality, get_colonies_by_zip(id_zip_code))
            return [Colony(c.id_colony_code, c.colony_name, c.id_municipality, c.id_zip_code) for c in colonies]
        return get_colonies_by_zip(id_zip_code)
    elif id_municipality is not None:
        return get_colonies_by_mun(id_municipality)
    return get_colonies()

@token_required
def get_colonies_by_zip(id_zip_code): # noqa: E501
    """get_colonies_by_zip

    Get colonies by zip # noqa: E501

    :rtype: List[Colony]
    """

    colonies = DBColony.query.filter(DBColony.id_zip_code == id_zip_code)
    if colonies == None:
        abort(404)
    return [Colony(c.id_colony_code, c.colony_name, c.id_municipality, c.id_zip_code) for c in colonies]

@token_required
def get_colonies_by_mun(id_municipality): # noqa: E501
    """get_colonies_by_mun

    Get colonies by municipality # noqa: E501

    :rtype: List[Colony]
    """

    colonies = DBColony.query.filter(DBColony.id_municipality == id_municipality)
    if colonies == None:
        abort(404)
    return [Colony(c.id_colony_code, c.colony_name, c.id_municipality, c.id_zip_code) for c in colonies]

@token_required
def get_countries(): # noqa: E501
    """get_countries

    Show a listing of countries # noqa: E501

    :rtype: List[CountryCode]
    """
    countries = DBCountryCode.query.all()
    if countries == None:
        abort(404)
    return [CountryCode(c.id_country_code, c.country_code, c.country_name) for c in countries]
    
@token_required
def get_country_by_id(id_country_code): # noqa: E501
    """get_country_by_id

    Get country by id # noqa: E501

    :rtype: CountryCode
    """
    country = DBCountryCode.query.filter(DBCountryCode.id_country_code == id_country_code).first()
    if country == None:
        abort(404)
    return CountryCode(country.id_country_code, country.country_code, country.country_name)

@token_required
def get_municipalities(): # noqa: E501
    """get_municipalities

    Show a listing of municipalities # noqa: E501

    :rtype: List[Municipality]
    """
    muns = DBMunicipality.query.all()
    if muns == None:
        abort(404)
    return [Municipality(m.id_municipality, m.municipality_name, m.id_state_code) for m in muns]

@token_required
def get_municipality_by_id(id_municipality): # noqa: E501
    """get_municipality_by_id

    Get municipality by id # noqa: E501

    :rtype: Municipality
    """
    mun = DBMunicipality.query.filter(DBMunicipality.id_municipality == id_municipality).first()
    if mun == None:
        abort(404)
    return Municipality(mun.id_municipality, mun.municipality_name, mun.id_state_code)

@token_required
def get_municipalities_with_filter(id_state_code=None): # noqa: E501
    """get_municipalities_with_filter

    Get municipalities with filter # noqa: E501

    :rtype: List[Municipality]
    """
    if id_state_code is not None:
        return get_municipalities_by_state(id_state_code)
    return get_municipalities()

@token_required
def get_municipalities_by_state(id_state_code): # noqa: E501
    """get_municipalities_by_state

    Get municipalities by state # noqa: E501

    :rtype: List[Municipality]
    """
    muns = DBMunicipality.query.filter(DBMunicipality.id_state_code == id_state_code)
    if muns == None:
        abort(404)
    return [Municipality(m.id_municipality, m.municipality_name, m.id_state_code) for m in muns]

@token_required
def get_skills(): # noqa: E501
    """get_skills

    Show a listing of skills # noqa: E501

    :rtype: List[Skills]
    """
    skills = DBSkills.query.all()
    if skills == None:
        abort(404)
    return [Skills(s.skills_id, s.skills_name, s.skills_media_id, s.skills_description, s.skills_updated_date) for s in skills]

@token_required
def get_skill_by_id(skills_id): # noqa: E501
    """get_skills_by_id

    Get skill by id # noqa: E501


    :rtype: Skills
    """

    skill = DBSkills.query.filter(DBSkills.skills_id == skills_id).first()
    if skill == None:
        abort(404)
    return Skills(skill.skills_id, skill.skills_name, skill.skills_media_id, skill.skills_description, skill.skills_updated_date)

@token_required
def get_states(): # noqa: E501
    """get_states

    Show a listing of states # noqa: E501

    :rtype: List[StateCode]
    """
    states = DBStateCode.query.all()
    if states == None:
        abort(404)
    return [StateCode(s.id_state_code, s.state_code, s.state_name, s.id_country_code) for s in states]

@token_required
def get_state_by_id(id_state_code): # noqa: E501
    """get_state_by_id

    Get state by id # noqa: E501

    :rtype: StateCode
    """
    state = DBStateCode.query.filter(DBStateCode.id_state_code == id_state_code).first()
    if state == None:
        abort(404)
    return StateCode(state.id_state_code, state.state_code, state.state_name, state.id_country_code)

@token_required
def get_states_with_filter(id_country_code=None): # noqa: E501
    """get_states_with_filter

    Get states with filter # noqa: E501

    :rtype: List[StateCode]
    """
    if id_country_code is not None:
        return get_states_by_country(id_country_code)
    return get_states()

@token_required
def get_states_by_country(id_country_code): # noqa: E501
    """get_states_by_country

    Get states by country # noqa: E501

    :rtype: List[StateCode]
    """
    states = DBStateCode.query.filter(DBStateCode.id_country_code == id_country_code)
    if states == None:
        abort(404)
    return [StateCode(s.id_state_code, s.state_code, s.state_name, s.id_country_code) for s in states]

@token_required
def get_statuses(): # noqa: E501
    """get_statuses

    Show a listing of statuses # noqa: E501

    :rtype: List[Status]
    """
    statuses = DBStatus.query.all()
    if statuses == None:
        abort(404)
    return [Status(s.status_id, s.status_name, s.status_updated_date) for s in statuses]

@token_required
def get_status_by_id(status_id): # noqa: E501
    """get_status_by_id

    Get status by id # noqa: E501

    :rtype: Status
    """
    status = DBStatus.query.filter(DBStatus.status_id == status_id).first()
    if status == None:
        abort(404)
    return Status(status.status_id, status.status_name, status.status_updated_date)

@token_required
def get_user_roles(): # noqa: E501
    """get_user_roles

    Show a listing of user roles # noqa: E501

    :rtype: List[UserRole]
    """

    roles = DBUserRole.query.all()
    if roles == None:
        abort(404)
    return [UserRole(r.user_role_id, r.user_role_name, r.user_role_updated_date) for r in roles]

@token_required
def get_user_role_by_id(user_role_id): # noqa: E501
    """get_user_role_by_id

    Get user role by id # noqa: E501

    :rtype: UserRole
    """

    r = DBUserRole.query.filter(DBUserRole.user_role_id == user_role_id).first()
    if r == None:
        abort(404)
    return UserRole(r.user_role_id, r.user_role_name, r.user_role_updated_date)

@token_required
def get_zip_codes(): # noqa: E501
    """get_zip_codes

    Show a listing of zip codes # noqa: E501

    :rtype: List[ZipCode]
    """

    zip_codes = DBZipCode.query.all()
    if zip_codes == None:
        abort(404)
    return [ZipCode(z.id_zip_code, z.zip_code) for z in zip_codes]

@token_required
def get_zip_code_by_id(id_zip_code): # noqa: E501
    """get_zip_code_by_id

    Get zip code by id # noqa: E501

    :rtype: ZipCode
    """

    zip_code = DBZipCode.query.filter(DBZipCode.id_zip_code == id_zip_code).first()
    if zip_code == None:
        abort(404)
    return ZipCode(zip_code.id_zip_code, zip_code.zip_code)

# @token_required
def get_orgs(): # noqa: E501
    """get_orgs

    Show a listing of orgs # noqa: E501

    :rtype: List[Org]
    """
    orgs = DBOrg.query.all()
    if orgs == None:
        abort(404)
    return [Org(o.org_id, o.org_name, o.org_media_id) for o in orgs]
    
# @token_required
def get_org_by_id(org_id): # noqa: E501
    """get_org_by_id

    Get org by id # noqa: E501

    :rtype: Org
    """
    org = DBOrg.query.filter(DBOrg.org_id == org_id).first()
    if org == None:
        abort(404)
    return Org(org.org_id, org.org_name, org.org_media_id)