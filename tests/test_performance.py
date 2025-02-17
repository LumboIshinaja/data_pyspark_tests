import pytest
from utils.data_validators import measure_execution_time

AGGREGATION_QUERY_MAX_TIME = 3.0  # in seconds
FILTER_QUERY_MAX_TIME = 3.0 
JOIN_QUERY_MAX_TIME = 3.0
SORT_QUERY_MAX_TIME = 3.0

@pytest.mark.performance
def test_aggregation_execution_time(sales_data_df):
    """Test if aggregation query executes within acceptable time limit."""

    execution_time, result = measure_execution_time(
        lambda: sales_data_df.groupBy("country").sum("total").collect()
    )

    assert execution_time <= AGGREGATION_QUERY_MAX_TIME, (
        f"Aggregation query took {execution_time:.2f}s, exceeding {AGGREGATION_QUERY_MAX_TIME}s"
    )

@pytest.mark.performance
def test_filter_execution_time(sales_data_df):
    """Test if filtering query executes within acceptable time limit."""
    execution_time, result = measure_execution_time(
        lambda: sales_data_df.filter(sales_data_df["country"] == "USA").collect()
    )

    assert execution_time <= FILTER_QUERY_MAX_TIME, (
        f"Filter query took {execution_time:.2f}s, exceeding {FILTER_QUERY_MAX_TIME}s"
    )

@pytest.mark.performance
def test_join_execution_time(sales_data_df, customers_data_df):
    """Test if join query executes within acceptable time limit."""
    execution_time, result = measure_execution_time(
        lambda: sales_data_df.join(customers_data_df, "customer_id").collect()
    )

    assert execution_time <= JOIN_QUERY_MAX_TIME, (
        f"Join query took {execution_time:.2f}s, exceeding {JOIN_QUERY_MAX_TIME}s"
    )

@pytest.mark.performance
def test_sort_execution_time(sales_data_df):
    """Test if sorting query executes within acceptable time limit."""
    execution_time, result = measure_execution_time(
        lambda: sales_data_df.orderBy("purchase_date").collect()
    )

    assert execution_time <= SORT_QUERY_MAX_TIME, (
        f"Sort query took {execution_time:.2f}s, exceeding {SORT_QUERY_MAX_TIME}s"
    )
