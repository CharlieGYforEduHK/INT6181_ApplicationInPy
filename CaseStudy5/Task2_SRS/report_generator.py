import os
from typing import Dict, Any
import pandas as pd

class ReportGenerator:
    @staticmethod
    def export_summary_text(summary: Dict[str, Any], at_risk_df: pd.DataFrame, output_path: str = "summary_report.txt") -> str:
        lines = [
            "==================================================",
            "      EduTrack Learning Analytics Summary Report  ",
            "==================================================",
            f"Total Students Evaluated: {summary['total_students']}",
            f"Class Average Score:      {summary['class_mean']:.2f}%",
            f"Class Score Median:       {summary['class_median']:.2f}%",
            f"Pass Rate:                {summary['pass_rate']:.1f}%",
            f"Average Attendance:       {summary['avg_attendance']:.1f}%",
            f"Average Study Hours:      {summary['avg_study_hours']:.1f} hrs/week",
            "--------------------------------------------------",
            f"At-Risk Students Identified: {len(at_risk_df)}",
            "--------------------------------------------------"
        ]
        
        for _, row in at_risk_df.iterrows():
            lines.append(f"ID: {row['student_id']} | Name: {row['name']} | Overall: {row['overall_score']:.1f}")
            lines.append(f"Reasons: {row['risk_reasons']}")
            lines.append("-")

        content = "\n".join(lines)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return output_path