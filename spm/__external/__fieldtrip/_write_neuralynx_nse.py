from spm._runtime import Runtime


def _write_neuralynx_nse(*args, **kwargs):
    r"""
      WRITE_NEURALYNX_NSE writes spike timestamps and waveforms to a NSE file  
        The input data should be scaled in uV.  
         
        Use as  
          write_neuralynx_nse(filename, nse)  
         
        See also READ_NEURALYNX_NSE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/write_neuralynx_nse.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_neuralynx_nse", *args, **kwargs, nargout=0)
