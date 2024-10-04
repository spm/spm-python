from spm.__wrap__ import _Runtime, _MatlabClassWrapper


class cfg_intree(_MatlabClassWrapper):
  def __init__(self, *args, _objdict=None, **kwargs):
    """  This is currently only a "marker" class that should be inherited by all  
    within-tree classes. It does not add fields and does not have methods.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
    
      Documentation for cfg_intree  
         doc cfg_intree  
    
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/@cfg_intree/cfg_intree.m)
    """

    if _objdict is None:
      _objdict = _Runtime.call("cfg_intree", *args, **kwargs)
    super().__init__(_objdict)

  def disp(self, *args, **kwargs):
    """  function disp(varargin)  
    This class should not display any information about its structure.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/@cfg_intree/disp.m)
    """

    return _Runtime.call("disp", self._as_matlab_object(), *args, **kwargs)


  def display(self, *args, **kwargs):
    """  function display(varargin)  
    This class should not display any information about its structure.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/@cfg_intree/display.m)
    """

    return _Runtime.call("display", self._as_matlab_object(), *args, **kwargs)


