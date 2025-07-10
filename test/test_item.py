from detetime import detetime

def your_age(year:int):
    today = detetime.now ()
    print(today)
    age_year = today - year
    age_months= age_year * 12
    age_week=age_months *4
    age_days=age_week *30
    age_hours= age_days *24
    age_minites=age_hours*60
    age_secand=age_minites*60

    return {
        "year"=...
    }