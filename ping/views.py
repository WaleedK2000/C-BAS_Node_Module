from rest_framework.response import Response
from rest_framework.decorators import api_view

import docker


# Just to check if application is running
@api_view(['GET'])
def simple_ping(request):

    response = {'running': 'TRUE', 'status': 'ok'}
    return Response(response)