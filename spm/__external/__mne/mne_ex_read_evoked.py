from spm.__wrapper__ import Runtime


def mne_ex_read_evoked(*args, **kwargs):
    """
       
          Load one evoked-response data set and do various kinds  
          of preprocessing  
         
          [res] = mne_ex_read_evoked(fname,setno,apply_proj,dest_comp,use_ctf_head)  
         
          fname           - Name of the data file  
          setno           - Data set number (default = 1)  
          apply_proj      - Apply SSP to the data (default = true)  
          dest_comp       - Desired (CTF/4D) compensation in the output data (default = keep the one in the file)  
          use_ctf_head    - Use the CTF/4D head coordinate system instead of the  
                            Neuromag one if available  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_ex_read_evoked.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_ex_read_evoked", *args, **kwargs)
