from spm.__wrapper__ import Runtime


def _appendstruct(*args, **kwargs):
    """
      APPENDSTRUCT appends a structure or a struct-array to another structure or  
        struct-array. It also works if the initial structure is an empty structure or an  
        empty double array. It also works if the input structures have different fields.  
         
        Use as  
          ab = appendstruct(a, b)  
         
        See also PRINTSTRUCT, MERGESTRUCT, COPYFIELDS, KEEPFIELDS, REMOVEFIELDS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/appendstruct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("appendstruct", *args, **kwargs)
