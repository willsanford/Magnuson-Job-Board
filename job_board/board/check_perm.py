from django.shortcuts import redirect
from django.contrib import messages

# This funciton will check the permissions of a user and possibly redirect them to a different page if need be
# Params:
# - request: the page request that can be used to get the user or add messages 
# - user: a boolean that says that someone must be a user to view this page. By default False
# - admin: a boolean that says a user must be an admin to view this page. By default False
# Returns:
# (bool, redirect) - this return a tuple of a boolean and a redirect object. If the boolean is False, then the user 
#   passes the permission check. If it is True, the user should be redirected to the redirect object. If the user is 
#   passed a valid user for this page, then the redirect object will be None.

def check_permissions(request,user=False,admin=False):

    # user check
    if user:
        if not(request.user.is_authenticated):
            messages.warning(request, 'You must be logged in to view this page. Please log in.')
            return ( True , redirect('login') )
    
    # admin check
    # if admin:
    #     if not():
    #         messages.warning(request, 'You must have admin priverleged to view this page. If you think you should have these priverleges, then please contact the Magnuson Center staff')
    #         return ( True , redirect('board-home'))

    return (False, None)
            