from spm.__wrapper__ import Runtime


def mne_read_epoch(*args, **kwargs):
    """
       
        [data,fid] = mne_read_epoch(epoch_info,which,prev_fid)  
         
        Reads an epoch from a binary file produced by mne_epochs2mat  
         
        epoch_info - The data structure read from the epoch data description file  
        which      - Which epoch to read  
        prev_fid   - Open file id from previous call  
                     if prev_fid < 0 or missing, the file will be opened  
                     The the current file id will be returned in the  
                     output argument fid, if present. If this argument is  
                     missing, file will be close upon exit from this function.  
         
        The data will contain nchan x ntimes calibrated values  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_read_epoch.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_read_epoch", *args, **kwargs)
