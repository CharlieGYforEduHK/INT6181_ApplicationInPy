import os
from data_loader import DataLoader, DataValidationError
from analytics import AnalyticsEngine
from risk_detector import RiskDetector
from recommender import Recommender
from report_generator import ReportGenerator

def run_pipeline(csv_path: str):
    print(f"\n[Info] Ingesting dataset from: {csv_path}")
    loader = DataLoader(csv_path)
    df = loader.load_and_validate()

    analytics = AnalyticsEngine(df)
    df = analytics.calculate_overall_scores()
    summary = analytics.get_class_summary()

    print("\n==================================================")
    print("           Class Analytics Summary                ")
    print("==================================================")
    print(f"Total Enrolled:     {summary['total_students']}")
    print(f"Class Mean Score:   {summary['class_mean']:.2f}%")
    print(f"Class Median Score: {summary['class_median']:.2f}%")
    print(f"Pass Rate:          {summary['pass_rate']:.1f}%")
    print(f"Average Attendance: {summary['avg_attendance']:.1f}%")

    risk_detector = RiskDetector(df)
    at_risk_df = risk_detector.identify_at_risk_students()

    print(f"\n--- At-Risk Students Detected ({len(at_risk_df)}) ---")
    if at_risk_df.empty:
        print("No students are currently flagged as at-risk.")
    else:
        for _, row in at_risk_df.iterrows():
            rec = Recommender.generate_recommendation(row)
            print(f"\n• [{row['student_id']}] {row['name']} (Score: {row['overall_score']:.1f}%, Attendance: {row['attendance']}%)")
            print(f"  Risk Factor: {row['risk_reasons']}")
            print(f"  Recommendation: {rec}")

    report_file = ReportGenerator.export_summary_text(summary, at_risk_df, "summary_report.txt")
    print(f"\n✅ Summary report successfully generated at '{report_file}'")

def main():
    print("==================================================")
    print("   EduTrack SRS-Driven Analytics System          ")
    print("==================================================")
    
    default_path = "data/student_records.csv"
    user_input = input(f"Enter CSV filepath [Default: {default_path}]: ").strip()
    target_path = user_input if user_input else default_path

    try:
        run_pipeline(target_path)
    except (DataValidationError, FileNotFoundError) as err:
        print(f"\n❌ Validation Failure: {err}")
    except Exception as err:
        print(f"\n❌ Unexpected System Error: {err}")

if __name__ == "__main__":
    main()