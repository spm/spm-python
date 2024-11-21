from spm.__wrapper__ import Runtime


def _printstruct_as_table(*args, **kwargs):
    """
      PRINTSTRUCT_AS_TABLE prints a struct-array as a table in Markdown format  
         
        Example  
          s(1).a = 1  
          s(1).b = 2  
          s(2).a = 3  
          s(2).b = 4  
          printstruct_as_table(s)  
         
        See also PRINTSTRUCT, APPENDSTRUCT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/printstruct_as_table.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("printstruct_as_table", *args, **kwargs, nargout=0)
