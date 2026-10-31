from typing import List
import pandas as pd

class Recommender:
    @staticmethod
    def generate_recommendation(student_row: pd.Series) -> str:
        advice: List[str] = []
        if student_row['quiz_score'] < 60:
            advice.append("Review weekly quiz concepts and complete practice problems.")
        if student_row['assignment_score'] < 60:
            advice.append("Seek lab teaching assistant guidance on assignment submissions.")
        if student_row['exam_score'] < 50:
            advice.append("Schedule one-on-one consultation for exam revision.")
        if student_row['attendance'] < 75:
            advice.append("Improve lecture attendance to maintain course engagement.")
        
        if not advice:
            advice.append("Performance is satisfactory; maintain current study schedule.")

        return " ".join(advice)