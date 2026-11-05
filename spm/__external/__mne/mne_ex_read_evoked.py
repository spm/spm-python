from spm._runtime import Runtime


def mne_ex_read_evoked(*args, **kwargs):
    r"""
       
          Load one evoked-response data set and do various kinds  
          of preprocessing  
         
          [res] = mne_ex_read_evoked(fname,setno,apply_proj,dest_comp,use_ctf_head)  
         
          fname           - Name of the data file  
          setno           - Data set number (default = 1)  
          apply_proj      - Apply SSP to the data (default = true)  
          dest_comp       - Desired (CTF/4D) compensation in the output data (default = keep the one in the file)  
          use_ctf_head    - Use the CTF/4D head coordinate system instead of the  
                            Neuromag one if available  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_ex_read_evoked.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_ex_read_evoked", *args, **kwargs)
