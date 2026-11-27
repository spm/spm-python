from spm._runtime import Runtime


def _dimlength(*args, **kwargs):
    r"""
      DIMLENGTH(DATA, SELDIM, FLD) is a helper function to obtain n, the number  
        of elements along dimension seldim from the appropriate field from the  
        input data containing functional data.  
         
        Use als  
          [n, fn] = dimlength(data, seldim, fld)  
         
        It can be called with one input argument only, in which case it will  
        output two cell arrays containing the size of the functional fields,  
        based on the XXXdimord, and the corresponding XXXdimord fields.  
         
        When the data contains a single dimord field (everything except source  
        data), the cell-arrays in the output only contain one element.  
         
        See also FIXSOURCE, CREATEDIMORD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/dimlength.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dimlength", *args, **kwargs)
