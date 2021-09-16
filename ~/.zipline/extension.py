import pandas as pd
from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

start_session = pd.Timestamp('2018-1-1', tz='utc')
end_session = pd.Timestamp('2021-8-24', tz='utc')



register(
    'crypto-bundle',   # What to call the new bundle
    csvdir_equities(
        ['daily'], csvs),
         # Are these daily or minute bars
        #'\data\csvs',  # Directory where the formatted bar data is
    
    calendar_name='NYSE', # US equities default
    start_session=start_session,
    end_session=end_session
)


"""
Some commandline reference code on ingesting and cleaning up data bundles
zipline bundles
zipline clean -b custom-csvdir-bundle --keep-last 1
zipline clean -b custom-csvdir-bundle --after 2020-10-1
zipline ingest -b test-csvdir
"""
