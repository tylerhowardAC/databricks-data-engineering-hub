from data_engineering.quality import validate_records
from ml.drift import population_shift
from governance.risk import risk_score
from ai.policy import evaluate_agent_action
from database.partition import partition_quality
from fabric.pipeline import readiness

def test_quality(): assert validate_records([{"id":1},{"id":2,"name":"x"}], ["id","name"])["accepted"]==1
def test_drift(): assert population_shift([1,1,1],[2,2,2])>0
def test_risk(): assert risk_score(.8,.8,.5)==.32
def test_policy(): assert evaluate_agent_action({"tool":"search","risk":.2},["search"])["allow"]
def test_partition(): assert partition_quality(["a","a","b"])["skew"]==2
def test_pipeline(): assert readiness(["ingest","quality","transform","publish"])["ready"]
