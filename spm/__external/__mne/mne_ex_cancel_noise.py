from spm._runtime import Runtime


def mne_ex_cancel_noise(*args, **kwargs):
    r"""
       
          Do projection and compensation as needed  
          Return the appropriate operators  
            
          [res,proj,comp] = mne_ex_cancel_noise(data,dest_comp)  
         
          res     - Data after noise cancellation  
          proj    - The projection operator applied  
          comp    - The compensator which brings uncompensated data to the  
                    desired compensation grade (will be useful in forward  
                    calculations)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_ex_cancel_noise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_ex_cancel_noise", *args, **kwargs)
