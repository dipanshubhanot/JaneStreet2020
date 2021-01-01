import math
import pandas as pd


def score_day(trades: pd.DataFrame):
    """

    Scores the trades for a day

    Args:
        trades (pd.DataFrame): A pandas data frame object which contains the columns weight, resp and action
    """
    day_sum = 0

    for index, row in trades.iterrows():
        day_sum += row['weight']*row['resp']*row['action']

    return day_sum


def score_func(trades: pd.DataFrame):
    """ Gets the evaulation score, according to competition specifications

    Args:
        trades (pd.DataFrame): Table contianing information about the trades
    """

    # Get all the unique dates
    dates = trades['date'].unique()
    p_i_sum = 0
    p_i_sq_sum = 0

    date_sum = dict()
    for date in dates:
        date_sum[date] = score_day(trades[trades['date'] == date])

    for date, val in date_sum.items():
        p_i_sum += val
        p_i_sq_sum += (val*val)

    t = (p_i_sum/math.sqrt(p_i_sq_sum)) * math.sqrt((250/len(dates)))

    u = min(max(t, 0), 6) * p_i_sum

    return u
