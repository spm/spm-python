from spm.__wrapper__ import Runtime


def _write_neuralynx_nse(*args, **kwargs):
    """
      WRITE_NEURALYNX_NSE writes spike timestamps and waveforms to a NSE file  
        The input data should be scaled in uV.  
         
        Use as  
          write_neuralynx_nse(filename, nse)  
         
        See also READ_NEURALYNX_NSE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/write_neuralynx_nse.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_neuralynx_nse", *args, **kwargs, nargout=0)
