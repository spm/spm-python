from spm.__wrapper__ import Runtime


def spm_XYZreg(*args, **kwargs):
    """
      Registry for GUI XYZ locations, and point list utility functions  
         
                                   ----------------  
         
        PointList & voxel centre utilities...  
         
        FORMAT [xyz,d] = spm_XYZreg('RoundCoords',xyz,M,D)  
        FORMAT [xyz,d] = spm_XYZreg('RoundCoords',xyz,V)  
        Round specified xyz location to nearest voxel centre  
        xyz - (Input) 3-vector of X, Y & Z locations, in "real" coordinates  
        M   - 4x4 transformation matrix relating voxel to "real" coordinates  
        D   - 3 vector of image X, Y & Z dimensions (DIM)  
        V   - 9-vector of image and voxel sizes, and origin [DIM,VOX,ORIGIN]'  
              M derived as [ [diag(V(4:6)), -(V(7:9).*V(4:6))]; [zeros(1,3) ,1]]  
              DIM    - D  
              VOX    - Voxel dimensions in units of "real" coordinates  
              ORIGIN - Origin of "real" coordinates in voxel coordinates  
        xyz - (Output) coordinates of nearest voxel centre in "real" coordinates  
        d   - Euclidean distance between requested xyz & nearest voxel centre  
         
        FORMAT i = spm_XYZreg('FindXYZ',xyz,XYZ)  
        find position of specified voxel in XYZ pointlist  
        xyz - 3-vector of coordinates  
        XYZ - Pointlist: 3xn matrix of coordinates  
        i   - Column(s) of XYZ equal to xyz  
         
        FORMAT [xyz,i,d] = spm_XYZreg('NearestXYZ',xyz,XYZ)  
        find nearest voxel in pointlist to specified location  
        xyz - (Input) 3-vector of coordinates  
        XYZ - Pointlist: 3xn matrix of coordinates  
        xyz - (Output) coordinates of nearest voxel in XYZ pointlist  
              (ties are broken in favour of the first location in the pointlist)  
        i   - Column of XYZ containing coordinates of nearest pointlist location  
        d   - Euclidean distance between requested xyz & nearest pointlist location  
         
        FORMAT d = spm_XYZreg('Edist',xyz,XYZ)  
        Euclidean distances between coordinates xyz & points in XYZ pointlist  
        xyz - 3-vector of coordinates  
        XYZ - Pointlist: 3xn matrix of coordinates  
        d   - n row-vector of Euclidean distances between xyz & points of XYZ  
         
                                   ----------------  
         
        Registry functions  
         
        FORMAT [hReg,xyz] = spm_XYZreg('InitReg',hReg,M,D,xyz)  
        Initialise registry in graphics object  
        hReg - Handle of HandleGraphics object to build registry in. Object must  
               be un'Tag'ged and have empty 'UserData'  
        M    - 4x4 transformation matrix relating voxel to "real" coordinates,  
               used and stored for checking validity of coordinates  
        D    - 3 vector of image X, Y & Z dimensions (DIM), used  
               and stored for checking validity of coordinates  
        xyz  - (Input) Initial coordinates [Default [0;0;0]]  
               These are rounded to the nearest voxel centre  
        hReg - (Output) confirmation of registry handle  
        xyz  - (Output) Current registry coordinates, after rounding  
         
        FORMAT spm_XYZreg('UnInitReg',hReg)  
        Clear registry information from graphics object  
        hReg - Handle of 'hReg' 'Tag'ged registry HandleGraphics object.  
               Object's 'Tag' & 'UserData' are cleared  
         
        FORMAT xyz = spm_XYZreg('GetCoords',hReg)  
        Get current registry coordinates  
        hReg - Handle of 'hReg' 'Tag'ged registry HandleGraphics object  
         
        FORMAT [xyz,d] = spm_XYZreg('SetCoords',xyz,hReg,hC,Reg)  
        Set coordinates in registry & update registered HGobjects/functions  
        xyz  - (Input) desired coordinates  
        hReg - Handle of 'hReg' 'Tag'ged registry HandleGraphics object  
               If hReg doesn't contain a registry, a warning is printed.  
        hC   - Handle of caller object (to prevent circularities) [Default 0]  
               If caller object passes invalid registry handle, then spm_XYZreg  
               attempts to blank the 'hReg' fiend of hC's 'UserData', printing  
               a warning notification.  
        Reg  - Alternative nx2 cell array Registry of handles / functions  
               If specified, overrides use of registry held in hReg  
               [Default getfield(get(hReg,'UserData'),'Reg')]  
        xyz  - (Output) Desired coordinates are rounded to nearest voxel if hC  
               is not specified, or is zero. Otherwise, caller is assumed to  
               have checked verity of desired xyz coordinates. Output xyz  
               returns coordinates actually set.  
        d    - Euclidean distance between desired and set coordinates.  
         
        FORMAT nReg = spm_XYZreg('XReg',hReg,{h,Fcn}pairs)  
        Cross registration object/function pairs with the registry, push xyz coords  
        hReg - Handle of 'hReg' 'Tag'ged registry HandleGraphics object  
        h    - Handle of HandleGraphics object to be registered  
               The 'UserData' of h must be a structure with an 'Reg' field, which  
               is set to hReg, the handle of the registry (back registration)  
        Fcn  - Handling function for HandleGraphics object h  
               This function *must* accept XYZ updates via the call:  
                       feval(Fcn,'SetCoords',xyz,h,hReg)  
               and should *not* call back the registry with the update!  
               {h,Fcn} are appended to the registry (forward registration)  
        nReg - New registry cell array: Handles are checked for validity before  
               entry. Invalid handles are omitted, generating a warning.  
         
        FORMAT nReg = spm_XYZreg('Add2Reg',hReg,{h,Fcn}pairs)  
        Add object/function pairs for XYZ updates to registry (forward registration)  
        hReg - Handle of 'hReg' 'Tag'ged registry HandleGraphics object  
        h    - Handle of HandleGraphics object to be registered  
        Fcn  - Handling function for HandleGraphics object h  
               This function *must* accept XYZ updates via the call:  
                       feval(Fcn,'SetCoords',xyz,h,hReg)  
               and should *not* call back the registry with the update!  
               {h,Fcn} are appended to the registry (forward registration)  
        nReg - New registry cell array: Handles are checked for validity before  
               entry. Invalid handles are omitted, generating a warning.  
         
        FORMAT spm_XYZreg('SetReg',h,hReg)  
        Set registry field of object's UserData (back registration)  
        h    - Handle of HandleGraphics object to be registered  
               The 'UserData' of h must be a structure with an 'Reg' field, which  
               is set to hReg, the handle of the registry (back registration)  
        hReg - Handle of 'hReg' 'Tag'ged registry HandleGraphics object  
         
        FORMAT nReg = spm_XYZreg('unXReg',hReg,hD1,hD2,hD3,...)  
        Un-cross registration of HandleGraphics object hD  
        hReg - Handle of 'hReg' 'Tag'ged registry HandleGraphics object  
        hD?  - Handles of HandleGraphics object to be unregistered  
               The 'UserData' of hD must be a structure with a 'Reg' field, which  
               is set to empty (back un-registration)  
        nReg - New registry cell array: Registry entries with handle entry hD are  
               removed from the registry (forward un-registration)  
               Handles not in the registry generate a warning  
         
        FORMAT nReg = spm_XYZreg('Del2Reg',hReg,hD)  
        Delete HandleGraphics object hD from registry (forward un-registration)  
        hReg - Handle of 'hReg' 'Tag'ged registry HandleGraphics object  
        hD?  - Handles of HandleGraphics object to be unregistered  
        nReg - New registry cell array: Registry entries with handle entry hD are  
               removed from the registry. Handles not in registry generate a warning  
         
        FORMAT spm_XYZreg('UnSetReg',h)  
        Unset registry field of object's UserData (back un-registration)  
        h - Handle of HandleGraphics object to be unregistered  
            The 'UserData' of hD must be a structure with a 'Reg' field, which  
            is set to empty (back un-registration)  
         
        FORMAT spm_XYZreg('CleanReg',hReg)  
        Clean invalid handles from registry  
        hReg - Handle of 'hReg' 'Tag'ged registry HandleGraphics object  
         
        FORMAT Reg = spm_XYZreg('VReg',Reg,Warn)  
        Prune invalid handles from Registry cell array  
        Reg  - (Input) nx2 cell array of {handle,function} pairs  
        Warn - If specified, print warning if find invalid handles  
        Reg  - (Output) mx2 cell array of valid {handle,function} pairs  
         
        FORMAT hReg = spm_XYZreg('FindReg',h)  
        Find/check registry object  
        h    - handle of Registry, or figure containing Registry (default gcf)  
               If ischar(h), then uses spm_figure('FindWin',h) to locate named figures  
        hReg - handle of confirmed registry object  
               Errors if h is not a registry or a figure containing a unique registry  
               Registry object is identified by 'hReg' 'Tag'  
       __________________________________________________________________________  
         
        spm_XYZreg provides a framework for modular inter-GUI communication of  
        XYZ co-orginates, and various utility functions for pointlist handling  
        and rounding in voxel coordinates.  
        Concept and examples can be found in the body of the function.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_XYZreg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_XYZreg", *args, **kwargs)
