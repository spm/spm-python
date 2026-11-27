from spm._runtime import Runtime


def _avgref(*args, **kwargs):
    r"""
      AVGREF computes the average reference in each column  
          [data] = avgref(data)  
         
        or it computes the re-referenced data relative to the  
        average over the selected channels  
          [data] = avgref(data, sel)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/avgref.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("avgref", *args, **kwargs)
