### 0. Importing SPM Python


```python
import spm
import numpy as np
```

### 1. Getting help on a function

To get help on a function or class, you can use the help function as you would in Matlab. For instance, 


```python
help(spm.spm_dcm_erp)
```

    Help on function spm_dcm_erp in module spm.__toolbox.__dcm_meeg.spm_dcm_erp:
    
    spm_dcm_erp(*args, **kwargs)
          Estimate parameters of a DCM model (Variational Lapalce)
            FORMAT [DCM,dipfit] = spm_dcm_erp(DCM)
    
            DCM
               name: name string
                  Lpos:  Source locations
                  xY:    data   [1x1 struct]
                  xU:    design [1x1 struct]
    
              Sname: cell of source name strings
                  A: {[nr x nr double]  [nr x nr double]  [nr x nr double]}
                  B: {[nr x nr double], ...}   Connection constraints
                  C: [nr x 1 double]
    
              options.trials       - indices of trials
              options.Tdcm         - [start end] time window in ms
              options.D            - time bin decimation       (usually 1 or 2)
              options.h            - number of DCT drift terms (usually 1 or 2)
              options.Nmodes       - number of spatial models to invert
              options.analysis     - 'ERP', 'SSR' or 'IND'
              options.model        - 'ERP', 'SEP', 'CMC', 'CMM', 'NMM' or 'MFM'
              options.spatial      - 'ECD', 'LFP' or 'IMG'
              options.onset        - stimulus onset (ms)
              options.dur          - and dispersion (sd)
              options.CVA          - use CVA for spatial modes [default = 0]
              options.Nmax         - maxiumum number of iterations [default = 64]
    
            dipfit - Dipole structure (for electromagnetic forward model)
                   See spm_dcm_erp_dipfit:  this field is removed from DCM.M to save
                   memory - and is offered as an output argument if needed
    
            The scheme can be initialised with parameters for the neuronal model
            and spatial (observer) model by specifying the fields DCM.P and DCM.Q,
            respectively. If previous priors (DCM.M.pE and pC or DCM.M.gE and gC or
            DCM.M.hE and hC) are specified, they will be used. Explicit priors can be
            useful for Bayesian parameter averaging - but would not normally be
            called upon - because prior constraints are specified by DCM.A, DCM.B,...
           __________________________________________________________________________
    
    
        [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_erp.m )
    
        Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    


It also works for classes, either to get more info on the class itself...


