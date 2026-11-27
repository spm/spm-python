from spm._runtime import Runtime


def _write_neuralynx_ncs(*args, **kwargs):
    r"""
      WRITE_NEURALYNX_NCS writes continuous data to a NCS file  
         
        Use as  
          write_neuralynx_ncs(filename, ncs)  
         
        The input data should be scaled in uV.  
         
        See also READ_NEURALYNX_NCS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/write_neuralynx_ncs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_neuralynx_ncs", *args, **kwargs, nargout=0)
