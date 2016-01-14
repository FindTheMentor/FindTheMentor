from django.utils import translation
 
def set_language_via_domain( request ):
    language = translation.get_language_from_request(request)
    #print "language from request: ", language, " uri: ", request.build_absolute_uri()
    # note this will be ignored on local debug:
    if request.build_absolute_uri().find("mysitedomain.jp") != -1:
        language = "ja"
    elif request.build_absolute_uri().find("192.168.1.203") != -1: #dev / test!
        language = "ja"
    elif request.build_absolute_uri().find("mysitedomain.com") != -1:
        language = "en"
    elif request.build_absolute_uri().find("127.0.0.1:8000") != -1: #dev / test!
        language = "id"
    elif request.build_absolute_uri().find("127.0.0.1:8080") != -1: #dev / test!
        language = "en"
    #set lang.
    translation.activate(language)
    return {
        "uri":request.build_absolute_uri()
        }
