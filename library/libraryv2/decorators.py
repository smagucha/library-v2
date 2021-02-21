from django.http  import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			print('working', allowed_roles)
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()
				print(group)
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('you are not authorized')
				
				print(group)
		return wrapper_func
	return decorator