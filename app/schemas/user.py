from pydantic import BaseModel, Field, EmailStr, UUID4, ConfigDict
from datetime import datetime


class UserBaseSchema(BaseModel):
    first_name: str = Field(
        description="User's first name",
        min_length=1,
        max_length=100,
        examples=["John"],
    )
    last_name: str = Field(
        description="User's last name",
        min_length=1,
        max_length=100,
        examples=["Doe"],
    )
    email: EmailStr = Field(
        description="User's email address (unique)",
        examples=["user@example.com"],
    )
    phone_number: str = Field(
        description="User's phone number (unique)",
        examples=["+58763451"],
    )
    telegram_link: str = Field(
        description="User's telegram link",
        examples=["https://t.me/User"],
    )
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "email": "user@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "phone_number": "+58763451",
                    "telegram_link": "https://t.me/User",
                },
            ],
        },
    )


class UserCreateSchema(UserBaseSchema):
    pass


class UserResponseSchema(UserBaseSchema):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "email": "user@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "phone_number": "+58763451",
                    "telegram_link": "https://t.me/User",
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "updated_at": "2023-11-15 14:30:45+00",
                    "created_at": "2023-11-11 14:30:45+00",
                },
            ],
        },
    )
