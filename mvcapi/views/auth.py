from mvcapi.models import User  # Importing the User model from mvcapi.models
from rest_framework.decorators import api_view  # Importing the api_view decorator from rest_framework.decorators
from rest_framework.response import Response  # Importing the Response class from rest_framework.response

@api_view(['POST'])
def check_user(request):
    """
    Checks to see if User has associated User.
    
    This function is a view that handles the HTTP POST request. It checks if a User with a specific UID exists in the database
    and returns the user's information if found.
    
    Args:
        request: The HTTP request object containing the data sent by the client.
            - The 'uid' parameter is expected to be present in the request data.
    
    Returns:
        A Response object containing the user's information if found, or a response indicating that the user is not valid.
    """
    
    uid = request.data['uid']  # Extract the 'uid' parameter from the request data
    
    # Query the User model to find the user with the given UID
    user = User.objects.filter(uid=uid).first()
    
    if user is not None:
        # If the user exists, create a dictionary containing the user's information
        data = {
            'id': user.id,
            'user_name': user.user_name,
            'email': user.email,
            'profile_image_url': user.profile_image_url,
            'bio': user.bio,
            'uid': user.uid
        }
        return Response(data)  # Return the user's information in the response
    else:
        data = {'valid': False}  # If the user does not exist, create a dictionary indicating that the user is not valid
        return Response(data)  # Return the validation response

@api_view(['POST'])
def register_user(request):
    """
    Handles the creation of a new gamer for authentication.
    
    This function is a view that handles the HTTP POST request. It creates a new User record in the database using the provided
    user information and returns the created user's information.
    
    Args:
        request: The HTTP request object containing the data sent by the client.
            - The following parameters are expected to be present in the request data:
                - 'user_name': The username of the new user.
                - 'email': The email of the new user.
                - 'profile_image_url': The profile image URL of the new user.
                - 'bio': The bio of the new user.
                - 'uid': The UID of the new user.
    
    Returns:
        A Response object containing the created user's information.
    """
    
    # Create a new User record in the database using the provided user information
    user = User.objects.create(
        user_name=request.data['user_name'],
        email=request.data['email'],
        profile_image_url=request.data['profile_image_email'],
        bio=request.data['bio'],
        uid=request.data['uid']
    )

    # Create a dictionary containing the created user's information
    data = {
        'id': user.id,
        'user_name': user.user_name,
        'email': user.email,
        'profile_image_url': user.profile_image_url,
        'bio': user.bio,
        'uid': user.uid
    }
    
    return Response(data)  # Return the created user's information in the response

