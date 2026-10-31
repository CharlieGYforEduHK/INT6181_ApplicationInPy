from typing import Dict, Any
import pandas as pd

class AnalyticsEngine:
    QUIZ_WEIGHT: float = 0.30
    ASSIGNMENT_WEIGHT: float = 0.30
    EXAM_WEIGHT: float = 0.40
    PASSING_SCORE: float = 50.0

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def calculate_overall_scores(self) -> pd.DataFrame:
        """Calculates weighted overall score according to SRS FR-2 specification."""
        self.df['overall_score'] = (
            self.df['quiz_score'] * self.QUIZ_WEIGHT +
            self.df['assignment_score'] * self.ASSIGNMENT_WEIGHT +
            self.df['exam_score'] * self.EXAM_WEIGHT
        ).round(2)
        return self.df

    def get_class_summary(self) -> Dict[str, Any]:
        """Generates class-level statistical metrics."""
        if 'overall_score' not in self.df.columns:
            self.calculate_overall_scores()

        overall = self.df['overall_score']
        return {
            "total_students": int(len(self.df)),
            "class_mean": float(overall.mean()),
            "class_median": float(overall.median()),
            "std_dev": float(overall.std()) if len(self.df) > 1 else 0.0,
            "pass_rate": float((overall >= self.PASSING_SCORE).mean() * 100),
            "avg_attendance": float(self.df['attendance'].mean()),
            "avg_study_hours": float(self.df['study_hours'].mean())
        }