from typing import List
import pandas as pd

class RiskDetector:
    ACADEMIC_RISK_THRESHOLD: float = 50.0
    ATTENDANCE_RISK_THRESHOLD: float = 75.0
    EXAM_RISK_THRESHOLD: float = 50.0

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def identify_at_risk_students(self) -> pd.DataFrame:
        """Identifies at-risk students based on SRS FR-4 criteria."""
        conditions = (
            (self.df['overall_score'] < self.ACADEMIC_RISK_THRESHOLD) |
            (self.df['attendance'] < self.ATTENDANCE_RISK_THRESHOLD) |
            (self.df['exam_score'] < self.EXAM_RISK_THRESHOLD)
        )
        at_risk_df = self.df[conditions].copy()
        
        reasons: List[str] = []
        for _, row in at_risk_df.iterrows():
            flag_reasons = []
            if row['overall_score'] < self.ACADEMIC_RISK_THRESHOLD:
                flag_reasons.append(f"Low overall score ({row['overall_score']:.1f} < 50)")
            if row['attendance'] < self.ATTENDANCE_RISK_THRESHOLD:
                flag_reasons.append(f"Low attendance ({row['attendance']:.1f}% < 75%)")
            if row['exam_score'] < self.EXAM_RISK_THRESHOLD:
                flag_reasons.append(f"Low exam score ({row['exam_score']:.1f} < 50)")
            reasons.append(" | ".join(flag_reasons))

        at_risk_df['risk_reasons'] = reasons
        return at_risk_df