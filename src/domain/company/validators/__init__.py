from ....helpers import InvalidDBAccessException, InvalidDataException
from .company_validators import validate_companies_get_data, validate_companies_post_data
from .cadidate_validators import validate_candidates_get_data

def validate_db_session(session):
    if not session:
        raise InvalidDBAccessException('db not connected')
    return False