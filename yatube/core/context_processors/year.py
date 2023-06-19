def year(request):
    import datetime
    return {
        'year': datetime.datetime.now().year
    }
