import os
from typing import List
import pandas as pd

class DataValidationError(Exception):
    """Custom exception raised for errors in input CSV data validation."""
    pass

class DataLoader:
    REQUIRED_COLUMNS: List[str] = [
        'student_id', 'name', 'subject', 'quiz_score', 
        'assignment_score', 'exam_score', 'attendance', 'study_hours'
    ]
    NUMERIC_SCORE_FIELDS: List[str] = ['quiz_score', 'assignment_score', 'exam_score', 'attendance']

    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_and_validate(self) -> pd.DataFrame:
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Error: Target data file '{self.filepath}' was not found.")

        try:
            df = pd.read_csv(self.filepath)
        except Exception as err:
            raise DataValidationError(f"Failed to read CSV file: {err}")

        # Validate column headers
        missing_cols = [col for col in self.REQUIRED_COLUMNS if col not in df.columns]
        if missing_cols:
            raise DataValidationError(f"Missing required columns in CSV: {missing_cols}")

        # Check for null values
        if df[self.REQUIRED_COLUMNS].isnull().any().any():
            null_cols = df.columns[df.isnull().any()].tolist()
            raise DataValidationError(f"Dataset contains null/missing values in columns: {null_cols}")

        # Range validation (0 - 100)
        for field in self.NUMERIC_SCORE_FIELDS:
            invalid_rows = df[~df[field].between(0, 100)]
            if not invalid_rows.empty:
                row_indices = invalid_rows.index.tolist()
                raise DataValidationError(
                    f"Invalid values in '{field}' for row indices {row_indices}. Scores must be between 0 and 100."
                )

        return df