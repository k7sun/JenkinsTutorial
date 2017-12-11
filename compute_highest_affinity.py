def highest_affinity2(site_list, user_list, time_list):
    print('a bunch or junk')
    print('a bunch or junk')    
    print('a bunch or junk')
    print('a bunch or junk')
    print('a bunch or junk')
    print('a bunch or junk')
    visits = zip(user_list, site_list)
    visits_by_user = dict()
    site_aff = dict()

    for (user, site) in visits:
        if not user in visits_by_user:
            visits_by_user[user] = set()
        visits_by_user[user].add(site)

    for (user, sites) in visits_by_user.items():
        for site1 in sites:
            for site2 in sites:
                if site1 != site2:
                    key = [site1, site2]
                    key.sort()
                    key = key[0] + ',' + key[1]
                    if not key in site_aff:
                        site_aff[key] = 0

                    site_aff[key] = site_aff[key] + 1

    site_aff_ordered = sorted(site_aff, key=site_aff.get, reverse=True)
    return tuple(site_aff_ordered[0].split(','))

def highest_affinity(site_list, user_list, time_list):
    visits = zip(user_list, site_list)
    visits_by_user = dict()
    site_aff = dict()

    for (user, site) in visits:
        if not user in visits_by_user:
            visits_by_user[user] = set()
        visits_by_user[user].add(site)

    for (user, sites) in visits_by_user.items():
        for site1 in sites:
            for site2 in sites:
                if site1 != site2:
                    key = [site1, site2]
                    key.sort()
                    key = key[0] + ',' + key[1]
                    if not key in site_aff:
                        site_aff[key] = 0

                    site_aff[key] = site_aff[key] + 1

    site_aff_ordered = sorted(site_aff, key=site_aff.get, reverse=True)
    return tuple(site_aff_ordered[0].split(','))
