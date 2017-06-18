from task1 import _read_df, _add_field_to_df


df = _read_df(open("launchlog.txt"))
print('Suc values are: ', df.Suc.unique())
df = _add_field_to_df(df, 'year')
print('Year values are: ', df.Field.unique())
df = _add_field_to_df(df, 'month')
print('Month values are: ', df.Field.unique())
