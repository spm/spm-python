from spm.__wrapper__ import Runtime


def help2cell(*args, **kwargs):
  """  HELP2CELL - translate help texts into cell arrays  
    cellhelp = help2cell(topic)  
    Create a cell array of help strings from the MATLAB help on 'topic'.  
    If a line ends with a ' ', it is assumed to be continued and the next   
    line will be appended, thus creating one cell per paragraph.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/help2cell.m)
  """

  return Runtime.call("help2cell", *args, **kwargs)
