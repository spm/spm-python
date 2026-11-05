from spm._runtime import Runtime


def fiff_write_dig_file(*args, **kwargs):
    r"""
       
        function fiff_write_dig_file(filename,lpa,nas,rpa,hpi,eeg,eegref,extra)  
         
        Create a fif file containing the Polhemus data  
         
        filename      Output file name  
         
        The following need to be specified in the Neuromag MEG  
        coordinate system in meters  
         
        lpa           Left auricular point  
        nas           Nasion  
        rpa           Right auricular point  
        hpi           HPI coil locations               (optional)  
        eeg           EEG electrode locations          (optional)  
        eegref        EEG reference electrode location (optional)  
        extra         Additional head surface points   (optional)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_dig_file.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_dig_file", *args, **kwargs, nargout=0)