```python
help(spm.meeg)
```

    Help on class meeg in module spm.meeg:
    
    class meeg(mpython.matlab_class.MatlabClass)
     |  meeg(*args, **kwargs)
     |
     |  Method resolution order:
     |      meeg
     |      mpython.matlab_class.MatlabClass
     |      mpython.core.base_types.MatlabType
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __call__ = __call(self, *index) from mpython.matlab_class.MatlabClass
     |
     |  __getitem__ = __getitem(self, ind) from mpython.matlab_class.MatlabClass
     |
     |  __init__(self, *args, **kwargs)
     |        Function for creating meeg objects.
     |          FORMAT
     |                  D = meeg;
     |                      returns an empty object
     |                  D = meeg(D);
     |                      converts a D struct to object or does nothing if already
     |                      object
     |                  D = meeg(nchannels, nsamples, ntrials)
     |                      return a time dataset with default settings
     |                  D = meeg(nchannels, nfrequencies, nsamples, ntrials)
     |                      return TF time dataset with default settings
     |
     |          SPM MEEG format consists of a header object optionally linked to
     |          binary data file. The object is usually saved in the header mat file
     |
     |          The header file will contain a struct called D. All
     |          information other than data is contained in this struct and access to the
     |          data is via methods of the object. Also, arbitrary data can be stored
     |          inside the object if their field names do not conflict with existing
     |          methods' names.
     |
     |          The following is a description of the internal implementation of meeg.
     |
     |          Fields of meeg:
     |          .type - type of data in the file: 'continuous', 'single', 'evoked'
     |          .Fsample - sampling rate
     |
     |          .data - file_array object linking to the data or empty if unlinked
     |
     |
     |          .Nsamples - length of the trial (whole data if the file is continuous).
     |          .timeOnset - the peri-stimulus time of the first sample in the trial (in sec)
     |
     |          .fname, .path - strings added by spm_eeg_load to keep track of where a
     |                          header struct was loaded from.
     |
     |          .trials - this describes the segments of the epoched file and is also a
     |                    structure array.
     |
     |            Subfields of .trials
     |
     |                .label - user-specified string for the condition
     |                .onset - time of the first sample in seconds in terms of the
     |                         original file
     |                .bad - 0 or 1 flag to allow rejection of trials.
     |                .repl - for epochs that are averages - number of replications used
     |                        for the average.
     |                .tag  - the user can put any data here that will be attached to
     |                        the respective trial. This is useful e.g. to make sure the
     |                        relation between regressors and data is not broken when
     |                        removing bad trials or merging files.
     |                .events - this is a structure array describing events related to
     |                          each trial.
     |
     |                    Subfields of .events
     |
     |                    .type - string (e.g. 'front panel trigger')
     |                    .value - number or string, can be empty (e.g. 'Trig 1').
     |                    .time - in seconds in terms of the original file
     |                    .duration - in seconds
     |
     |          .channels - This is a structure array which is a field of meeg.
     |                      length(channels) should equal size(.data.y, 1) and the order
     |                      must correspond to the order of channels in the data.
     |
     |            Subfields of .channels
     |
     |                .label - channel label which is always a string
     |                .type - a string, possible values - 'MEG', 'EEG', 'VEOG', 'HEOG',
     |                        'EMG' ,'LFP' etc.
     |                .units - units of the data in the channel.
     |                .bad - 0 or 1 flag to mark channels as bad.
     |                .X_plot2D, .Y_plot2D - positions on 2D plane (formerly in ctf). NaN
     |                                       for channels that should not be plotted.
     |
     |          .sensors
     |
     |
     |            Subfields of .sensors (optional)
     |                .meg - struct with sensor positions for MEG (subfields: .pnt .ori .tra .label)
     |                .eeg - struct with sensor positions for MEG (subfields: .pnt .tra .label)
     |
     |          .fiducials - headshape and fiducials for coregistration with sMRI
     |
     |            Subfiels of .fiducials (optional)
     |                .pnt - headshape points
     |                .fid.pnt - fiducial points
     |                .fid.label - fiducial labels
     |
     |          .transform - additional information for transformed (most commonly time-frequency) data
     |             Subfields of .transform
     |                 .ID - 'time', 'TF', or 'TFphase'
     |                 .frequencies (optional)
     |
     |          .history - structure array describing commands that modified the file.
     |
     |            Subfields of .history:
     |
     |                .function - string, the function name
     |                .arguments - cell array, the function arguments
     |                .time - when function call was made
     |
     |          .other - structure used to store other information bits, not fitting the
     |                   object structure at the moment,
     |                for example:
     |                .inv - structure array corresponding to the forw/inv problem in MEEG.
     |                .val - index of the 'inv' solution currently used.
     |
     |          .condlist - cell array of unique condition labels defining the proper
     |                 condition order
     |
     |          .montage - structure used to store info on on-line montage used
     |                .M contains transformation matrix of the montage and names of
     |                    original and new channels (+ new channels definition)
     |                .Mind indicates which montage to use
     |         __________________________________________________________________________
     |
     |            Documentation for meeg
     |               doc meeg
     |
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/meeg.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  __setitem__ = __setitem(self, ind, value) from mpython.matlab_class.MatlabClass
     |
     |  badchannels(self, *args, **kwargs)
     |        Method for getting/setting bad channels
     |          FORMAT res = badchannels(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/badchannels.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  badsamples(self, *args, **kwargs)
     |        Returns an array of 0/1 marking bad data based on artefact events and bad flags
     |          FORMAT res = badsamples(this, chanind, sampind, trialind)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/badsamples.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  badtrials(self, *args, **kwargs)
     |        Method for getting/setting bad trials
     |          FORMAT res = badtrials(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/badtrials.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  blank(self, *args, **kwargs)
     |        Creates a blank datafile matching in the header in dimensions
     |          Will not erase existing datafile it it's there
     |          FORMAT this = blank(this)
     |            Will create the datafile using fname and path
     |          FORMAT this = blank(this, fnamedat)
     |            Will create the datafile using the provided name and path
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/blank.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  chanlabels(self, *args, **kwargs)
     |        Method for getting/setting the channel labels
     |          FORMAT res = chanlabels(this, ind, label)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/chanlabels.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  chantype(self, *args, **kwargs)
     |        Method for setting/getting channel types
     |          FORMAT chantype(this, ind, type)
     |            ind - channel index
     |            type - type (string: 'EEG', 'MEG', 'LFP' etc.)
     |
     |          FORMAT chantype(this, ind), chantype(this)
     |          Sets channel types to default using Fieldtrip channelselection
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/chantype.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  check(self, *args, **kwargs)
     |        Method that performs integrity checks of the meeg object
     |          and its readiness for particular purposes.
     |          FORMAT  this = check(this, option)
     |          IN
     |          option - 'basic' (default) - just check the essential fields
     |                   '3d' - check if suitable for source reconstruction
     |                   'dcm'    - check if suitable for DCM
     |
     |          OUT
     |          ok - 1 - OK, 0- failed
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/check.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  clone(self, *args, **kwargs)
     |        Creates a copy of the object with a new, empty data file,
     |          possibly changing dimensions
     |          FORMAT new = clone(this, fnamedat, dim, reset)
     |          reset - 0 (default) do not reset channel or trial info unless dimensions
     |                   change, 1 - reset channels only, 2 - trials only, 3 both
     |          forcefloat - force the new data file to be float (0 by default)
     |                   this is to fix an issue with TF analysis of files using int16
     |                   for the raw data
     |          Note that when fnamedat comes with a path, the cloned meeg object uses
     |          it. Otherwise, its path is by definition that of the meeg object to be
     |          cloned.
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/clone.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  conditions(self, *args, **kwargs)
     |        Method for getting condition labels, over trials
     |          FORMAT res = conditions(this, ind, conditionlabels)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/conditions.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  condlist(self, *args, **kwargs)
     |        Method for getting a list of unique condition labels sorted according to
     |          the trial order in the file
     |          FORMAT res = condlist(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/condlist.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  coor2D(self, *args, **kwargs)
     |        x and y coordinates of channels in 2D plane
     |          FORMAT coor2D(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/coor2D.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  copy(self, *args, **kwargs)
     |        Method for copying a dataset
     |          FORMAT res = copy(this, fname)
     |
     |          fname can be
     |          - pathilename -> data copied and renamed
     |          - path          -> data copied only
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/copy.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  delete(self, *args, **kwargs)
     |        Delete files of an M/EEG dataset from disk and return unlinked object
     |          FORMAT this = delete(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/delete.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  display(self, *args, **kwargs)
     |        Method for displaying information about an meeg object
     |          FORMAT display(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/display.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  end(self, *args, **kwargs)
     |        Overloaded end function for meeg objects.
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/end.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  events(self, *args, **kwargs)
     |        Method for getting/setting events per trial
     |          FORMAT res = events(this, ind, event)
     |            ind = indices of trials
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/events.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  fiducials(self, *args, **kwargs)
     |        Method for getting/setting the fiducials field
     |          FORMAT res = fiducials(this, fiducials)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fiducials.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  fieldnames(self, *args, **kwargs)
     |        Returns names of the fields in .other
     |          FORMAT res = fieldnames(this)
     |
     |          An overloaded function...
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fieldnames.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  fname(self, *args, **kwargs)
     |        Method for getting/setting file name
     |          FORMAT res = fname(this, name)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fname.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  fnamedat(self, *args, **kwargs)
     |        Method for getting the name of the data file
     |          FORMAT res = fnamedat(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fnamedat.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  frequencies(self, *args, **kwargs)
     |        Method for getting/setting frequencies of TF data
     |          FORMAT res = frequencies(this, ind, values)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/frequencies.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  fsample(self, *args, **kwargs)
     |        Method for getting and setting the sampling rate
     |          FORMAT res = fsample(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fsample.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  ftraw(self, *args, **kwargs)
     |        Method for converting meeg object to Fieldtrip raw struct
     |          FORMAT raw  =  ftraw(this, chanind, timeind, trialind)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/ftraw.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  fttimelock(self, *args, **kwargs)
     |        Method for converting meeg object to Fieldtrip timelock/freq struct
     |          FORMAT timelock = fttimelock(this, chanind, timeind, trialind, freqind)
     |
     |          The method support both time and TF data and outputs different variants
     |          of timelock or freq FT struct depending on the dataset type and requested
     |          data dimensions.
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fttimelock.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  fullfile(self, *args, **kwargs)
     |        Returns full path to the meeg mat file
     |          FORMAT p = fullfile(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fullfile.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  getfield(self, *args, **kwargs)
     |        Returns  fields in .other
     |          FORMAT res = getfield(this, varargin)
     |
     |          An overloaded function...
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/getfield.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  history(self, *args, **kwargs)
     |        Method for getting or adding to the history of function calls of some
     |          M/EEG data
     |          FORMAT res = history(this, varargin)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/history.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  indchannel(self, *args, **kwargs)
     |        Method for getting channel indices based on channel labels
     |          FORMAT  res = indchannel(this, label)
     |          this       - MEEG object
     |          label      - string or cell array of labels
     |
     |          res        - vector of channel indices matching labels
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indchannel.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  indchantype(self, *args, **kwargs)
     |        Method for getting channel indices based on labels and/or types
     |          FORMAT  ind = indchantype(this, types)
     |          this       - MEEG object
     |          channels   - string or cell array of strings may include
     |                      ('ALL', 'EEG', 'MEG', 'ECG', 'EOG' etc.)
     |          flag       - 'GOOD' or 'BAD' to include only good or bad channels
     |                       respectively (all are selected by default)
     |
     |          ind        - vector of channel indices matching labels
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indchantype.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  indfrequency(self, *args, **kwargs)
     |        Method for getting the index closest to given frequency
     |          FORMAT  res = indfrequency(this, f)
     |          this       - MEEG object
     |          f          - vector of frequencies (in Hz)
     |
     |          res        - vector of sample indices matching indices
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indfrequency.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  indsample(self, *args, **kwargs)
     |        Method for getting the sample closest to some time point
     |          FORMAT res = indsample(this, t)
     |          this       - MEEG object
     |          t          - vector of time points in seconds
     |
     |          res        - vector of sample indices matching time points
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indsample.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  indtrial(self, *args, **kwargs)
     |        Method for getting trial indices based on condition labels
     |          FORMAT res = indtrial(this, label)
     |          this       - MEEG object
     |          label      - string or cell array of labels, 'GOOD' and 'BAD'
     |                       can be added to list of labels to select only
     |                       good or bad trials respectively
     |          flag       - 'GOOD' or 'BAD' to include only good or bad trials
     |                       respectively (all are selected by default)
     |
     |          res        - vector of trial indices matching condition labels
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indtrial.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  isempty(self, *args, **kwargs)
     |        True if the object is empty
     |          FORMAT out = isempty(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/isempty.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  isequal(self, *args, **kwargs)
     |        Method to check if 2 MEEG objects are the same
     |          FORMAT res = isequal(this, that)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/isequal.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  isfield(self, *args, **kwargs)
     |        Returns true if the string fieldname is the name of a field in the
     |          substructure 'other' in the meeg object 'this'.
     |          FORMAT res = isfield(this,fieldname)
     |
     |          An overloaded function...
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/isfield.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  islinked(self, *args, **kwargs)
     |        True if the object is linked to data file
     |          FORMAT out = islinked(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/islinked.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  link(self, *args, **kwargs)
     |        Links the object to data file (only if exists)
     |          FORMAT this = link(this)
     |            Will try to find the datafile based on fname and path
     |          FORMAT this = link(this, fnamedat)
     |            Will find the datafile using the provided name and path
     |          FORMAT this = link(this, fnamedat, dtype, slope, offset)
     |            Additional parameters for non-float data files
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/link.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  modality(self, *args, **kwargs)
     |        Returns data modality
     |          FORMAT [res, list] = modality(this, scalp)
     |
     |          scalp - 1 (default) only look at scalp modalities
     |                  0  look at all modalities
     |          planar - 1 distinguish between MEG planar and other MEG
     |                   0 (default) do not distinguish
     |          If more than one modality is found the function returns 'Multimodal'
     |          in res and a cell array of modalities in list.
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/modality.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  montage(self, *args, **kwargs)
     |        Method for specifying an online montage, or setting one to use
     |          FORMAT
     |            res = montage(this, 'add', montage)
     |                    Adding a montage to the meeg object, see format here under
     |
     |            res = montage(this, 'action', idx)
     |                    Setting, checking, getting or removing a montage in the object,
     |                    depending on the action string and index idx of montage.
     |          Actions:
     |          - add        -> adding a montage to the object
     |          - switch     -> switch between montage, 0 being no applied montage
     |                          (switch to 0 by default if no index passed)
     |          - remove     -> removing montage, one at a time or any list.
     |          - getnumber  -> returning the number of montage(s) available
     |          - getindex   -> return current montage index
     |          - getname    -> returning a list of montage name (by default the current
     |                          one if no list is passed)
     |          - getmontage -> returning the current or any other montage structure,
     |                          depending on list provided (current one by default if
     |                          no list passed).
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/montage.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  move(self, *args, **kwargs)
     |        Method for moving or changing name of data file
     |          FORMAT res = move(this, fname)
     |
     |          fname can be
     |          - pathilename -> data moved and renamed
     |          - path          -> data moved only
     |          - filename      -> data renamed only
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/move.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  nchannels(self, *args, **kwargs)
     |        returns number of channels
     |          FORMAT res = nchannels(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/nchannels.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  nconditions(self, *args, **kwargs)
     |        Method for getting the number of unique conditions in the file
     |          FORMAT res = nconditions(obj)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/nconditions.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  nfrequencies(self, *args, **kwargs)
     |        Method for getting the number of frequencies for TF data
     |          FORMAT res = nsamples(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/nfrequencies.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  nsamples(self, *args, **kwargs)
     |        Method for getting the number of samples per trial
     |          FORMAT res = nsamples(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/nsamples.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  ntrials(self, *args, **kwargs)
     |        Method for getting the number of trials in the file
     |          FORMAT res = ntrials(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/ntrials.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  path(self, *args, **kwargs)
     |        Method for getting/setting path
     |          FORMAT res = path(this, newpath)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/path.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  reload(self, *args, **kwargs)
     |        Reload the file from disk
     |          FORMAT this = reload(this)
     |
     |          Useful to update the object e.g. after running a batch.
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/reload.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  repl(self, *args, **kwargs)
     |        Method for getting replication counts, over trials
     |          FORMAT res = repl(this, index, nrepl)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/repl.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  rmdata(self, *args, **kwargs)
     |        Deletes the data file and unlinks the header
     |          FORMAT this = rmdata(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/rmdata.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  rmfield(self, *args, **kwargs)
     |        Method for removing an object field
     |          FORMAT this = rmfield(this, fields)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/rmfield.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  save(self, *args, **kwargs)
     |        Save an meeg object into a file
     |          FORMAT this = save(this)
     |
     |          Converts an meeg object to struct and saves it.
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/save.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  sconfounds(self, *args, **kwargs)
     |        Method for getting/setting spatial confounds
     |          FORMAT res = sconfounds(this, newsconfounds)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/sconfounds.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  selectchannels(self, *args, **kwargs)
     |        Method for getting channel indices based on labels and/or types
     |          FORMAT  res = selectchannels(this, label)
     |          this       - MEEG object
     |          channels   - string or cell array of labels that may also include
     |                       'all', or types ('EEG', 'MEG' etc.)
     |
     |          res        - vector of channel indices matching labels
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/selectchannels.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  selectdata(self, *args, **kwargs)
     |        Selects data using channel labels, time and condition labels as indices
     |          FORMAT res = selectdata(D, chanlabel, timeborders, condition)
     |                 res = selectdata(D, chanlabel, freqborders, timeborders, condition)
     |
     |           D - meeg object
     |           chanlabel   - channel label, cell array of labels or [] (for all channels)
     |           timeborders - [start end] in sec or [] for all times
     |           freqborders - [start end] in Hz or [] for all frequencis (for TF datasets only)
     |           condition   - condition label, cell array of labels or [] (for all conditions)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/selectdata.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  sensors(self, *args, **kwargs)
     |        Sets and gets sensor fields for EEG and MEG
     |          returns empty matrix if no sensors are defined.
     |          FORMAT res = sensors(this, type, newsens)
     |            type - 'EEG' or 'MEG'
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/sensors.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  size(self, *args, **kwargs)
     |        returns the dimensions of the data matrix
     |          FORMAT res = size(this, dim))
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/size.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  subsasgn(self, *args, **kwargs)
     |        Overloaded subsasgn function for meeg objects.
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/subsasgn.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  subsref(self, *args, **kwargs)
     |        SUBSREF Subscripted reference
     |          An overloaded function...
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/subsref.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  time(self, *args, **kwargs)
     |        Method for getting the time axis
     |          FORMAT res = time(this, ind, format)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/time.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  timeonset(self, *args, **kwargs)
     |        Method for reading and setting the time onset
     |          FORMAT res = timeonset(this)
     |                 res = timeonset(this, newonset)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/timeonset.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  transformtype(self, *args, **kwargs)
     |        Method for getting/setting type of transform
     |          FORMAT res = transformtype(this, name)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/transformtype.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  trialonset(self, *args, **kwargs)
     |        Method for getting/setting trial onset times
     |          FORMAT res = trialonset(this, ind, onset)
     |            ind = indices of trials
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/trialonset.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  trialtag(self, *args, **kwargs)
     |        Method for getting/setting trial tag
     |          FORMAT res = trialtag(this, ind, tag)
     |            ind = indices of trials
     |          The user can put any data here that will be attached to
     |          the respective trial. This is useful e.g. to make sure the
     |          relation between regressors and data is not broken when
     |          removing bad trials or merging files.
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/trialtag.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  type_(self, *args, **kwargs)
     |        Method for and getting/setting EEG file type
     |          FORMAT res = type(this, value)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/type.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  units(self, *args, **kwargs)
     |        Method for setting/getting all units, over channels
     |          FORMAT res = units(this, ind)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/units.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  unlink(self, *args, **kwargs)
     |        Unlinks the object from the data file
     |          FORMAT this = unlink(this)
     |         __________________________________________________________________________
     |
     |
     |      [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/unlink.m )
     |
     |      Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from mpython.matlab_class.MatlabClass:
     |
     |  __init_subclass__()
     |      This method is called when a class is subclassed.
     |
     |      The default implementation does nothing. It may be
     |      overridden to extend subclasses.
     |
     |  from_any(other)
     |      Convert python/matlab objects to `MatlabType` objects
     |      (`Cell`, `Struct`, `Array`, `MatlabClass`).
     |
     |      !!! warning "Conversion is performed in-place when possible."
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from mpython.matlab_class.MatlabClass:
     |
     |  __new__(cls, *args, _objdict=None, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from mpython.core.base_types.MatlabType:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
    


... or learn how to construct an object from it:


```python
help(spm.meeg.__init__)
```

    Help on function __init__ in module spm.meeg:
    
    __init__(self, *args, **kwargs)
          Function for creating meeg objects.
            FORMAT
                    D = meeg;
                        returns an empty object
                    D = meeg(D);
                        converts a D struct to object or does nothing if already
                        object
                    D = meeg(nchannels, nsamples, ntrials)
                        return a time dataset with default settings
                    D = meeg(nchannels, nfrequencies, nsamples, ntrials)
                        return TF time dataset with default settings
    
            SPM MEEG format consists of a header object optionally linked to
            binary data file. The object is usually saved in the header mat file
    
            The header file will contain a struct called D. All
            information other than data is contained in this struct and access to the
            data is via methods of the object. Also, arbitrary data can be stored
            inside the object if their field names do not conflict with existing
            methods' names.
    
            The following is a description of the internal implementation of meeg.
    
            Fields of meeg:
            .type - type of data in the file: 'continuous', 'single', 'evoked'
            .Fsample - sampling rate
    
            .data - file_array object linking to the data or empty if unlinked
    
    
            .Nsamples - length of the trial (whole data if the file is continuous).
            .timeOnset - the peri-stimulus time of the first sample in the trial (in sec)
    
            .fname, .path - strings added by spm_eeg_load to keep track of where a
                            header struct was loaded from.
    
            .trials - this describes the segments of the epoched file and is also a
                      structure array.
    
              Subfields of .trials
    
                  .label - user-specified string for the condition
                  .onset - time of the first sample in seconds in terms of the
                           original file
                  .bad - 0 or 1 flag to allow rejection of trials.
                  .repl - for epochs that are averages - number of replications used
                          for the average.
                  .tag  - the user can put any data here that will be attached to
                          the respective trial. This is useful e.g. to make sure the
                          relation between regressors and data is not broken when
                          removing bad trials or merging files.
                  .events - this is a structure array describing events related to
                            each trial.
    
                      Subfields of .events
    
                      .type - string (e.g. 'front panel trigger')
                      .value - number or string, can be empty (e.g. 'Trig 1').
                      .time - in seconds in terms of the original file
                      .duration - in seconds
    
            .channels - This is a structure array which is a field of meeg.
                        length(channels) should equal size(.data.y, 1) and the order
                        must correspond to the order of channels in the data.
    
              Subfields of .channels
    
                  .label - channel label which is always a string
                  .type - a string, possible values - 'MEG', 'EEG', 'VEOG', 'HEOG',
                          'EMG' ,'LFP' etc.
                  .units - units of the data in the channel.
                  .bad - 0 or 1 flag to mark channels as bad.
                  .X_plot2D, .Y_plot2D - positions on 2D plane (formerly in ctf). NaN
                                         for channels that should not be plotted.
    
            .sensors
    
    
              Subfields of .sensors (optional)
                  .meg - struct with sensor positions for MEG (subfields: .pnt .ori .tra .label)
                  .eeg - struct with sensor positions for MEG (subfields: .pnt .tra .label)
    
            .fiducials - headshape and fiducials for coregistration with sMRI
    
              Subfiels of .fiducials (optional)
                  .pnt - headshape points
                  .fid.pnt - fiducial points
                  .fid.label - fiducial labels
    
            .transform - additional information for transformed (most commonly time-frequency) data
               Subfields of .transform
                   .ID - 'time', 'TF', or 'TFphase'
                   .frequencies (optional)
    
            .history - structure array describing commands that modified the file.
    
              Subfields of .history:
    
                  .function - string, the function name
                  .arguments - cell array, the function arguments
                  .time - when function call was made
    
            .other - structure used to store other information bits, not fitting the
                     object structure at the moment,
                  for example:
                  .inv - structure array corresponding to the forw/inv problem in MEEG.
                  .val - index of the 'inv' solution currently used.
    
            .condlist - cell array of unique condition labels defining the proper
                   condition order
    
            .montage - structure used to store info on on-line montage used
                  .M contains transformation matrix of the montage and names of
                      original and new channels (+ new channels definition)
                  .Mind indicates which montage to use
           __________________________________________________________________________
    
              Documentation for meeg
                 doc meeg
    
    
    
        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/meeg.m )
    
        Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    


### 2. Using Matlab-like types

SPM Python provides you with a type system that allows to reuse Matlab syntax without too much worries. The following classes are available:
 1. `spm.Cell`, for cell arrays
 2. `spm.Struct`, for struct arrays
 3. `spm.Array`, for general arrays


#### 2.1. Base types

We've got cell arrays:


```python
# Create an empty 1D Cell array with a shape of (3,)
c = spm.Cell(3)

# Populate the Cell array with data
c[0] = "Hello"
c[1] = "World"
c[2] = 42

# Print the Cell array
print("Initial Cell array:", c.tolist())

# Add a new element in (undefined) index 4
c[4] = "New Element"

# Print the updated Cell array
print("Updated Cell array:", c.tolist())
```

    Initial Cell array: ['Hello', 'World', 42]
    Updated Cell array: ['Hello', 'World', 42, Array([]), 'New Element']


Some struct arrays as well:


```python
# Create an empty Struct
example_struct = spm.Struct()
example_struct.name = "Example"
example_struct.value = 42
print("Single Struct example:", example_struct)

# Create a 1D Struct array
struct_array_1d = spm.Struct(3)
struct_array_1d[0].name = "First"
struct_array_1d[1].name = "Second"
struct_array_1d[2].name = "Third"
print("1D Struct array example:", struct_array_1d)

# Create a 2D Struct array
struct_array_2d = spm.Struct(2, 2)
struct_array_2d[0, 0].name = "Top Left"
struct_array_2d[0, 1].name = "Top Right"
struct_array_2d[1, 0].name = "Bottom Left"
struct_array_2d[1, 1].name = "Bottom Right"
print("2D Struct array example:")
print(struct_array_2d)

# Add a new field to the Struct
example_struct.new_field = "New Field Value"
print("Updated Struct with new field:", example_struct)
```

    Single Struct example: {'name': 'Example', 'value': 42}
    1D Struct array example: [{'name': 'First'}, {'name': 'Second'}, {'name': 'Third'}]
    2D Struct array example:
    [[{'name': 'Top Left'}, {'name': 'Top Right'}],
     [{'name': 'Bottom Left'}, {'name': 'Bottom Right'}]]
    Updated Struct with new field: {'name': 'Example', 'value': 42, 'new_field': 'New Field Value'}


And some generic arrays too:


```python
# Create an empty array (scalar)
a = spm.Array()
print("Empty array:", a, "Shape:", a.shape)

# Create a 1D array of length 3
a1d = spm.Array(3)
print("1D array:", a1d)

# Create a 2D array (3 rows, 2 columns)
a2d = spm.Array(3, 2)
print("2D array:\n", a2d)
```

    Empty array: 0.0 Shape: ()
    1D array: [0.0, 0.0, 0.0]
    2D array:
     [[0.0, 0.0],
     [0.0, 0.0],
     [0.0, 0.0]]


#### 2.2. Array operations

All of these types are derived from `np.ndarray` (thank you, Yael), which makes them really nice to work with if you're confortable with Numpy. 


```python
# Create a 1D struct array
s = spm.Struct(4)

# Populate the struct array with data
for i in range(4):
    s[i].value = i
    s[i].label = f"item{i}"

print("Original Struct:", s)

# Reshape the struct array to 2x2
s_reshaped = s.reshape((2, 2))
print("Reshaped Struct (2x2):\n", s_reshaped)

# Transpose the struct array
s_transposed = np.transpose(s_reshaped)
```

    Original Struct: [{'value': 0, 'label': 'item0'}, {'value': 1, 'label': 'item1'},
     {'value': 2, 'label': 'item2'}, {'value': 3, 'label': 'item3'}]
    Reshaped Struct (2x2):
     [[{'value': 0, 'label': 'item0'}, {'value': 1, 'label': 'item1'}],
     [{'value': 2, 'label': 'item2'}, {'value': 3, 'label': 'item3'}]]
    Concatenated Struct (1D): [{'value': 0, 'label': 'item0'} {'value': 1, 'label': 'item1'}
     {'value': 2, 'label': 'item2'} {'value': 3, 'label': 'item3'}
     {'value': 10, 'label': 'item10'} {'value': 11, 'label': 'item11'}
     {'value': 12, 'label': 'item12'} {'value': 13, 'label': 'item13'}]



```python
# Concatenate along the first axis
s2 = spm.Struct(4)
for i in range(4):
    s2[i].value = i + 10
    s2[i].label = f"item{i + 10}"

s_concat = np.concatenate([s, s2])
print("Concatenated Struct (1D):", s_concat)
```

    Concatenated Struct (1D): [{'value': 0, 'label': 'item0'} {'value': 1, 'label': 'item1'}
     {'value': 2, 'label': 'item2'} {'value': 3, 'label': 'item3'}
     {'value': 10, 'label': 'item10'} {'value': 11, 'label': 'item11'}
     {'value': 12, 'label': 'item12'} {'value': 13, 'label': 'item13'}]



```python
# Concatenate along the first axis
s2 = spm.Struct(4)
for i in range(4):
    s2[i].value = i + 10
    s2[i].label = f"item{i+10}"

s_concat = np.concatenate([s, s2])
print("Concatenated Struct (1D):", s_concat)
```


```python
# Create a 1D Cell array
c = spm.Cell(4)
c[:] = ["hello", 123, {"a": 1}, [1, 2, 3]]

print("Original Cell:", c)

# Create a 1D Cell array
c_extra = spm.Cell(2)
c_extra[:] = ["more", "cells"]

# Concatenate the Cell arrays
c_concat = np.concatenate([c, c_extra])
print("Concatenated Cell (1D):", c_concat.tolist())
```

    Original Cell: [hello, 123, [a], [1, 2, 3]]
    Concatenated Cell (1D): ['hello', 123, Cell(['a']), Cell([1, 2, 3]), 'more', 'cells']


#### 2.3. Type inference

One of the nice feature these types have is type inference at construction time. This enables accessing undefined field of an array, as long as the indexing sequence ends up with an assignment. There are a few extra rules:
 1. `.`: Use dot indexing to create a new field, as you'd use `.` in Matlab,
 2. `[]`: Use square brackets for array indexing, as you'd use `()` in Matlab,
 3. `()`: Use round brackets for cell indexing, as you'd use `{}` in Matlab,

 For example, to create a struct array with a field containing a cell array with, in third position, a struct array with a 2-by-2 random matrix in fifth position (showcasing all three rules):


```python
S = spm.Struct()
S.field(3).struct[5].elem = np.random.rand(2, 2)
S
```




    {'field': Cell([Array([]), Array([]), Array([]),
          {'struct': Struct([{'elem': Array([])}, {'elem': Array([])}, {'elem': Array([])},
                  {'elem': Array([])}, {'elem': Array([])},
                  {'elem': Array([[0.38339607, 0.55686198],
                         [0.53678757, 0.5828017 ]])}       ])}                             ])}



There is one caveat though: elements of unfinalised cell arrays cannot be specified:
```python
>>> S = spm.Struct()
>>> S.field(3) = 'test'
 S.field(3) = 'test'
    ^
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
```

This is why we need one additional rule: 

 4. `as_cell[]`: Initialising an element of an unfinalised cell array needs to use `as_cell`. 

Using `as_cell` solves exactly this problem:


```python
S = spm.Struct()
S.field.as_cell[3] = "test"
S
```




    {'field': Cell([Array([]), Array([]), Array([]), 'test'])}


