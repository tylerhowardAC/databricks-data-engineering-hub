def readiness(stages):
    required={"ingest","quality","transform","publish"}; present=set(stages)
    return {"ready":required<=present,"missing":sorted(required-present)}
