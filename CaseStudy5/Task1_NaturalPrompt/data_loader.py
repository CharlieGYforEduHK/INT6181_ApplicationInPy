import os
import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_and_validate(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Error: File '{self.filepath}' does not exist.")
        
        df = pd.read_csv(self.filepath)
        required_cols = ['student_id', 'name', 'subject', 'quiz_score', 'assignment_score', 'exam_score', 'attendance', 'study_hours']
        
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Error: Required column '{col}' is missing.")
                
        score_cols = ['quiz_score', 'assignment_score', 'exam_score', 'attendance']
        for col in score_cols:
            if df[col].isnull().any():
                raise ValueError(f"Error: Column '{col}' contains missing values.")
            if not df[col].between(0, 100).all():
                raise ValueError(f"Error: Column '{col}' must contain values between 0 and 100.")
                
        return df