from mpython import Runtime


def mne_ex_cancel_noise(*args, **kwargs):
    """

          Do projection and compensation as needed
          Return the appropriate operators

          [res,proj,comp] = mne_ex_cancel_noise(data,dest_comp)

          res     - Data after noise cancellation
          proj    - The projection operator applied
          comp    - The compensator which brings uncompensated data to the
                    desired compensation grade (will be useful in forward
                    calculations)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_ex_cancel_noise.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_ex_cancel_noise", *args, **kwargs)
