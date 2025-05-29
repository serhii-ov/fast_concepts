from jose import jwt, JWTError
from datetime import datetime, timedelta

from config import SECRET_KEY, ALGORITHM


def create_access_token(
        data: dict, 
        secret_key: str,
        expire_delta: timedelta = None,
        ):
    """Create current user's timed access token."""

    to_encode = data.copy()
    expire = datetime.now() + (expire_delta or timedelta(minutes=10))
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode, secret_key=SECRET_KEY, algorithm=ALGORITHM,
        )


def verify_token(token: str):
    """Verify token"""

    try:
        verified_token = jwt.decode(
                                    token, SECRET_KEY, 
                                    algorithms=[ALGORITHM],
                                    )
        return verified_token
    except JWTError:
        return None
