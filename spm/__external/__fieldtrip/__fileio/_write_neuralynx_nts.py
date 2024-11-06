from spm.__wrapper__ import Runtime


def _write_neuralynx_nts(*args, **kwargs):
    """
      WRITE_NEURALYNX_NTS writes spike timestamps to a NTS file  
         
        Use as  
          write_neuralynx_nts(filename, nts)  
         
        See also READ_NEURALYNX_NTS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_neuralynx_nts.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_neuralynx_nts", *args, **kwargs, nargout=0)
