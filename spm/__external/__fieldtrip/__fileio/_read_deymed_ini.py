from spm._runtime import Runtime


def _read_deymed_ini(*args, **kwargs):
    r"""
      READ_DEYMED_INI reads EEG data from the Deymed Truescan file format  
         
        Use as  
          hdr = read_deymed_ini(filename)  
         
        See also READ_DEYMED_DAT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_deymed_ini.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_deymed_ini", *args, **kwargs)
