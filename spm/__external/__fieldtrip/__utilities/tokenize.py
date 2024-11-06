from spm.__wrapper__ import Runtime


def tokenize(*args, **kwargs):
    """
      TOKENIZE cuts a string into pieces, returning the pieces in a cell-array  
         
        Use as  
          t = tokenize(str)  
          t = tokenize(str, sep)  
          t = tokenize(str, sep, rep)  
        where  
          str = the string that you want to cut into pieces  
          sep = the separator at which to cut (default is whitespace)  
          rep = whether to treat repeating separator characters as one (default is false)  
         
        With the optional boolean flag "rep" you can specify whether repeated  
        separator characters should be squeezed together (e.g. multiple  
        spaces between two words). The default is rep=1, i.e. repeated  
        separators are treated as one.  
         
        See also STRSPLIT, SPLIT, STRTOK, TEXTSCAN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/tokenize.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tokenize", *args, **kwargs)
