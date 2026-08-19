# Databricks Data Engineering & Lakehouse Blueprint 🧱⚡️

Welcome to my personal Databricks learning repository and real-world enterprise data engineering lab! 

This project documents hands-on Lakehouse architecture patterns, Delta Lake transaction mechanics, PySpark/Delta Live Tables (DLT) data pipelines, and study strategies for the **Databricks Certified Data Engineer Associate** exam.

---

### 💡 Core Enterprise Engineering Principles

* **Medallion Architecture Pattern:** Enforce strict data quality progression across Bronze (raw ingestion), Silver (cleaned/validated), and Gold (business-level aggregation) tables.
* **ACID Integrity & Time Travel:** Leverage Delta Lake transaction logs (`_delta_log`) for deterministic updates, schema enforcement, `OPTIMIZE`, and `Z-ORDER` layout performance.
* **Incremental Processing at Scale:** Utilize Auto Loader (`cloudFiles`) and Structured Streaming for cost-efficient, continuous ingestion without manual partition management.
* **Unity Catalog Governance:** Implement unified governance across workspaces with three-level namespace (`catalog.schema.table`) and fine-grained access control.

---

## 📂 Repository Index & Study Directory

### 📘 Certification Guides & Resources
* [`Databricks-Data-Engineer-Associate-Resources.md`](./Databricks-Data-Engineer-Associate-Resources.md) - Exam domain breakdowns, Spark SQL/PySpark tactics, pipeline debugging, and official reference guides.

### 📝 Lakehouse Architecture Notes
* [`notes/Databricks-Lakehouse-Architecture.md`](./notes/Databricks-Lakehouse-Architecture.md) - In-depth breakdown of Delta Lake internals, Liquid Clustering, DLT expectations, and Unity Catalog.

### 🛠️ PySpark & Delta Lake ETL Scripts
* [`scripts/pyspark_delta_pipeline.py`](./scripts/pyspark_delta_pipeline.py) - Production-ready PySpark ETL script implementing Auto Loader, schema enforcement, and Delta table upserts (`MERGE INTO`).

---

### ⏱️ Data Engineer Associate Study Progress

- [x] Mastered Delta Lake ACID capabilities, compaction (`OPTIMIZE`), and vacuum retention
- [x] Configured Auto Loader (`cloudFiles`) for incremental JSON/Parquet ingestion
- [ ] Built Delta Live Tables (DLT) pipelines with `@dlt.expect_or_drop` quality constraints
- [ ] Managed Databricks Workflows, multi-task job clusters, and task dependency graphs

---
*Feel free to star ⭐️ this repository if you find these Databricks & Lakehouse engineering resources helpful.*
