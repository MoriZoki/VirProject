from django.utils import timezone

# check vip middleware

class CheckVip:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
    
        if request.user.is_authenticated:
            if request.user.vip_end_time <= timezone.now():
                request.user.is_vip = False
                request.user.save()
        
        response = self.get_response(request)

        return response

