class RiskDetector:
    def __init__(self, df):
        self.df = df

    def identify_at_risk_students(self):
        # 按照文档规则: 综合分<50 或 考勤<75% 或 考试分<50
        conditions = (
            (self.df['overall_score'] < 50) |
            (self.df['attendance'] < 75) |
            (self.df['exam_score'] < 50)
        )
        at_risk_df = self.df[conditions].copy()
        reasons = []
        for _, row in at_risk_df.iterrows():
            r = []
            if row['overall_score'] < 50:
                r.append("Overall score < 50")
            if row['attendance'] < 75:
                r.append("Low attendance (<75%)")
            if row['exam_score'] < 50:
                r.append("Low exam score (<50)")
            reasons.append("; ".join(r))
        at_risk_df['risk_reason'] = reasons
        return at_risk_df