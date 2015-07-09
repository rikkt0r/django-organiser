from django.forms import forms, CharField, BooleanField


class LoginForm(forms.Form):
    username = CharField(
        label="Email or login",
        max_length="80",
        required=True
    )

    password = CharField(
        label="Password",
        max_length="80",
        required=True
    )

    remember = BooleanField(required=False)

# <div class="form-group">
#     <label for="username">Email or login</label>
#     <input type="text" class="form-control" id="username" name="username" placeholder="Email or login">
# </div>
#
# <div class="form-group">
#     <label for="password">Password</label>
#     <input type="password" class="form-control" id="password" name="password" placeholder="Password">
# </div>
#
# <div class="checkbox">
#     <label>
#       <input type="checkbox"> Remember me ?
#     </label>
# </div>
