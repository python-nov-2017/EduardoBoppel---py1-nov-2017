

def get_data(info, data):


    if data.upper() == "ALL":
        print "Here is my information:"

        for key, data in info.iteritems():
            print key +": "+ data

    elif data.upper() == "NAME":
        print "My name is", info.get('name_last')+ "... " + info.get('name_first') + " " + info.get('name_last')

    elif data.upper() == "COUNTRY":
        print "My country of birth is {}, and I currently live in {}".format(info.get('country_birth'), info.get('country_living'))

    elif data.upper() == "LANG":
        print "My favorite languate {}, and I am currently learning {}".format(info.get('language_favorite'), info.get('language_learning'))

    else:
        print "Data is not available"





personal_info = {
    'name_first': "Eduardo",
    'name_last': "Boppel",
    'country_birth': "Guatemala",
    'country_living': "Guatemala",
    'language_favorite': "All",
    'language_learning': "Python"
}

get_data(personal_info, "lang")   # ALL, NAME, COUNTRY, LANG
