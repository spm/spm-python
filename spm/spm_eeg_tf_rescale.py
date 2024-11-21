from spm.__wrapper__ import Runtime


def spm_eeg_tf_rescale(*args, **kwargs):
    """
      Rescale (avg) spectrogram with nonlinear and/or difference operator  
        FORMAT [D] = spm_eeg_tf_rescale(S)  
         
        S                    - input structure (optional)  
        fields of S:  
          S.D                - MEEG object or filename of M/EEG mat-file  
          S.method           - 'LogR', 'Diff', 'Rel', 'Log', 'Sqrt', 'None'  
          S.timewin          - 2-element vector: start and stop of baseline (ms)  
                               (need to specify this for LogR and Diff)  
          S.pooledbaseline   - take the baseline individually for each trial   
                               (0, default) or pool across trials (1), see    
                               doi: 10.1111/ejn.13179  
          S.Db               - MEEG object or filename of M/EEG mat-file to use  
                               for the baseline (if different from the input dataset).  
          prefix             - prefix for the output file (default - 'r')  
         
        Output:  
          D                  - MEEG object with rescaled power data (also  
                               written to disk with prefix r)  
         
        For 'Log' and 'Sqrt', these functions are applied to spectrogram  
        For 'LogR', 'Rel' and 'Diff' this function computes power in the baseline  
        p_b and outputs (i) p-p_b for 'Diff' (ii) 100*(p-p_b)/p_b for 'Rel'  
                        (iii) log (p/p_b) for 'LogR'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_tf_rescale.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_tf_rescale", *args, **kwargs)
