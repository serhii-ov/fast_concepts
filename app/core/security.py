from jose import jwt, JWTError
from datetime import datetime, timedelta
from passlib.context import CryptContext

from config import SECRET_KEY, ALGORITHM


# bcrypt is the most commonly used algorithm
password_context = CryptContext(
                                schemes=["bcrypt"], 
                                deprecated="auto",
                                )


def get_password_hash(password: str) -> str:
    """Hash a plain-text password."""
    return password_context.hash(password)


def verify_password(plain_password: str, hashed_password: str,) -> bool:
    """Verify a plain-text password against the hashed one."""
    return password_context.verify(plain_password, hashed_password)


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
