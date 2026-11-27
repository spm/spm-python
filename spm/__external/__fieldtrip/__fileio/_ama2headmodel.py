from spm._runtime import Runtime


def _ama2headmodel(*args, **kwargs):
    r"""
      AMA2HEADMODEL converts a dipoli structure with boundary geometries  
        and a boundary element method transfer matrix to a volume conduction  
        model.  
         
        Use as  
          headmodel = ama2headmodel(ama)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/ama2headmodel.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ama2headmodel", *args, **kwargs)
