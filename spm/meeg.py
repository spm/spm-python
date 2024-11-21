from spm.__wrapper__ import Runtime, MatlabClassWrapper


class meeg(MatlabClassWrapper):
    def __init__(self, *args, **kwargs):
        """
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

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        super().__init__()

    def badchannels(self, *args, **kwargs):
        """
          Method for getting/setting bad channels  
            FORMAT res = badchannels(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/badchannels.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("badchannels", self._as_matlab_object(), *args, **kwargs)

    def badsamples(self, *args, **kwargs):
        """
          Returns an array of 0/1 marking bad data based on artefact events and bad flags  
            FORMAT res = badsamples(this, chanind, sampind, trialind)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/badsamples.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("badsamples", self._as_matlab_object(), *args, **kwargs)

    def badtrials(self, *args, **kwargs):
        """
          Method for getting/setting bad trials  
            FORMAT res = badtrials(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/badtrials.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("badtrials", self._as_matlab_object(), *args, **kwargs)

    def blank(self, *args, **kwargs):
        """
          Creates a blank datafile matching in the header in dimensions   
            Will not erase existing datafile it it's there  
            FORMAT this = blank(this)   
              Will create the datafile using fname and path       
            FORMAT this = blank(this, fnamedat)   
              Will create the datafile using the provided name and path  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/blank.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("blank", self._as_matlab_object(), *args, **kwargs)

    def chanlabels(self, *args, **kwargs):
        """
          Method for getting/setting the channel labels  
            FORMAT res = chanlabels(this, ind, label)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/chanlabels.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("chanlabels", self._as_matlab_object(), *args, **kwargs)

    def chantype(self, *args, **kwargs):
        """
          Method for setting/getting channel types  
            FORMAT chantype(this, ind, type)  
              ind - channel index  
              type - type (string: 'EEG', 'MEG', 'LFP' etc.)  
             
            FORMAT chantype(this, ind), chantype(this)  
            Sets channel types to default using Fieldtrip channelselection  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/chantype.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("chantype", self._as_matlab_object(), *args, **kwargs)

    def check(self, *args, **kwargs):
        """
          Method that performs integrity checks of the meeg object  
            and its readiness for particular purposes.  
            FORMAT  this = check(this, option)  
            IN  
            option - 'basic' (default) - just check the essential fields  
                     '3d' - check if suitable for source reconstruction  
                     'dcm'    - check if suitable for DCM  
             
            OUT  
            ok - 1 - OK, 0- failed  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/check.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("check", self._as_matlab_object(), *args, **kwargs)

    def clone(self, *args, **kwargs):
        """
          Creates a copy of the object with a new, empty data file,  
            possibly changing dimensions  
            FORMAT new = clone(this, fnamedat, dim, reset)  
            reset - 0 (default) do not reset channel or trial info unless dimensions  
                     change, 1 - reset channels only, 2 - trials only, 3 both  
            forcefloat - force the new data file to be float (0 by default)  
                     this is to fix an issue with TF analysis of files using int16  
                     for the raw data  
            Note that when fnamedat comes with a path, the cloned meeg object uses  
            it. Otherwise, its path is by definition that of the meeg object to be  
            cloned.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/clone.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("clone", self._as_matlab_object(), *args, **kwargs)

    def conditions(self, *args, **kwargs):
        """
          Method for getting condition labels, over trials  
            FORMAT res = conditions(this, ind, conditionlabels)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/conditions.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("conditions", self._as_matlab_object(), *args, **kwargs)

    def condlist(self, *args, **kwargs):
        """
          Method for getting a list of unique condition labels sorted according to  
            the trial order in the file  
            FORMAT res = condlist(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/condlist.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("condlist", self._as_matlab_object(), *args, **kwargs)

    def coor2D(self, *args, **kwargs):
        """
          x and y coordinates of channels in 2D plane  
            FORMAT coor2D(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/coor2D.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("coor2D", self._as_matlab_object(), *args, **kwargs)

    def copy(self, *args, **kwargs):
        """
          Method for copying a dataset  
            FORMAT res = copy(this, fname)  
             
            fname can be  
            - path\filename -> data copied and renamed  
            - path          -> data copied only  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/copy.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("copy", self._as_matlab_object(), *args, **kwargs)

    def delete(self, *args, **kwargs):
        """
          Delete files of an M/EEG dataset from disk and return unlinked object  
            FORMAT this = delete(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/delete.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("delete", self._as_matlab_object(), *args, **kwargs)

    def display(self, *args, **kwargs):
        """
          Method for displaying information about an meeg object  
            FORMAT display(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/display.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("display", self._as_matlab_object(), *args, **kwargs)

    def end(self, *args, **kwargs):
        """
          Overloaded end function for meeg objects.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/end.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("end", self._as_matlab_object(), *args, **kwargs)

    def events(self, *args, **kwargs):
        """
          Method for getting/setting events per trial  
            FORMAT res = events(this, ind, event)  
              ind = indices of trials  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/events.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("events", self._as_matlab_object(), *args, **kwargs)

    def fiducials(self, *args, **kwargs):
        """
          Method for getting/setting the fiducials field  
            FORMAT res = fiducials(this, fiducials)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fiducials.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fiducials", self._as_matlab_object(), *args, **kwargs)

    def fieldnames(self, *args, **kwargs):
        """
          Returns names of the fields in .other  
            FORMAT res = fieldnames(this)  
             
            An overloaded function...  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fieldnames.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fieldnames", self._as_matlab_object(), *args, **kwargs)

    def fname(self, *args, **kwargs):
        """
          Method for getting/setting file name  
            FORMAT res = fname(this, name)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fname.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fname", self._as_matlab_object(), *args, **kwargs)

    def fnamedat(self, *args, **kwargs):
        """
          Method for getting the name of the data file  
            FORMAT res = fnamedat(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fnamedat.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fnamedat", self._as_matlab_object(), *args, **kwargs)

    def frequencies(self, *args, **kwargs):
        """
          Method for getting/setting frequencies of TF data  
            FORMAT res = frequencies(this, ind, values)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/frequencies.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("frequencies", self._as_matlab_object(), *args, **kwargs)

    def fsample(self, *args, **kwargs):
        """
          Method for getting and setting the sampling rate  
            FORMAT res = fsample(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fsample.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fsample", self._as_matlab_object(), *args, **kwargs)

    def ftraw(self, *args, **kwargs):
        """
          Method for converting meeg object to Fieldtrip raw struct  
            FORMAT raw  =  ftraw(this, chanind, timeind, trialind)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/ftraw.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("ftraw", self._as_matlab_object(), *args, **kwargs)

    def fttimelock(self, *args, **kwargs):
        """
          Method for converting meeg object to Fieldtrip timelock/freq struct  
            FORMAT timelock = fttimelock(this, chanind, timeind, trialind, freqind)  
             
            The method support both time and TF data and outputs different variants  
            of timelock or freq FT struct depending on the dataset type and requested  
            data dimensions.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fttimelock.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fttimelock", self._as_matlab_object(), *args, **kwargs)

    def fullfile(self, *args, **kwargs):
        """
          Returns full path to the meeg mat file  
            FORMAT p = fullfile(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/fullfile.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fullfile", self._as_matlab_object(), *args, **kwargs)

    def getfield(self, *args, **kwargs):
        """
          Returns  fields in .other  
            FORMAT res = getfield(this, varargin)  
             
            An overloaded function...  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/getfield.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("getfield", self._as_matlab_object(), *args, **kwargs)

    def history(self, *args, **kwargs):
        """
          Method for getting or adding to the history of function calls of some  
            M/EEG data  
            FORMAT res = history(this, varargin)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/history.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("history", self._as_matlab_object(), *args, **kwargs)

    def indchannel(self, *args, **kwargs):
        """
          Method for getting channel indices based on channel labels  
            FORMAT  res = indchannel(this, label)  
            this       - MEEG object  
            label      - string or cell array of labels  
             
            res        - vector of channel indices matching labels  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indchannel.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("indchannel", self._as_matlab_object(), *args, **kwargs)

    def indchantype(self, *args, **kwargs):
        """
          Method for getting channel indices based on labels and/or types  
            FORMAT  ind = indchantype(this, types)  
            this       - MEEG object  
            channels   - string or cell array of strings may include  
                        ('ALL', 'EEG', 'MEG', 'ECG', 'EOG' etc.)  
            flag       - 'GOOD' or 'BAD' to include only good or bad channels  
                         respectively (all are selected by default)  
                           
            ind        - vector of channel indices matching labels  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indchantype.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("indchantype", self._as_matlab_object(), *args, **kwargs)

    def indfrequency(self, *args, **kwargs):
        """
          Method for getting the index closest to given frequency  
            FORMAT  res = indfrequency(this, f)  
            this       - MEEG object  
            f          - vector of frequencies (in Hz)  
             
            res        - vector of sample indices matching indices  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indfrequency.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("indfrequency", self._as_matlab_object(), *args, **kwargs)

    def indsample(self, *args, **kwargs):
        """
          Method for getting the sample closest to some time point  
            FORMAT res = indsample(this, t)  
            this       - MEEG object  
            t          - vector of time points in seconds  
             
            res        - vector of sample indices matching time points  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indsample.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("indsample", self._as_matlab_object(), *args, **kwargs)

    def indtrial(self, *args, **kwargs):
        """
          Method for getting trial indices based on condition labels  
            FORMAT res = indtrial(this, label)  
            this       - MEEG object  
            label      - string or cell array of labels, 'GOOD' and 'BAD'  
                         can be added to list of labels to select only  
                         good or bad trials respectively  
            flag       - 'GOOD' or 'BAD' to include only good or bad trials  
                         respectively (all are selected by default)  
             
            res        - vector of trial indices matching condition labels  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/indtrial.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("indtrial", self._as_matlab_object(), *args, **kwargs)

    def isempty(self, *args, **kwargs):
        """
          True if the object is empty   
            FORMAT out = isempty(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/isempty.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("isempty", self._as_matlab_object(), *args, **kwargs)

    def isequal(self, *args, **kwargs):
        """
          Method to check if 2 MEEG objects are the same  
            FORMAT res = isequal(this, that)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/isequal.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("isequal", self._as_matlab_object(), *args, **kwargs)

    def isfield(self, *args, **kwargs):
        """
          Returns true if the string fieldname is the name of a field in the   
            substructure 'other' in the meeg object 'this'.  
            FORMAT res = isfield(this,fieldname)  
             
            An overloaded function...  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/isfield.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("isfield", self._as_matlab_object(), *args, **kwargs)

    def islinked(self, *args, **kwargs):
        """
          True if the object is linked to data file  
            FORMAT out = islinked(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/islinked.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("islinked", self._as_matlab_object(), *args, **kwargs)

    def link(self, *args, **kwargs):
        """
          Links the object to data file (only if exists)  
            FORMAT this = link(this)   
              Will try to find the datafile based on fname and path       
            FORMAT this = link(this, fnamedat)   
              Will find the datafile using the provided name and path  
            FORMAT this = link(this, fnamedat, dtype, slope, offset)  
              Additional parameters for non-float data files  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/link.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("link", self._as_matlab_object(), *args, **kwargs)

    def modality(self, *args, **kwargs):
        """
          Returns data modality   
            FORMAT [res, list] = modality(this, scalp)  
             
            scalp - 1 (default) only look at scalp modalities  
                    0  look at all modalities  
            planar - 1 distinguish between MEG planar and other MEG   
                     0 (default) do not distinguish  
            If more than one modality is found the function returns 'Multimodal'  
            in res and a cell array of modalities in list.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/modality.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("modality", self._as_matlab_object(), *args, **kwargs)

    def montage(self, *args, **kwargs):
        """
          Method for specifying an online montage, or setting one to use  
            FORMAT  
              res = montage(this, 'add', montage)  
                      Adding a montage to the meeg object, see format here under  
             
              res = montage(this, 'action', idx)  
                      Setting, checking, getting or removing a montage in the object,  
                      depending on the action string and index idx of montage.  
            Actions:  
            - add        -> adding a montage to the object  
            - switch     -> switch between montage, 0 being no applied montage   
                            (switch to 0 by default if no index passed)  
            - remove     -> removing montage, one at a time or any list.  
            - getnumber  -> returning the number of montage(s) available  
            - getindex   -> return current montage index  
            - getname    -> returning a list of montage name (by default the current  
                            one if no list is passed)  
            - getmontage -> returning the current or any other montage structure,   
                            depending on list provided (current one by default if   
                            no list passed).  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/montage.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("montage", self._as_matlab_object(), *args, **kwargs)

    def move(self, *args, **kwargs):
        """
          Method for moving or changing name of data file  
            FORMAT res = move(this, fname)  
             
            fname can be  
            - path\filename -> data moved and renamed  
            - path          -> data moved only  
            - filename      -> data renamed only  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/move.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("move", self._as_matlab_object(), *args, **kwargs)

    def nchannels(self, *args, **kwargs):
        """
          returns number of channels  
            FORMAT res = nchannels(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/nchannels.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("nchannels", self._as_matlab_object(), *args, **kwargs)

    def nconditions(self, *args, **kwargs):
        """
          Method for getting the number of unique conditions in the file  
            FORMAT res = nconditions(obj)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/nconditions.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("nconditions", self._as_matlab_object(), *args, **kwargs)

    def nfrequencies(self, *args, **kwargs):
        """
          Method for getting the number of frequencies for TF data  
            FORMAT res = nsamples(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/nfrequencies.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("nfrequencies", self._as_matlab_object(), *args, **kwargs)

    def nsamples(self, *args, **kwargs):
        """
          Method for getting the number of samples per trial  
            FORMAT res = nsamples(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/nsamples.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("nsamples", self._as_matlab_object(), *args, **kwargs)

    def ntrials(self, *args, **kwargs):
        """
          Method for getting the number of trials in the file  
            FORMAT res = ntrials(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/ntrials.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("ntrials", self._as_matlab_object(), *args, **kwargs)

    def path(self, *args, **kwargs):
        """
          Method for getting/setting path  
            FORMAT res = path(this, newpath)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/path.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("path", self._as_matlab_object(), *args, **kwargs)

    def reload(self, *args, **kwargs):
        """
          Reload the file from disk  
            FORMAT this = reload(this)  
             
            Useful to update the object e.g. after running a batch.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/reload.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("reload", self._as_matlab_object(), *args, **kwargs)

    def repl(self, *args, **kwargs):
        """
          Method for getting replication counts, over trials  
            FORMAT res = repl(this, index, nrepl)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/repl.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("repl", self._as_matlab_object(), *args, **kwargs)

    def rmdata(self, *args, **kwargs):
        """
          Deletes the data file and unlinks the header  
            FORMAT this = rmdata(this)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/rmdata.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("rmdata", self._as_matlab_object(), *args, **kwargs)

    def rmfield(self, *args, **kwargs):
        """
          Method for removing an object field  
            FORMAT this = rmfield(this, fields)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/rmfield.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("rmfield", self._as_matlab_object(), *args, **kwargs)

    def save(self, *args, **kwargs):
        """
          Save an meeg object into a file  
            FORMAT this = save(this)  
             
            Converts an meeg object to struct and saves it.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/save.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("save", self._as_matlab_object(), *args, **kwargs)

    def sconfounds(self, *args, **kwargs):
        """
          Method for getting/setting spatial confounds  
            FORMAT res = sconfounds(this, newsconfounds)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/sconfounds.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("sconfounds", self._as_matlab_object(), *args, **kwargs)

    def selectchannels(self, *args, **kwargs):
        """
          Method for getting channel indices based on labels and/or types  
            FORMAT  res = selectchannels(this, label)  
            this       - MEEG object  
            channels   - string or cell array of labels that may also include   
                         'all', or types ('EEG', 'MEG' etc.)  
             
            res        - vector of channel indices matching labels  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/selectchannels.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("selectchannels", self._as_matlab_object(), *args, **kwargs)

    def selectdata(self, *args, **kwargs):
        """
          Selects data using channel labels, time and condition labels as indices  
            FORMAT res = selectdata(D, chanlabel, timeborders, condition)  
                   res = selectdata(D, chanlabel, freqborders, timeborders, condition)  
             
             D - meeg object  
             chanlabel   - channel label, cell array of labels or [] (for all channels)  
             timeborders - [start end] in sec or [] for all times  
             freqborders - [start end] in Hz or [] for all frequencis (for TF datasets only)  
             condition   - condition label, cell array of labels or [] (for all conditions)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/selectdata.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("selectdata", self._as_matlab_object(), *args, **kwargs)

    def sensors(self, *args, **kwargs):
        """
          Sets and gets sensor fields for EEG and MEG  
            returns empty matrix if no sensors are defined.  
            FORMAT res = sensors(this, type, newsens)  
              type - 'EEG' or 'MEG'  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/sensors.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("sensors", self._as_matlab_object(), *args, **kwargs)

    def size(self, *args, **kwargs):
        """
          returns the dimensions of the data matrix  
            FORMAT res = size(this, dim))  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/size.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("size", self._as_matlab_object(), *args, **kwargs)

    def subsasgn(self, *args, **kwargs):
        """
          Overloaded subsasgn function for meeg objects.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/subsasgn.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsref(self, *args, **kwargs):
        """
          SUBSREF Subscripted reference  
            An overloaded function...  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/subsref.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

    def time(self, *args, **kwargs):
        """
          Method for getting the time axis  
            FORMAT res = time(this, ind, format)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/time.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("time", self._as_matlab_object(), *args, **kwargs)

    def timeonset(self, *args, **kwargs):
        """
          Method for reading and setting the time onset  
            FORMAT res = timeonset(this)  
                   res = timeonset(this, newonset)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/timeonset.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("timeonset", self._as_matlab_object(), *args, **kwargs)

    def transformtype(self, *args, **kwargs):
        """
          Method for getting/setting type of transform  
            FORMAT res = transformtype(this, name)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/transformtype.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("transformtype", self._as_matlab_object(), *args, **kwargs)

    def trialonset(self, *args, **kwargs):
        """
          Method for getting/setting trial onset times  
            FORMAT res = trialonset(this, ind, onset)  
              ind = indices of trials  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/trialonset.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("trialonset", self._as_matlab_object(), *args, **kwargs)

    def trialtag(self, *args, **kwargs):
        """
          Method for getting/setting trial tag  
            FORMAT res = trialtag(this, ind, tag)  
              ind = indices of trials  
            The user can put any data here that will be attached to  
            the respective trial. This is useful e.g. to make sure the  
            relation between regressors and data is not broken when  
            removing bad trials or merging files.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/trialtag.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("trialtag", self._as_matlab_object(), *args, **kwargs)

    def type(self, *args, **kwargs):
        """
          Method for and getting/setting EEG file type  
            FORMAT res = type(this, value)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/type.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("type", self._as_matlab_object(), *args, **kwargs)

    def units(self, *args, **kwargs):
        """
          Method for setting/getting all units, over channels  
            FORMAT res = units(this, ind)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/units.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("units", self._as_matlab_object(), *args, **kwargs)

    def unlink(self, *args, **kwargs):
        """
          Unlinks the object from the data file   
            FORMAT this = unlink(this)     
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/unlink.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("unlink", self._as_matlab_object(), *args, **kwargs)

    def _checkmeeg(self, *args, **kwargs):
        """
          Check the internal structure of meeg objects  
            FORMAT this = checkmeeg(this)  
            this  - the struct to check (is returned modified if necessary)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/private/checkmeeg.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("checkmeeg", self._as_matlab_object(), *args, **kwargs)

    def _fixpnt(self, *args, **kwargs):
        """
          Rename point structure fields (backward compatibility)  
            FORMAT data = fixpnt(data, recurse)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/private/fixpnt.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fixpnt", self._as_matlab_object(), *args, **kwargs)

    def _getset(self, *args, **kwargs):
        """
          Generic method for getting and setting multiple fields of meeg struct  
            FORMAT res = getset(this, parent, fieldname, ind, values)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/private/getset.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("getset", self._as_matlab_object(), *args, **kwargs)

    def _match_str(self, *args, **kwargs):
        """
          MATCH_STR looks for matching labels in two lists of strings  
            and returns the indices into both the 1st and 2nd list of the matches.  
            They will be ordered according to the first input argument.  
             
            Use as  
              [sel1, sel2] = match_str(strlist1, strlist2)  
             
            The strings can be stored as a char matrix or as an vertical array of  
            cells, the matching is done for each row.  
             
            When including a 1 as the third input argument, the output lists of  
            indices will be expanded to the size of the largest input argument.  
            Entries that occur only in one of the two inputs will correspond to a 0  
            in the output, in this case. This can be convenient in rare cases if the  
            size of the input lists is meaningful.  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/private/match_str.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("match_str", self._as_matlab_object(), *args, **kwargs)

    def _warning_flexible(self, *args, **kwargs):
        """
          Function allowing to have better control over the warnings  
            that might not be necessary at some point  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@meeg/private/warning_flexible.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("warning_flexible", self._as_matlab_object(), *args, **kwargs, nargout=0)
