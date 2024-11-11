from spm.__wrapper__ import Runtime


def _unparcellate(*args, **kwargs):
    """
      UNPARCELLATE performs the reverse of a parcellation, by assigigning each  
        parcel's activation to the vertices that contributed to that parcel.  
         
        Use as  
         
          fun = unparcellate(data, parcellation, parameter, parcelparam, varargin)  
         
        Required inputs:  
         
          data          = structure (or matrix) containing the parcellated functional data  
          parcellation  = structure describing the parcellation, i.e. the parcel  
                          membership for each of the vertices  
          parameter     = string (or cell-array with labels) that specifies the  
                          parameter to be used (if data is a structure) or how to  
                          interpret the rows in the data matrix (if data is a matrix)  
         
        Additional inputs are key-value pairs and pertain to bivariate data with  
        a 'labelcmb' specified in the input argument 'parameter'.  
         
          avgoverref     = 'yes' (or 'no')  
          directionality = 'both' (or 'inflow'/'outflow')  
         
        Outputs:  
          fun = matrix Nvertices x size(data.(parameter),2) (or Nvertices x  
                  size(data,2), containing the unparcellated data  
         
          If the input was bivariate data with a labelcmb, an optional second  
          output argument gives a list of the reference parcels.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/unparcellate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("unparcellate", *args, **kwargs)
