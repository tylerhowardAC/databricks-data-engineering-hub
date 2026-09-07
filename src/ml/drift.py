def population_shift(reference,current):
    if not reference or not current: raise ValueError("samples required")
    ref=sum(reference)/len(reference); cur=sum(current)/len(current)
    return round(abs(cur-ref)/(abs(ref)+1e-9),4)
