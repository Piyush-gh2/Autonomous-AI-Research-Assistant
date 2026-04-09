def generate_report(query, insights, conclusion):
    return f"""
    🔍 Research Topic: {query}

    📊 Key Insights:
    {"".join(insights)}

    🧠 Conclusion:
    {conclusion}
    """