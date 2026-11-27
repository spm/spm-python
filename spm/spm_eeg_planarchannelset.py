from spm._runtime import Runtime


def spm_eeg_planarchannelset(*args, **kwargs):
    r"""
      Define the planar gradiometer channel combinations  
        FORMAT planar = spm_eeg_planarchannelset(data)  
         
        The output cell array contains the horizontal label, vertical label and  
        the label after combining the two.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_planarchannelset.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_planarchannelset", *args, **kwargs)
