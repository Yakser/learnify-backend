from users.serializers import UserProfileSerializer


def update_profile_fields(user, data):
    for field_name in UserProfileSerializer.Meta.fields:
        if data.get(field_name):
            setattr(user.profile, field_name, data.get(field_name))
    user.profile.save()
