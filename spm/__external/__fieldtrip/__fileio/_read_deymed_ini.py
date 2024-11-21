from spm.__wrapper__ import Runtime


def _read_deymed_ini(*args, **kwargs):
    """
      READ_DEYMED_INI reads EEG data from the Deymed Truescan file format  
         
        Use as  
          hdr = read_deymed_ini(filename)  
         
        See also READ_DEYMED_DAT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_deymed_ini.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_deymed_ini", *args, **kwargs)
