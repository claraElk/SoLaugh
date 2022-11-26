"""Default settings for data processing and analysis.

Do not edit this file directly!

Instead, create a new configuration changing only the settings you need to
alter for your specific analysis.
"""

import importlib
import pathlib
import os
import logging
from typing import Optional, Union, Iterable, List, Tuple, Dict, Callable

import coloredlogs
from numpy.typing import ArrayLike
import matplotlib

import mne
from mne_bids import BIDSPath
import numpy as np

from mne_bids_pipeline._typing import PathLike, ArbitraryContrast, Literal
from mne_bids_pipeline._logging import gen_log_kwargs


###############################################################################
# Config parameters
# -----------------

from src.params import BIDS_PATH, PREPROC_PATH

interactive = True
debug = True

study_name = 'Solaugh'
bids_root = '/run/media/claraek/Clara_Seagate/bids_mne/'
deriv_root = '/run/media/claraek/Clara_Seagate/test_mne_bibs_pipeline/'

subjects = ['02'] #if 'all' include all subjects
sessions = ['recording']

task = 'LaughterActive'
runs = ['07'] 

find_flat_channels_meg = False
find_noisy_channels_meg = False
use_maxwell_filter = False
ch_types = ['mag']
data_type = 'meg'
eog_channels = ['EEG057', 'EEG058']

# ecg_channels = ['EEG059']
mf_cal_fname = None
l_freq = 1.
h_freq = 40.
resample_sfreq = 250

# Artifact correction.
spatial_filter = 'ica'
ica_max_iterations = 500
ica_l_freq = 1.
ica_n_components = 0.99
ica_reject_components = 'auto'

# Epochs => Issue here
epochs_tmin = -0.5
epochs_tmax = 1.0
baseline = (None, 0)

# Conditions / events to consider when epoching
conditions = ['LaughPosed', 'LaughReal']
event_repeated = 'drop'

# Noise estimation
process_empty_room = True
noise_cov = 'emptyroom'

# Decoding
decode = True
contrasts = [('LaughReal', 'LaughPosed')]