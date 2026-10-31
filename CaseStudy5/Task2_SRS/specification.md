# Software Requirements Specification (SRS)
## EduTrack: A Learning Analytics Dashboard for Monitoring Student Performance

### 1. Introduction
EduTrack is a modular Python application designed for educators to monitor student performance, detect learning risks, and derive actionable academic recommendations from CSV datasets.

### 2. System Architecture & Component Design
The system consists of modular components:
- `data_loader.py`: Handles CSV ingestion and input validation.
- `analytics.py`: Computes weighted scores and class statistics.
- `risk_detector.py`: Implements rule-based risk evaluation.
- `recommender.py`: Generates targeted learning advice.
- `main.py`: Interactive Command-Line Interface (CLI).

### 3. Functional Requirements
- **FR-1 Data Ingestion & Validation**: Import CSV datasets containing `student_id`, `name`, `subject`, `quiz_score`, `assignment_score`, `exam_score`, `attendance`, and `study_hours`. Reject missing values or out-of-bound scores (not in 0–100).
- **FR-2 Weighted Score Calculation**: Calculate overall performance score using:
  Overall Score = 0.30 * Quiz + 0.30 * Assignment + 0.40 * Exam
- **FR-3 Class Analytics**: Compute class mean score, pass rate (>= 50%), and average attendance rate.
- **FR-4 At-Risk Detection**: Flag students as "At Risk" if overall score < 50, attendance < 75%, or exam score < 50.
- **FR-5 Recommendations**: Output student-specific intervention feedback based on identified performance weaknesses.

### 4. Non-Functional Requirements & Constraints
- **Usability**: Provide descriptive error messages identifying field name upon validation failure.
- **Maintainability**: Follow standard Python PEP 8 guidelines and modular architecture.
- **Execution Constraints**: Built strictly using standard Python packages / `pandas`.

### 5. Evaluation & Testing Plan
- **Data Ingestion Tests**: Verify handling of valid CSV, missing columns, out-of-range values, and nonexistent files.
- **Calculation Verification**: Test exact match of calculated overall scores and class averages against manual calculations.