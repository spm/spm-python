from spm.__wrapper__ import Runtime


def _parameterselection(*args, **kwargs):
    """
      PARAMETERSELECTION selects the parameters that are present as a volume in the data  
        add that have a dimension that is compatible with the specified dimensions of the  
        volume, i.e. either as a vector or as a 3D volume.  
         
        Use as  
          [select] = parameterselection(param, data)  
        where  
          param    cell-array, or single string, can be 'all'  
          data     structure with anatomical or functional data  
          select   returns the selected parameters as a cell-array  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/parameterselection.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("parameterselection", *args, **kwargs)
