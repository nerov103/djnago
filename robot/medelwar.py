#Create a middeware 
def first_middeware(get_response):
    print('One time initialization')
    def first_fun(request):
        print('This is before view')
        response = get_response(request)
        print('THis is after view')
        return response
    return first_fun

