from spm.__wrapper__ import Runtime


def spm_eeg_convert(*args, **kwargs):
    """
      Convert various M/EEG formats to SPM12 format  
        FORMAT D = spm_eeg_convert(S)  
        S                - string (filename) or struct (see below)  
         
        If S is a struct it can have the optional following fields:  
        S.dataset        - file name  
        S.mode           - 'header'     - only convert the header without reading data  
                           'continuous' - convert data as continuous  
                           'epoched'    - convert data as epoched (requires data that is  
                                          already epoched or a trial definition in S.trl).  
        S.timewin        - for continuous mode [start end] of data segment in sec (all if empty)  
                         - for epoched mode time window in PST ms  
        S.outfile        - output file name (default 'spmeeg_' + input)  
        S.channels       - 'all' - convert all channels  
                           or cell array of labels  
        For epoched mode:  
         
        S.trl            - [N x 3] trl matrix or name of the trial definition file  
                           containing 'trl' variable with such a matrix  
        S.conditionlabels- labels for the trials in the data [default: 'Undefined']  
         
          or  
         
        S.trialdef       - structure array for trial definition with fields  
            S.trialdef.conditionlabel - string label for the condition  
            S.trialdef.eventtype      - string  
            S.trialdef.eventvalue     - string, numeric or empty  
         
         
        S.inputformat    - data type (optional) to force the use of specific data  
                           reader  
        S.chanindx       - list of channels to read in the case of different   
                           sampling frequencies (EDF only)  
        S.eventpadding   - the additional time period around each trial for which  
                           the events are saved with the trial (to let the user  
                           keep and use for analysis events which are outside  
                           trial borders), in seconds. [default: 0]  
        S.blocksize      - size of blocks used internally to split large files  
                           [default: ~100Mb]  
        S.checkboundary  - 1 - check if there are breaks in the file and do not  
                               read across those breaks [default]  
                           0 - ignore breaks (not recommended).  
        S.saveorigheader - 1 - save original data header with the dataset  
                           0 - do not keep the original header [default]  
         
        % D              - MEEG object (also written on disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_convert.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_convert", *args, **kwargs)
