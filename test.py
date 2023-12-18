from datetime import datetime


def calculate_annualized_return(
    investment_amount,
    current_value,
    start_date,
    end_date=datetime.now().strftime("%Y-%m-%d"),
):
    """
    Calculate the annualized return of an investment.

    :param investment_amount: Initial amount invested.
    :param current_value: The current or end value of the investment.
    :param start_date: The date when the investment was made (format: 'YYYY-MM-DD').
    :param end_date: The end date for the calculation (format: 'YYYY-MM-DD'). Defaults to today's date.
    :return: Annualized return as a percentage.
    """
    # Convert dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the number of years
    years_elapsed = (end_date - start_date).days / 365.25

    # Calculate the annualized return
    annualized_return = (current_value / investment_amount) ** (1 / years_elapsed) - 1

    # Convert to percentage
    return annualized_return * 100


# Example usage
investment_amount_example = 20000  # Example investment amount
start_date_example = "2023-10-11"  # Example start date
current_value_example = 20112.16  # Example current value
end_date_example = "2023-12-14"  # Example end date

# Calculate the annualized return
annualized_return_example = calculate_annualized_return(
    investment_amount_example,
    current_value_example,
    start_date_example,
    # end_date_example,
)
print(annualized_return_example)
