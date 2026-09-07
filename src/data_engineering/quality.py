def validate_records(records, required_fields):
    errors=[]
    for i,r in enumerate(records):
        missing=[f for f in required_fields if not r.get(f)]
        if missing: errors.append({"row":i,"missing":missing})
    return {"valid":not errors,"errors":errors,"accepted":len(records)-len(errors)}
