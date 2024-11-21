from spm.__wrapper__ import Runtime


def spm_eeg_avgtime(*args, **kwargs):
    """
      Average a TF-dataset over time to get a spectrum dataset  
        FORMAT D = spm_eeg_avgtime(S)  
         
        S        - input struct  
         fields of S:  
          D        - MEEG object or filename of M/EEG mat-file with epoched data    
          timewin  - time window to average over {in PST ms} [default: [-Inf,Inf]]  
          prefix   - prefix for the output file [default: 'S']  
         
         
        Output:  
        D        - MEEG object   
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_avgtime.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_avgtime", *args, **kwargs)
