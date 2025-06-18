from mpython import Runtime


def spm_depth(*args, **kwargs):
    """
      Create an image of cortical depth.
        FORMAT spm_depth(P)
        P - filenames for GM and WM maps.

        A skeletonisation is saved, along with a map of
        cortical depth.

        In principle, cortical depth can be determined from maps
        of GM and WM. However, opposite banks of sulci usually touch
        making it difficult to identify the outer surface of the brain.

        This code uses maps of GM and WM to:
        1. Obtain a map of background (i.e. BG = 1-GM-WM).
        2. Takes a binary map of GM+BG>0.5, and does a topology
           preserving conditional erosion (conditional on BG>0.5)
           to try to identify voxels running along the medial surface
           of sulci. The end result is a sort of binary skeletonisation
           that tries to generate medial surfaces.
        3. Combine the GM, WM and BG with the skeletonisation, giving
           mGM, mWM and mBG.
        4. Compute Euclidean distances of all voxels from the mWM map (d2).
        5. Compute Euclidean distances of all voxels from the mBG map (d3).
        6. Save a depth map computed from d3./(d2+d3)

        The end result is not perfect because it is susceptible to segmentation
        imperfections, particularly in relation to isolated speckles of WM, or
        incorrect WM topology. Also, the medial surface is mid-way between the
        inner and outer surfaces, which may not always be optimal. Thresholding
        segmentation probabilities at 0.5 is a bit arbitrary, but a probabilistic
        topology-preserving erosion would be very slow.

        While the results may not be exactly correct, they are probably a
        better approximation than would be obtained from not doing the
        skeletonisation. Cortical regions to worry about most will be those
        close to the cerebellum.  It will also do strange things for cortical
        regions close to subcortical GM structures.


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_depth.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_depth", *args, **kwargs, nargout=0)
