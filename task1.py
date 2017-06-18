import pandas as pd


def _read_df(stream):
    with stream as f:
        _, second_line = f.readline(), f.readline()
        f.seek(0)
        column_indexes = [i for i, ch in enumerate(second_line) if ch == '#']
        column_ranges = list(zip(column_indexes, column_indexes[1:]))
        df = pd.read_fwf(f, colspecs=column_ranges, skiprows=[1])  # read data to dataframe
    df = df.fillna(method='ffill')
    # fill empty fields with previous raw values
    # (some fields are empty but they should have the same value as previous ones)
    return df


def _add_field_to_df(df, field):
    date_time_indexes = {'year': slice(0, 4), 'month': slice(5, 8)}
    try:
        df['Field'] = df['Launch Date (UTC)'].str[date_time_indexes[field]]
    except KeyError:
        raise ValueError('Invalid value of field parameter')

    return df


def group_by(stream, field, success=None):
    """
    Parse stream object, aggregate count by field, filter if launch succeeded (or
    not) and return dict of aggregations.

    :param file stream: file-like object open for reading
    :param str field: specifies field, possible values are: 'year' or 'month'
    :param bool success: filters if launch succeeded, possible values are: True, False or None (default=None).

    :rtype: dict
    :return: dictionary of aggregated counts by field with format {FIELD: int}
    """

    df = _read_df(stream)
    df = _add_field_to_df(df, field)

    if success is not None:
        suc_values = {True: 'S', False: 'F'}  # success values in column 'Suc'
        df = df[df.Suc == suc_values[success]]
    return df.groupby('Field').size().to_dict()  # return aggregated counts by field
