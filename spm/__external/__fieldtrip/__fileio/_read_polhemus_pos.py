from spm._runtime import Runtime


def _read_polhemus_pos(*args, **kwargs):
    r"""
      READ_POLHEMUS_POS reads electrode positions measured with the Polhemus tracker in  
        one of the EEG labs at the DCCN. The software used with the Polhemus is from CTF.  
         
        Use as:  
          [elec] = read_polhemus_pos(filename)  
         
        This returns an electrode structure with  
          elec.label     cell-array with electrode labels (strings)  
          elec.pnt       position of each electrode  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_polhemus_pos.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_polhemus_pos", *args, **kwargs)
