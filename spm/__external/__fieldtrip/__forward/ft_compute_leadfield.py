from spm.__wrapper__ import Runtime


def ft_compute_leadfield(*args, **kwargs):
    """
      FT_COMPUTE_LEADFIELD computes a forward solution for a dipole in a a volume  
        conductor model. The forward solution is expressed as the leadfield matrix  
        (Nchan*3), where each column corresponds with the potential or field distributions  
        on all sensors for one of the x,y,z-orientations of the dipole.  
         
        Use as  
          [lf] = ft_compute_leadfield(dippos, sens, headmodel, ...)  
        with input arguments  
          dippos    = position dipole (1*3 or Ndip*3)  
          sens      = structure with gradiometer or electrode definition  
          headmodel = structure with volume conductor definition  
         
        The headmodel represents a volume conductor model, its contents  
        depend on the type of model. The sens structure represents a sensor  
        array, i.e. EEG electrodes or MEG gradiometers.  
         
        It is possible to compute a simultaneous forward solution for EEG and MEG  
        by specifying sens and grad as two cell-arrays, e.g.  
          sens       = {senseeg, sensmeg}  
          headmodel  = {voleeg,  volmeg}  
        This results in the computation of the leadfield of the first element of  
        sens and headmodel, followed by the second, etc. The leadfields of the  
        different imaging modalities are subsequently concatenated.  
         
        Additional input arguments can be specified as key-value pairs, supported  
        optional arguments are  
          'reducerank'      = 'no' or number (default = 3 for EEG, 2 for MEG)  
          'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')  
          'normalize'       = 'no', 'yes' or 'column' (default = 'no')  
          'normalizeparam'  = parameter for depth normalization (default = 0.5)  
          'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)  
         
        The leadfield weight may be used to specify a (normalized) corresponding surface  
        area for each dipole, e.g. when the dipoles represent a folded cortical surface  
        with varying triangle size.  
         
        Depending on the specific input arguments for the sensor and volume, this function  
        will select the appropriate low-level EEG or MEG forward model. The leadfield  
        matrix for EEG will have an average reference over all the electrodes.  
         
        The supported forward solutions for MEG are  
          infinite homogenous medium  
          single sphere (Cuffin and Cohen, 1977)  
          multiple spheres with one sphere per channel (Huang et al, 1999)  
          realistic single shell using superposition of basis functions (Nolte, 2003)  
          leadfield interpolation using a precomputed sourcemodel  
          boundary element method (BEM)  
         
        The supported forward solutions for EEG are  
          infinite homogenous medium  
          infinite halfspace homogenous medium  
          single sphere  
          multiple concentric spheres (up to 4 spheres)  
          leadfield interpolation using a precomputed sourcemodel  
          boundary element method (BEM)  
          finite element method (FEM)  
         
        See also FT_PREPARE_VOL_SENS, FT_HEADMODEL_ASA, FT_HEADMODEL_BEMCP,  
        FT_HEADMODEL_CONCENTRICSPHERES, FT_HEADMODEL_DIPOLI, FT_HEADMODEL_HALFSPACE,  
        FT_HEADMODEL_INFINITE, FT_HEADMODEL_LOCALSPHERES, FT_HEADMODEL_OPENMEEG,  
        FT_HEADMODEL_SINGLESHELL, FT_HEADMODEL_SINGLESPHERE,  
        FT_HEADMODEL_HALFSPACE, FT_HEADMODEL_DUNEURO  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_compute_leadfield.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_compute_leadfield", *args, **kwargs)
