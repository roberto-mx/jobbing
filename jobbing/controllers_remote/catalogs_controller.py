"""
Catalogs are read only tables
"""

from flask import abort

# DB Models
from jobbing.DBModelsRemote import ZipCode as DBZipCode

# Swagger Models
from jobbing.models_remote.zip_code import ZipCode # noqa: E501

def get_zip_codes(): # noqa: E501
    """get_zip_codes

    Show a listing of zip codes # noqa: E501

    :rtype: List[ZipCode]
    """

    zip_codes = DBZipCode.query.all()
    if zip_codes == None:
        abort(404)
    return [ZipCode(z.id_zip_code, z.zip_code) for z in zip_codes]

def get_zip_code_by_id(id_zip_code): # noqa: E501
    """get_zip_code_by_id

    Get zip code by id # noqa: E501

    :rtype: ZipCode
    """
 
    zip_code = DBZipCode.query.filter(DBZipCode.id_zip_code == id_zip_code).first()
    if zip_code == None:
        abort(404)
    return ZipCode(zip_code.id_zip_code, zip_code.zip_code)
