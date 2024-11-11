from spm.__wrapper__ import Runtime


def _retriangulate(*args, **kwargs):
    """
      RETRIANGULATE projects a triangulation onto another triangulation  
        thereby providing a a new triangulation of the old one.  
         
        Use as  
          [pnt, tri] = retriangulate(pnt1, tri1, pnt2, tri2, flag)  
        where  
          pnt1, tri1  describe the desired surface   
          pnt2, tri2  describe the triangulation that will be projected on surface 1  
         
        The optional flag determines whether the center of the triangulations should be  
        shifted to the origin before the projection is done. The resulting surface will  
        be shifted back to its original location.  
         
        flag=0 means no shift (default)  
        flag=1 means shifting to the geometrical mean of the respective triangulations  
        flag=2 means shifting to the center of the bounding box of the respective triangulations  
        flag=3 means shifting to the geometrical mean of the first triangulation  
        flag=4 means shifting to the center of the bounding box of the first triangulation  
        flag=5 means shifting to the geometrical mean of the second triangulation  
        flag=6 means shifting to the center of the bounding box of the second triangulation  
         
        The projection is done from the coordinate system origin (0,0,0).  
         
        See also ICOSAHEDRONxxx, ISOSURFACE, REDUCEPATCH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/retriangulate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("retriangulate", *args, **kwargs)
