names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.


def solutin(names):
    *nordict_countries, es, ru = names
    return (nordict_countries, es, ru)


print(solutin(names))

