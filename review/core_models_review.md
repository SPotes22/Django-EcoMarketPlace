# Code Review for puddle/core/models.py

This code defines a custom user model, `CustomUser`, for a Django project. Let's break it down section by section:

**1. Imports:**

```python
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
```

*   `django.contrib.auth.models`: Imports `AbstractUser`, `Group`, and `Permission` from Django's built-in authentication system.
    *   `AbstractUser`:  This is the base class for creating custom user models in Django. It provides a lot of the standard user fields and functionality.
    *   `Group`: Represents a group of users.  Users can belong to one or more groups, which allows for assigning permissions to a whole set of users at once.
    *   `Permission`: Represents a specific permission that a user or group can have.  Permissions control what actions users are allowed to perform.
*   `django.db.models`: Imports `models`, the base class for defining database models in Django.
*   `django.utils.timezone`: Imports `timezone` to work with timezone-aware datetime objects.

**2. `CustomUser` Class Definition:**

```python
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('it', 'IT'),
        ('ops', 'Ops'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='ops')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
```

*   **`class CustomUser(AbstractUser):`**: Defines a new model class named `CustomUser` that inherits from `AbstractUser`.  This means it inherits all the standard user fields like `username`, `password`, `first_name`, `last_name`, `is_staff`, `is_superuser`, `date_joined`, etc.

*   **`ROLE_CHOICES = (...)`**: Defines a tuple called `ROLE_CHOICES`. This tuple will be used as a set of possible values for the `role` field, providing a list of available roles for the user.
    *   `('admin', 'Admin')`:  The first element is the value stored in the database (e.g., 'admin'), and the second element is the human-readable name displayed in forms and the admin interface (e.g., 'Admin').

*   **`email = models.EmailField(unique=True)`**: Adds an `email` field to the `CustomUser` model.
    *   `models.EmailField`:  Specifies that this field will store an email address.
    *   `unique=True`:  Ensures that no two users can have the same email address. This acts as a constraint in the database.

*   **`role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='ops')`**:  Adds a `role` field to the `CustomUser` model.
    *   `models.CharField`:  Specifies that this field will store a short string.
    *   `max_length=10`:  Limits the maximum length of the string to 10 characters.
    *   `choices=ROLE_CHOICES`:  Restricts the possible values for this field to those defined in the `ROLE_CHOICES` tuple.  This provides a dropdown list or radio button options in forms.
    *   `default='ops'`:  Sets the default value for this field to 'ops'.  If a role is not explicitly set when creating a user, it will default to 'ops'.

*   **`is_active = models.BooleanField(default=False)`**: Adds an `is_active` field to the `CustomUser` model.
    *   `models.BooleanField`:  Specifies that this field will store a boolean value (True or False).
    *   `default=False`:  Sets the default value for this field to False. This means new users will be inactive by default. You'll likely need to activate them (e.g., via email verification or manual approval).

*   **`created_at = models.DateTimeField(default=timezone.now)`**: Adds a `created_at` field to the `CustomUser` model.
    *   `models.DateTimeField`:  Specifies that this field will store a date and time.
    *   `default=timezone.now`:  Sets the default value for this field to the current date and time when the user is created. `timezone.now` ensures that the datetime is timezone-aware, if your Django project is configured to use timezones.

*   **`ip_address = models.GenericIPAddressField(null=True, blank=True)`**:  Adds an `ip_address` field to the `CustomUser` model.
    *   `models.GenericIPAddressField`: Specifies that this field will store an IP address (either IPv4 or IPv6).
    *   `null=True`: Allows the field to be stored as `NULL` in the database, meaning it can be empty.
    *   `blank=True`: Allows the field to be empty in Django forms.

*   **`groups = models.ManyToManyField(...)`**:  This field manages the relationship between `CustomUser` and `Group` models. It allows users to be part of multiple groups.
    *   `models.ManyToManyField(Group)`: Defines a many-to-many relationship with the `Group` model.
    *   `related_name='customuser_set'`:  Specifies the reverse relationship name.  This allows you to access all the users in a group by using `group.customuser_set.all()`.  Without this, the default reverse relation name would be `user_set`, which might conflict with Django's default `User` model if you're using both.
    *   `blank=True`:  Allows a user to not belong to any groups.
    *   `help_text`:  Provides a helpful description for the field in Django forms and the admin interface.
    *   `verbose_name`:  Specifies a human-readable name for the field.

*   **`user_permissions = models.ManyToManyField(...)`**:  This field manages the relationship between `CustomUser` and `Permission` models. It allows you to assign specific permissions directly to a user, bypassing the group permissions.
    *   `models.ManyToManyField(Permission)`: Defines a many-to-many relationship with the `Permission` model.
    *   `related_name='customuser_set'`:  Specifies the reverse relationship name.  This allows you to access all the users with a specific permission by using `permission.customuser_set.all()`.
    *   `blank=True`:  Allows a user to not have any specific permissions.
    *   `help_text`:  Provides a helpful description for the field.
    *   `verbose_name`:  Specifies a human-readable name for the field.

**In Summary:**

This code defines a custom user model that extends Django's built-in `AbstractUser`.  It adds extra fields for:

*   Email (required and unique)
*   Role (limited to 'admin', 'it', or 'ops')
*   Account activation status (`is_active`)
*   Creation timestamp (`created_at`)
*   IP address (`ip_address`)

It also customizes the `groups` and `user_permissions` many-to-many fields to use a `related_name` of `customuser_set`, preventing conflicts and making it easier to query the relationships.

To use this `CustomUser` model in your Django project, you need to configure the `AUTH_USER_MODEL` setting in your `settings.py` file to point to your custom user model:

```python
# settings.py
AUTH_USER_MODEL = 'your_app_name.CustomUser'  # Replace your_app_name
```

You would also need to create migrations to apply the changes to your database:

```bash
python manage.py makemigrations
python manage.py migrate
```
