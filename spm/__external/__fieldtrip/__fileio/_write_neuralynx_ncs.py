from spm.__wrapper__ import Runtime


def _write_neuralynx_ncs(*args, **kwargs):
    """
      WRITE_NEURALYNX_NCS writes continuous data to a NCS file  
         
        Use as  
          write_neuralynx_ncs(filename, ncs)  
         
        The input data should be scaled in uV.  
         
        See also READ_NEURALYNX_NCS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_neuralynx_ncs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_neuralynx_ncs", *args, **kwargs, nargout=0)
