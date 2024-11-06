from spm.__wrapper__ import Runtime


def _read_smi_txt(*args, **kwargs):
    """
      READ_SMI_TXT reads the header information, input triggers, messages  
        and all data points from an SensoMotoric Instruments (SMI) *.txt file  
         
        Use as  
          smi = read_smi_txt(filename)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_smi_txt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_smi_txt", *args, **kwargs)
