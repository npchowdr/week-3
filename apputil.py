from altair.datasets import url
import seaborn as sns
import pandas as pd


DATA_URL = "https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv"


# update/add code below ...
def fibonacci(n):
    """Return the nth Fibonacci number.

    Args:
        n: The index of the Fibonacci number to compute.

    Returns:
        The Fibonacci number at index n.

    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def to_binary(n):
    """Convert a non-negative integer to its binary representation.

    Args:
        n: A non-negative integer.

    Returns:
        The binary string representing the integer n.

    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary


def task_1():
    """Return a list of all column names, in ascending order of missing values, for the Bellevue dataset.

    Args:
        None

    Returns:
        A list of column names sorted by the proportion of missing values in ascending order.
    """
    df_bellevue = pd.read_csv(DATA_URL)

    df_bellevue["gender"] = df_bellevue["gender"].replace(["?", "h", "g"], pd.NA)
    return df_bellevue.isna().mean().sort_values(ascending=True).index.tolist()


def task_2():
    """Return a DataFrame with the total number of admissions for each year in the Bellevue dataset.

    Args:
        None

    Returns:
        A DataFrame with 'year' and 'total_admissions', where 'year' is
        the year of admission and 'total_admissions' is the count of admissions for that year.
    """
    df_bellevue = pd.read_csv(DATA_URL)

    df_year = df_bellevue.groupby("year").size().reset_index(name="total_admissions")
    return df_year

def task_3():
    """Return a DataFrame with the average age for each gender in the Bellevue dataset.

    Args:
        None

    Returns:
        A DataFrame with 'gender' and 'average_age', 
        where 'gender' is the gender of the patient and
        'average_age' is the average age for that gender.
    """
    df_bellevue = pd.read_csv(DATA_URL)

    df_gender = df_bellevue.groupby("gender").age.mean().reset_index()
    return df_gender

def task_4():
    """Return a list of the top 5 most common professions in the Bellevue dataset.

    Args:
        None

    Returns:
        A list of the top 5 most common professions.
    """
    df_bellevue = pd.read_csv(DATA_URL)

    df_profession = df_bellevue.groupby("profession").size().reset_index(name="count")
    df_sorted_profession = df_profession.sort_values(by="count", ascending=False)
    top5 = df_sorted_profession["profession"].head(5).tolist()
    return top5