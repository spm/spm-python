from spm._runtime import Runtime


def appendstruct(*args, **kwargs):
    """
      APPENDSTRUCT appends a structure or a struct-array to another structure or  
        struct-array. It also works if the initial structure is an empty structure or an  
        empty double array. It also works if the input structures have different fields.  
         
        Use as  
          ab = appendstruct(a, b)  
         
        See also PRINTSTRUCT, MERGESTRUCT, COPYFIELDS, KEEPFIELDS, REMOVEFIELDS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/appendstruct.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("appendstruct", *args, **kwargs)
