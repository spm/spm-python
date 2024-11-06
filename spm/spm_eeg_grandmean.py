from spm.__wrapper__ import Runtime


def spm_eeg_grandmean(*args, **kwargs):
    """
      Average over multiple M/EEG data sets  
        FORMAT Do = spm_eeg_grandmean(S)  
         
        S         - struct (optional)  
         fields of S:  
          D         - filenames (char matrix) of M/EEG MAT-files containing  
                      epoched data  
          weighted  - average weighted by number of replications in inputs (1)  
                      or not (0) [default: 0]  
          outfile   - name of the output file [default: 'grand_mean']  
         
        Output:  
        Do        - EEG data struct, result files are saved in the same  
                    directory as first input file.  
       __________________________________________________________________________  
         
        spm_eeg_grandmean averages data over multiple files. The data must have  
        the same trialtype numbering and sampling rate. This function can be used  
        for grand mean averaging, i.e. computing the average over multiple  
        subjects. Missing event types and bad channels are taken into account  
        properly. The output is written to a user-specified new file. The default  
        name is the same name as the first selected input file, but prefixed with  
        a 'g'. The output file is written to the current working directory.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_grandmean.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_grandmean", *args, **kwargs)
