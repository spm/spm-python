from spm.__wrapper__ import Runtime


def bf_inverse_champagne(*args, **kwargs):
    """
      Computes Champagne filters  
         
        See Owen et al. Performance evaluation of the Champagne source   
        reconstruction algorithm on simulated and real M/EEG data. Neuroimage.  
        2012 Mar;60(1):305-23  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_champagne.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_inverse_champagne", *args, **kwargs)
