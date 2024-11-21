from spm.__wrapper__ import Runtime


def spm_eeg_remove_spikes(*args, **kwargs):
    """
      Use Will Pennys robust GLM code to remove 'spikes' from continuous data.  
        Such spikes occur in EEG data recorded with the CTF MEG system at FIL  
        due to some obscure electrical problem.  
         
        FORMAT Dnew = spm_eeg_remove_spikes(S)  
         
        S         - struct (optional)  
        (optional) fields of S:  
        S.D      - meeg object or filename  
        S.logbf  - clean a block if log bayes factor in favour of spike model is  
                   bigger than this (default - 3)  
        S.hpf    - high-pass frequency above which to look for spikes (default 40 Hz)  
        S.fast   - option to speed up the function by only using GLM if there is  
                   threshold crossing ('yes', or check all the data with GLM - 'no')  
        S.fasthresh - threshold for the fast option (in STD) - default 4  
        S.trialbased - use trials in the data as they are ('yes') or break them  
                     into sub-blocks ('no' - default)  
        S.channels - channels to clean up (default 'gui' - brings up a GUI for  
                    channel choice.  
         
        Output:  
        Dnew  - MEEG object with data cleaned of spikes.  
         
         
        Disclaimer: this code is provided as an example and is not guaranteed to work  
        with data on which it was not tested. If it does not work for you, feel  
        free to improve it and contribute your improvements to the MEEGtools toolbox  
        in SPM (http://www.fil.ion.ucl.ac.uk/spm)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_remove_spikes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_remove_spikes", *args, **kwargs)
