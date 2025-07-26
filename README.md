# Pareto‑Optimal Multi‑Criteria Pathfinding

A scalable and optimized iteration on the proof-of-concept for multi‑criteria route optimization using Pareto‑optimality. This project demonstrates:

- **O(1) edge updates** via dict‑based adjacency  
- **Cached Pareto dominance** with `@lru_cache`  
- **ε‑Pruning** to bound frontier growth  
- **`__slots__`** for memory‑efficient `Label` objects  
- **SQLite streaming** for on‑disk neighbor queries  

## Repository

- **pathfinder/**  
  - `graph.py` — In‑memory/disk‐backed graph with O(1) updates  
  - `label.py` — Lightweight `Label` with memoized dominance  
  - `label_set.py` — Pareto frontier with optional ε‑pruning  
  - `priority_queue.py` — Lexicographic min‑heap  

- **tests/**  
  - **Performance benchmarks**: `performance_tests.py`  
  - **Functional correctness and robustness**: `test_validation.py`

- **requirements.txt** — `pytest>=6.0`  

## Installation

```bash
git clone https://github.com/Oishani/MSCS_532_Project_Phase_3.git
cd MSCS_532_Project_Phase_3
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

- **Unit & Validation Tests**  
  ```bash
  python3 -m pytest -q -s --disable-warnings tests/test_validation.py > tests/validation_results.txt
  ```
- **Performance Benchmarks**  
  ```bash
  python3 performance_tests.py | tee performance_results.txt
  ```

## Next Steps

- **Custom criteria weighting** and comparator plug‑ins  
- **Spatial indexing** (R‑tree, contraction hierarchies) for faster lookups  
- **Parallel label expansion** via threading or async I/O  
- **Adaptive ε‑pruning** based on frontier growth  
- **Hybrid caching** for mixed in‑memory and on‑disk performance