def risk_score(likelihood,impact,control_effectiveness):
    for x in (likelihood,impact,control_effectiveness):
        if not 0<=x<=1: raise ValueError("values must be between 0 and 1")
    return round(likelihood*impact*(1-control_effectiveness),4)
