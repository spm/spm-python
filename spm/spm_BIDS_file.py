from mpython import Runtime


def spm_BIDS_file(*args, **kwargs):
    """
      Function to create BIDS style filenames for saving and loading data.
        FORMAT [BIDS_file] = spm_BIDS_file(S)

        Input Parameters:
            S:         Struct containing input parameters
                category = 1xn char, describing the BIDS or derivative category.
                          e.g. 'meg' (optional);
                description = 1xn char, describes the filename ending. e.g.
                          'channels' (optional)
                type = 1xn char, describes file type, or extension. e.g. '.tsv'
                          (default: '.mat').
                derivative = boolean, whether or not the output is a derivative
                          (default: true).
                detailed = boolean, whether to include ses/task/run info in output
                          (default: true).
                prefix = 1xn char, describes the prefix to the filename. Useful
                          for when spm functions have added a prefix.
                BIDS: Struct containing BIDS information
                    directory = 1xn char providing BIDS directory.
                    sub = cell array or string, containing subject names.
                    ses = cell array or string, containing session names.
                    task = cell array or string, containing task names.
                    run = cell array or string, containing run names.

        Output:
            outputs: Array of structures containing directory information
                     with fields:
                     - file: Full path and filename
                     - folder: Directory path
                     - name: Full filename
                     - ext: File extension
                     - exists: Boolean, does the file exist already?
                     - + bids fields, sub, ses, task, run
       _________________________________________________________________________

        Further help:

        spm_BIDS_file is a function that takes an input of BIDS parameters, along
        with some additional specification of the way to handle those parameters,
        and provides a single, or array, of file directories. This method may be
        used within a loop that, for example, takes a list of subject names and
        updates S.BIDS.sub, or by providing the function with the list of subject
        names directly. If insufficient information is provided the method
        assumes this is intentional and provides a limited output. This may be
        useful for accessing files which are independent of the task/run, such as
        an anatomical image in an MEG study. Or, for when only a single session
        is used, and is excluded from the file specification.

        Note, when S.derivative = false, this function will not create new
        folders, to avoid breaking the organisation of existing data. Otherwise,
        it will create a new folder. The function never checks if the file
        exists.

        Note, this function does not enforce BIDS standards
        (found here: https://bids-specification.readthedocs.io), see spm_BIDS for
        associated methods and checks. For example, the parameter S.prefix is
        there to make it easier to work with files produced by SPM, rather than
        maintaining the BIDS standard.

       _________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_BIDS_file.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_BIDS_file", *args, **kwargs)
