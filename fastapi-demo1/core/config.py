from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
	PROJECT_NAME: str = "fastapi-demo"

	API_V1_STR: str = "/api/v1"

	SECRET_KEY: str = "YF1rnTkk0Ba_yCAXN6BSXPVY4FWCHBohypUKIchDCmU"
	SALT_ROUNDS: int = 4

	# JWT expiration time
	ACCESS_TOKEN_EXPIRES_MINUTES: int = 60 * 24

	# Cross-domain request configuration
	BACKEND_CORS_ORIGINS: List = ["*"]

	# Database configuration
	MYSQL_USER: str = ""
	MYSQL_PASS: str = ""
	MYSQL_HOST: str = ""
	MYSQL_DB: str = ""
	MYSQL_PORT: str = ""
	SQLALCHEMY_DATABASE_URI: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

	# Redis store address
	REDIS_STORAGE = "redis://127.0.0.1:6379/?password="

	class Config:
		case_sensitive = True


settings = Settings()
