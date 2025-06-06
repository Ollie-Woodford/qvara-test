def get_qvara_snippet(query):
    query = query.lower()
    if "volatility surface" in query:
        return (
            "In Qvara, a volatility surface is a 3D plot of implied volatility across maturities "
            "and strike prices. You can import or model your own surface to support options pricing "
            "and risk simulations."
        )
    elif "import position data" in query or "upload positions" in query:
        return (
            "To import position data, go to the 'Positions' tab in Qvara and use the CSV uploader. "
            "The system will auto-detect schema and allow manual mapping."
        )
    elif "scenario analysis" in query:
        return (
            "Qvara’s scenario analysis tool lets you simulate market moves (e.g., oil drop 10%) "
            "and see impacts on P&L and exposure in real time."
        )
    elif "risk analytics" in query:
        return (
            "Qvara offers advanced risk analytics including VaR, stress tests, and real-time exposure tracking. "
            "These tools help traders quantify and manage portfolio risk more effectively."
        )
    return "No specific Qvara information matched, answering based on general knowledge."
