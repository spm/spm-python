from spm._runtime import Runtime


def _read_smi_txt(*args, **kwargs):
    r"""
      READ_SMI_TXT reads the header information, input triggers, messages  
        and all data points from an SensoMotoric Instruments (SMI) *.txt file  
         
        Use as  
          smi = read_smi_txt(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_smi_txt.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_smi_txt", *args, **kwargs)
