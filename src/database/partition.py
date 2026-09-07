def partition_quality(keys):
    if not keys: return {"unique_ratio":0.0,"skew":1.0}
    counts={k:keys.count(k) for k in set(keys)}
    return {"unique_ratio":round(len(set(keys))/len(keys),4),"skew":round(max(counts.values())/min(counts.values()),4)}
