def get_summary(df):

    return {
        "Total Transactions":
            len(df),

        "Average Carpet Area":
            round(
                df["carpet_area"].fillna(0).mean(),
                2
            ),

        "Average Total Area":
            round(
                df["total_area"].fillna(0).mean(),
                2
            )
    }
