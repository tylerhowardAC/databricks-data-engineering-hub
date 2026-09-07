def evaluate_agent_action(action, allowed_tools, max_risk=0.4):
    if action.get("tool") not in allowed_tools: return {"allow":False,"reason":"tool_not_allowed"}
    risk=float(action.get("risk",1))
    return {"allow":risk<=max_risk,"reason":"ok" if risk<=max_risk else "risk_threshold_exceeded"}
