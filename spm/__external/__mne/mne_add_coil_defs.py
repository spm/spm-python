from spm._runtime import Runtime


def mne_add_coil_defs(*args, **kwargs):
    r"""
       
        [res] = mne_add_coil_defs(chs,accuracy,coil_def_templates)  
         
        Add transformed coil definitions to the channel info  
         
        chs        - original channel definitions  
        accuracy   - desired accuracy (0, 1, or 2, defaults to 1)  
        templates  - coil definition templates  
                     (defaults to $MNE_ROOT/setup/mne/coil_def.dat or $MNE_ROOT/share/mne/coil_def.dat)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_add_coil_defs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_add_coil_defs", *args, **kwargs)
