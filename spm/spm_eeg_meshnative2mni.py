from spm._runtime import Runtime


def spm_eeg_meshnative2mni(*args, **kwargs):
    r"""
     function nativemesh=spm_eeg_meshmni2native(mnimesh,mesh)  
        Uses mesh ( spm mesh structure D.inv{:}.mesh ) to compute transform to   
        express mnimesh in native space  
        replicates code segment from headmodel section of SPM code  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_meshnative2mni.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_meshmni2native", *args, **kwargs)
