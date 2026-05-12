from metavision_core.event_io.raw_reader import RawReader
import numpy as np
import pandas as pd

raw_stream = RawReader(r'C:\Users\Mor Loya\Documents\metavision\recordings\recording_2026-05-06_11-24-12.raw')

all_events = []
while not raw_stream.is_done():
    events = raw_stream.load_n_events(1_000_000)  # Load 1 million events at a time
    # events is a numpy array with fields: x, y, p (polarity), t (timestamp)
    arr = np.vstack((events['x'], events['y'], events['t'], events['p'])).T
    all_events.append(arr)
    # print(events['x'], events['y'], events['t'], events['p'])

event_table = pd.DataFrame(np.vstack(all_events), columns=['x', 'y', 't', 'p'])
event_table[:1000].to_excel('events.xlsx', index=False)  # Save to Excel file
# print(event_table[:1000])