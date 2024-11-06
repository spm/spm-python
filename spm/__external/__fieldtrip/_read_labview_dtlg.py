from spm.__wrapper__ import Runtime


def _read_labview_dtlg(*args, **kwargs):
    """
      READ_LABVIEW_DTLG  
         
        Use as  
          dat = read_labview_dtlg(filename, datatype)  
        where datatype can be 'int32' or 'int16'  
         
        The output of this function is a structure.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_labview_dtlg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_labview_dtlg", *args, **kwargs)
