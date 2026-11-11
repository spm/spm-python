from spm._runtime import Runtime


def _equidistant_locate(*args, **kwargs):
    r"""
      EQUIDISTANT_LOCATE determines electrode positions that are distributed  
        equidistantly on a scalp surface that is described by a triangulation  
         
        See also ELEC1020_LOCATE, FT_ELECTRODEPLACEMENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/equidistant_locate.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("equidistant_locate", *args, **kwargs)
